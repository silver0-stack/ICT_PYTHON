# voice_modulation_model.py
import torch
import torchaudio
from torchvision import models, transforms


class VoiceModulationDetector:
    def __init__(self, model_path):
        # 사전 학습된 ResNet 모델 로드
        self.model = models.resnet18(pretrained=True)
        self.model.fc = torch.nn.Linear(self.model.fc.in_features, 2)  # 이진 분류
        self.model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
        self.model.eval()

        # 전처리 변환 정의
        self.transform = transforms.Compose([
            torchaudio.transforms.Resample(orig_freq=16000, new_freq=16000),
            torchaudio.transforms.MelSpectrogram(),
            transforms.ToTensor(),
        ])

    def detect_modulation(self, file_path):
        waveform, sample_rate = torchaudio.load(file_path)
        spectrogram = self.transform(waveform)
        spectrogram = spectrogram.unsqueeze(0)  # 배치 차원 추가

        with torch.no_grad():
            output = self.model(spectrogram)
            _, predicted = torch.max(output, 1)

        return '변조됨' if predicted.item() == 1 else '원본'
