# test_dict 디렉토리 안에 있는 dict_sample.py 파일 안의 함수를 사용하려면
# import 문을 사용해서 임포트 선언해야 함

# 모듈: 함수를 가지고 있는 파이썬 파일
# import 파일명 => 같은 디렉토리 안의 파일을 임포트할 때
# import 디렉토리명.파일명 => 다른 디렉토리의 파일을 임포트할 때

import test_dict.dict_sample as dict_sample
from mission.dict_mission1 import get_student_info
import mission.dict_mission2 as mission2

def main():
    dict_mission1 = get_student_info()
    print(f'{dict_mission1["grade"]}학년 {dict_mission1["s_class"]}반 {dict_mission1["s_no"]}번 {dict_mission1["name"]}의 점수는 {dict_mission1["score"]:.2f} 입니다.')
    # 여기에 프로젝트의 주요 기능을 추가하세요.

if __name__ == "__main__":
    # main()
    # mission2.dictfunc1()
    mission2.dictfunc2()
    # mission2.dictfunc3()
    # mission2.dictfunc4()
    # mission2.dictfunc5()
    # 임포트한 모듈 안의 함수 사용 시:
    # 임포트한 모듈명 그대로 사용: 모듈명.함수명()
    # test_dict.dict_sample.print_dictionary() # 모듈명에 줄임말이 지정되면 정식 모듈명 사용 못 함
    # dict_sample.test1()
    # dict_sample.test2()
    # dict_sample.test3()
    # dict_sample.test4()
    # dict_sample.test5()
