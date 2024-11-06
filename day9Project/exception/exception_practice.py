# 2단에서 9단까지의 구구단을 선택해서 한개의 단을 출력처리함
# 키보드로 출력할 단을 입력받아서 진행함
# 입력된 단수는 정수여야 함 (예외처리)
# 입력된 단수는  2~ 9 사이의 값이여야 구구단 출력됨
# 입력된 단수가 2보다 작으면 단수는 2로 처리함
# 입력된 단수가 9보다 크면 단수는 9로 처리함
# try: except: else: finally: 형식으로 작성함

def gugudan():
    while True:
        try:
            user_input = input("2~9 사이의 단을 입력하세요 (종료하려면 'exit' 입력): ")
            if user_input.lower() == 'exit':
                print("구구단 프로그램을 종료합니다.")
                break
            input_dan = int(user_input)
            input_dan = 2 if input_dan < 2 else 9 if input_dan > 9 else input_dan
        except ValueError:
            print("정수를 입력하세요.\n")
            continue  # 잘못된 입력일 경우 다시 입력 받기
        except Exception as e:
            print(f"예상치 못한 에러 발생: {e}")
            continue
        else:
            for i in range(1, 10):
                print(f"{input_dan} x {i} = {input_dan * i}")
        finally:
            print("입력 처리가 완료되었습니다.\n")  # 항상 실행되는 블록

if __name__ =="__main__":
    gugudan()