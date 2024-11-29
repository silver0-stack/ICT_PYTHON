import os  # 운영 체제 관련 작업(디렉토리 생성, 파일 목록 가져오기 등)을 위한 모듈
import random  # 랜덤 샘플링(데이터 셔플링)에 필요한 모듈
from shutil import copyfile  # 파일 복사에 필요한 모듈

# 원본 데이터 디렉토리
data_dir = "./catdog/PetImages"  # 고양이와 강아지 이미지가 저장된 디렉토리
cat_dir = os.path.join(data_dir, "Cat")  # 고양이 이미지 폴더 경로
dog_dir = os.path.join(data_dir, "Dog")  # 강아지 이미지 폴더 경로

# 데이터 분리 후 저장할 새로운 디렉토리 생성
base_dir = "./catdog_split"  # 학습, 검증, 테스트 데이터를 저장할 기본 경로
train_dir = os.path.join(base_dir, "train")  # 학습 데이터 저장 경로
val_dir = os.path.join(base_dir, "validation")  # 검증 데이터 저장 경로
test_dir = os.path.join(base_dir, "test")  # 테스트 데이터 저장 경로

# 학습, 검증, 테스트 디렉토리에 'cats'와 'dogs' 하위 폴더 생성
for folder in [train_dir, val_dir, test_dir]:
    os.makedirs(os.path.join(folder, "cats"), exist_ok=True)  # 'cats' 폴더 생성
    os.makedirs(os.path.join(folder, "dogs"), exist_ok=True)  # 'dogs' 폴더 생성


# 데이터 분배 함수 정의
def split_data(src_dir, train_dir, val_dir, test_dir, split_ratio=(0.7, 0.15, 0.15)):
    """
    데이터를 학습(train), 검증(validation), 테스트(test) 데이터로 분리하는 함수
    :param src_dir: 원본 이미지가 저장된 디렉터리
    :param train_dir: 학습 데이터 저장 디렉토리
    :param val_dir: 검증 데이터 저장 디렉토리
    :param test_dir: 테스트 데이터 저장 디렉토리
    :param split_ratio: 데이터를 학습/검증/테스트로 나눌 비율 (기본값: 70%, 15%, 15%)
    :return:
    """
    files = os.listdir(src_dir)  # 원본 디렉토리(src_dir)에 있는 파일 목록 가져오기
    random.shuffle(files)  # 파일 순서를 랜덤으로 섞음
    train_split = int(len(files) * split_ratio[0])  # 학습 데이터의 개수 계산
    val_split = train_split + int(len(files) * split_ratio[1])  # 검증 데이터의 끝 인덱스 계산

    train_files = files[:train_split]  # 학습 데이터 파일 리스트
    val_files = files[train_split:val_split]  # 검증 데이터 파일 리스트
    test_files = files[val_split:]  # 테스트 데이터 파일 리스트: 배고파배고파배고팡ㄹ123456

    # 학습 데이터 파일 복사
    for file in train_files:
        copyfile(os.path.join(src_dir, file), os.path.join(train_dir, file))
    #  검증 데이터 파일 복사
    for file in val_files:
        copyfile(os.path.join(src_dir, file), os.path.join(val_dir, file))
    #  테스트 데이터 파일 복사
    for file in test_files:
        copyfile(os.path.join(src_dir, file), os.path.join(test_dir, file))


# 데이터 분리 실행
split_data(cat_dir, f"{train_dir}/cats", f"{val_dir}/cats", f"{test_dir}/cats") # 고양이 데이터 분리
split_data(dog_dir, f"{train_dir}/dogs", f"{val_dir}/dogs", f"{test_dir}/dogs") # 강아지 데이터 분리

# 데이터 분리 결과 출력
print("데이터 분리가 완료되었습니다!")
print("훈련 데이터:", len(os.listdir(f"{train_dir}/cats")), "고양이, ", len(os.listdir(f"{train_dir}/dogs")), "강아지")
print("검증 데이터:", len(os.listdir(f"{val_dir}/cats")), "고양이, ", len(os.listdir(f"{val_dir}/dogs")), "강아지")
print("테스트 데이터:", len(os.listdir(f"{test_dir}/cats")), "고양이, ", len(os.listdir(f"{test_dir}/dogs")), "강아지")
