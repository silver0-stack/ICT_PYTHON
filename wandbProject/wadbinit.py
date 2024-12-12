import wandb
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np

# wandb 프로젝트 설정
wandb.init(project="my-pytorch-project")

# 하이퍼파라미터 설정
config = wandb.config
config.learning_rate = 0.001
config.batch_size = 64
config.epochs = 10

# 데이터셋 생성
x = np.random.rand(1000, 20)
y = np.random.randint(0, 2, size=(1000, 1))

dataset = TensorDataset(torch.tensor(x, dtype=torch.float32), torch.tensor(y, dtype=torch.float32))
dataloader = DataLoader(dataset, batch_size=config.batch_size, shuffle=True)


# 간단한 모델 정의
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(20, 50)
        self.fc2 = nn.Linear(50, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x


model = SimpleNet()
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=config.learning_rate)

# 모델 학습
for epoch in range(config.epochs):
    for batch_x, batch_y in dataloader:
        optimizer.zero_grad()
        outputs = model(batch_x)
        loss = criterion(outputs, batch_y)
        loss.backward()
        optimizer.step()

    # 매 에포크마다 wandb에 메트릭 기록
    wandb.log({"epoch": epoch, "loss": loss.item()})

# wandb run 종료
wandb.finish()
