# loop\\whileMission.py | loop/whileMission.py
# module: loop.whileMission
# 파이썬에서의 while 문 사용 테스트 스크립트

#  이 파이썬 스크립트 파일을 실행파일로 만들고자 한다면
#  아래쪽에 main 코드 추가하면 됨


# while 문 실습문제
'''  prompt 변수를 while 문으로 반복해서 출력하면서, 입력되는 번호에 따라
sungjuk_list 의 아이템을 추가하거나 삭제하거나 출력되게 작성하시오.
1 입력 : 리스트에 아이템 값들을 입력받아 추가함
  번호 : 24 (sno : int)
  이름 : 이순신 (sname : str)
  점수 : 100 (score : int)
  ==> 리스트에 추가 처리함    ==> 새로운 학생정보가 추가되었습니다.  출력함
2 입력 : 리스트의 인덱스 위치의 아이템 제거함
  현재 저장된 아이템의 갯수는 3개 입니다.  출력함
  제거할 아이템의 순번 : 3    ==> 입력받은 인덱스 위치의 아이템 제거함
  ==> 3번 위치의 아이템이 제거되었습니다.  출력함   ==> 현재 저장된 아이템의 갯수는 2개 입니다.  출력함
  ==> 잘못된 인덱스 입력시 :   '순번이 잘못 입력되었습니다. 확인하고 다시 입력하세요.' 출력함
3 입력 : 저장된 리스트 정보 아이템별로 출력함
  0 : [12, '홍길동', 98]
  1 : [15, '김유신', 87]
  2 : .......
4 입력 : while 반복 종료함
  성적관리 프로그램이 종료되었습니다.  출력함
'''


def sungjuk_process():
    # sungjuk_list : [sno, sname, score]
    sungjuk_list = []

    prompt = '''
    '1. 입력 | 2. 삭제 | 3. 출력 | 4. 종료'
  '''
    while True:
        print(prompt)
        try:
            num = int(input('메뉴 입력: '))
        except ValueError:
            print("정수를 입력해주세요.")
            continue  # 다시 입력받기 위해 루프 처음으로 돌아감

        if num == 1:
            try:
                sno = int(input('\n번호 : '))
            except ValueError:
                print('번호를 다시 입력하세요.')
                continue  # 번호 입력이 실패하면 다시 루프 시작

            sname = input('이름 : ').strip()
            if not sname:
                print('이름을 입력해 주세요.')
                continue  # 이름이 비어있으면 다시 입력받기

            try:
                score = int(input('점수 : '))
            except ValueError:
                print('점수를 다시 입력하세요.')
                continue  # 점수 입력이 실패하면 다시 루프 시작

            # 모든 입력이 유효하면 리스트에 추가
            sungjuk_list.append([sno, sname, score])
            print('==> 새로운 학생정보가 추가되었습니다.')

        elif num == 2:
            if len(sungjuk_list) == 0:
                print('==> 현재 저장된 아이템의 갯수는 0개 입니다.')
                continue

            rem_item_seq = int(input('제거할 아이템의 순번: '))
            if rem_item_seq < 0 or rem_item_seq > len(sungjuk_list):
                print('순번이 잘못 입력되었습니다. 확인하고 다시 입력하세요.')
                continue # 순번 입력이 실패하면 루프 재시작
            sungjuk_list.remove(sungjuk_list[rem_item_seq - 1])
            print(f'==> {rem_item_seq}번 위치의 아이템이 제거되었습니다.')
            print(f'==> 현재 저장된 아이템의 개수는 {len(sungjuk_list)}개 입니다.')

        elif num == 3:
            if len(sungjuk_list) == 0:
                print('==> 현재 저장된 아이템의 개수는 0개 입니다.')
                continue
            print('==> 저장된 리스트 정보 출력')
            for i, item in enumerate(sungjuk_list, 0):
                print(f'{i}: {item}')
        elif num == 4:
            print('==> 성적관리 프로그램이 종료되었습니다.')
            break

        else:
            print('순번이 잘못 입력되었습니다. 확인하고 다시 입력하세요.')
            continue
