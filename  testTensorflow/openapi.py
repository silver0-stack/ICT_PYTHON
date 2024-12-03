import os
from dotenv import load_dotenv
import openai

# 환경 변수 로드 및 API 키 설정
if not load_dotenv():
    print(".env 파일을 찾지 못했습니다. API 키를 코드에 직접 설정합니다.")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("API 키를 설정해주세요.")

openai.api_key = OPENAI_API_KEY

def ask(question, message_history=[], model="gpt-3.5-turbo"):
    if len(message_history) == 0:
        message_history.append(
            {"role": "system", "content": "You are a helpful assistant. You must answer in Korean."}
        )

    message_history.append({"role": "user", "content": question})

    try:
        completion = openai.ChatCompletion.create(model=model, messages=message_history)
        assistant_reply = completion.choices[0].message.content
        message_history.append({"role": "assistant", "content": assistant_reply})
    except Exception as e:
        print(f"오류 발생: {e}")
        return message_history

    return message_history

# 대화 테스트
message_history = ask("대한민국의 수도는 어디인가요?", message_history=[])
print(message_history[-1])

message_history = ask("이전의 내용을 영어로 답변해 주세요", message_history=message_history)
print(message_history[-1])
