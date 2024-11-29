import os # 운영 체제 관련 작업(디렉토리 생성, 파일 목록 가져오기 등)을 위한 모듈
import random # 랜덤 샘플링(데이터 셔플링)에 필요한 모듈
from shutil import copyfile # 파일 복사에 필요한 모듈

# 원본 데이터 디렉토리
data_dir = "./catdog/PetImages" # 고양이와 강아지 이미지가 저장된 디렉토리
cat_dir = os.path.join(data_dir, "Cat") # 고양이 이미지 폴더 경로
dog_dir = os.path.join(data_dir, "Dog") # 강아지 이미지 폴더 경로

# 데이터 분리 후 저장할 새로운 디렉토리 생성
base_dir = "./catdog_split" # 학습, 검증, 테스트 데이터를 저장할 기본 경로
train_dir = os.path.join(base_dir, "train") # 학습 데이터 저장 경로
val_dir = os.path.join(base_dir, "validation") # 검증 데이터 저장 경로
test_dir = os.path.join(base_dir, "test") # 테스트 데이터 저장 경로

# 학습, 검증, 테스트 디렉토리에 'cats'와 'dogs' 하위 폴더 생성
for folder in [train_dir, val_dir, test_dir]:
    os.makedirs(os.path.join(folder, "cats"), exist_ok=True) # 'cats' 폴더 생성
    os.makedirs(os.path.join(folder, "dogs"), exist_ok=True) # 'dogs' 폴더 생성

# 데이터 분배 함수
def split_data(src_dir, train_dir, val_dir, test_dir, split_ratio=(0.7, 0.15, 0.15)):
    files = os.listdir(src_dir)
    random.shuffle(files)
    train_split = int(len(files) * split_ratio[0])
    val_split = train_split + int(len(files) * split_ratio[1])

    train_files = files[:train_split]
    val_files = files[train_split:val_split]
    test_files = files[val_split:]

    # 파일 복사
    for file in train_files:
        copyfile(os.path.join(src_dir, file), os.path.join(train_dir, file))
    for file in val_files:
        copyfile(os.path.join(src_dir, file), os.path.join(val_dir, file))
    for file in test_files:
        copyfile(os.path.join(src_dir, file), os.path.join(test_dir, file))

# 데이터 분리 실행
split_data(cat_dir, f"{train_dir}/cats", f"{val_dir}/cats", f"{test_dir}/cats")
split_data(dog_dir, f"{train_dir}/dogs", f"{val_dir}/dogs", f"{test_dir}/dogs")

print("데이터 분리가 완료되었습니다!")
print("훈련 데이터:", len(os.listdir(f"{train_dir}/cats")), "고양이, ", len(os.listdir(f"{train_dir}/dogs")), "강아지")
print("검증 데이터:", len(os.listdir(f"{val_dir}/cats")), "고양이, ", len(os.listdir(f"{val_dir}/dogs")), "강아지")
print("테스트 데이터:", len(os.listdir(f"{test_dir}/cats")), "고양이, ", len(os.listdir(f"{test_dir}/dogs")), "강아지")
