import cx_Oracle
import numpy as np
import cv2
import pytesseract
import sys
import oraclecommon.dbConnectTemplate as dbtemp


# Tesseract 실행 파일 경로를 설정
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def reorderPts(pts):
    idx = np.lexsort((pts[:, 1], pts[:, 0]))
    pts = pts[idx]

    if pts[0, 1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]]

    if pts[2, 1] < pts[3, 1]:
        pts[[2, 3]] = pts[[3, 2]]

    return pts

def clean_data(data):
    """
    데이터 클렌징 함수.
    Args:
        data (str): 클렌징할 문자열
    Returns:
        str: 클렌징된 문자열
    """
    return ''.join(e for e in data if e.isalnum() or e.isspace()).strip()

def camerain():
    filenames = ['./images/sample01.jpg', './images/sample02.jpg', './images/sample03.jpg']
    data_list = []

    for filename in filenames:
        print(f'파일이름 : {filename}')
        src = cv2.imread(filename)
        if src is None:
            print('이미지 로드 실패')
            sys.exit()

        dh, dw = src.shape[:2]
        srcQuad = np.array([[0, 0], [0, 0], [0, 0], [0, 0]], np.float32)
        dstQuad = np.array([[0, 0], [0, dh], [dw, dh], [dw, 0]], np.float32)
        dst = np.zeros((dh, dw), np.uint8)

        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        _, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        for pts in contours:
            if cv2.contourArea(pts) < 10:
                continue

            approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)

            if not cv2.isContourConvex(approx) or len(approx) != 4:
                continue

            cv2.polylines(src, [approx], True, (0, 255, 0), 2, cv2.LINE_AA)
            srcQuad = reorderPts(approx.reshape(4, 2).astype(np.float32))

            pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
            dst = cv2.warpPerspective(src, pers, (dw, dh), flags=cv2.INTER_CUBIC)

            dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
            result = pytesseract.image_to_string(dst_rgb, lang='Hangul+eng')
            print(result)

        cv2.waitKey()
        cv2.destroyAllWindows()

        list = [item for item in result.split('\n') if item]
        data = {}
        for i in range(len(list)):
            if i == len(list) - 1:
                data['tel'] = list[i]  # 'phone'을 'tel'로 변경
            elif 'name' not in data:
                data['name'] = list[i]
            else:
                data['name'] = data['name'] + list[i]
        data_list.append(data)

    outputDB(data_list)

def outputDB(data_list):
    delete_query = 'DELETE FROM vision'
    conn = dbtemp.connect()
    cursor = conn.cursor()

    try:
        # 기존 데이터 삭제
        dbtemp.execute_query(cursor, delete_query)
        dbtemp.commit(conn)
        print('vision 테이블 데이터 삭제 성공')
    except cx_Oracle.Error as e:
        dbtemp.rollback(conn)
        print('vision 테이블 데이터 삭제 실패:', e)
    finally:
        cursor.close()
        dbtemp.close(conn)

    # 새 데이터 삽입
    insert_query = 'INSERT INTO vision (name, tel) VALUES (:1, :2)'  # 'phone'을 'tel'로 변경
    for data in data_list:
        conn = dbtemp.connect()
        cursor = conn.cursor()

        # 데이터 클렌징
        name = clean_data(data.get('name', ''))
        tel = clean_data(data.get('tel', ''))  # 'phone'을 'tel'로 변경

        tp_data = (name, tel)
        print(f'{name} 데이터 삽입 중')

        try:
            print(f'Executing query: {insert_query} with data: {tp_data}')  # 디버깅용 출력
            dbtemp.execute_query(cursor, insert_query, tp_data)
            dbtemp.commit(conn)
            print(f'{name} 데이터 삽입 성공')
        except cx_Oracle.Error as e:
            dbtemp.rollback(conn)
            print(f'{name} 데이터 삽입 실패:', e)
        finally:
            cursor.close()
            dbtemp.close(conn)

if __name__ == '__main__':
    dbtemp.oracle_init()
    camerain()
