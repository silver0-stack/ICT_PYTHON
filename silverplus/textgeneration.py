import openai
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, send_file
from pathlib import Path
from gtts import gTTS
from flask_cors import CORS
import jwt
from functools import wraps
import requests
import uuid
from datetime import datetime, timezone
import logging
import base64


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}}, allow_headers=["Authorization", "Content-Type"])

# 로깅 설정
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# .env 파일에서 환경 변수 로드
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
SPRING_BOOT_API_URL = os.getenv("SPRING_BOOT_API_URL")


# textgeneration.py


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            log.debug(f"Authorization Header: {auth_header}")  # 헤더 로그 추가
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]
        else:
            log.debug("Authorization header not found")  # 헤더 없음 로그 추가
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            # Base64로 인코딩된 SECRET_KEY를 디코딩
            decoded_secret_key = base64.b64decode(SECRET_KEY)
            data = jwt.decode(token, decoded_secret_key, algorithms=["HS256"])
            current_user = data['sub']  # 'sub' 키에서 사용자 UUID 추출
            log.debug(f"Current User: {current_user}")  # 사용자 로그 추가
        except Exception as e:
            log.error(f"Token decoding error: {str(e)}")
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated






# Flask애서 JWT 토큰을 디코딩할 때, current_user 객체에 id 속성이 포함되어 있다고 가정했다.
# Chat Completion 엔드포인트
# Flask 애플리케이션 코드 수정
@app.route("/chat", methods=["POST"])
@token_required
def chat(current_user):
    # 사용자로부터 받은 JWT 토큰 추출
    auth_header = request.headers.get('Authorization', '')
    token = auth_header.split(' ')[1] if 'Bearer ' in auth_header else None

    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided."}), 400

    # conversationId를 사용자 UUID로 고정
    conversation_id = current_user

    # 사용자 메시지 ID 생성 (UUID 문자열로 변환)
    user_msg_id = str(uuid.uuid4())

    # 현재 시각 (UTC, timezone-aware 객체)
    sent_at = datetime.now(timezone.utc).isoformat()

    # 사용자 메시지 데이터 생성
    user_chat_data = {
        "msgId": user_msg_id,
        "msgSenderRole": "USER",
        "msgContent": user_message,
        "msgSentAt": sent_at,
        "msgSenderUUID": current_user,  # JWT에서 추출한 사용자 UUID
        "parentMsgId": None,
        "msgType": "T",  # 메시지 타입 추가 (T for text)
        "msgWorkspaceId": "111"
    }

    # Authorization 헤더에 토큰 포함
    headers = {}
    if token:
        headers['Authorization'] = f'Bearer {token}'

    # Spring Boot API를 통해 사용자 메시지 저장
    try:
        response_user = requests.post(
            f"{SPRING_BOOT_API_URL}/api/chat/save",
            json=user_chat_data,
            headers=headers  # 토큰 포함
        )
        if response_user.status_code != 201:
            log.error(f"Failed to save user message: {response_user.text}")
            return jsonify({"error": "Failed to save user message."}), 500
    except Exception as e:
        log.error(f"Exception when saving user message: {str(e)}")
        return jsonify({"error": f"Exception when saving user message: {str(e)}"}), 500

    # OpenAI Chat Completion API를 통해 응답 생성
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system",
                 "content": "You are a helpful assistant designed to have friendly and patient conversations with elderly users."},
                {"role": "user", "content": user_message}
            ]
        )
        ai_reply = response.choices[0].message["content"].strip()
    except Exception as e:
        log.error(f"Exception when calling OpenAI:  {str(e)}")
        return jsonify({"error": f"Exception when calling OpenAI: {str(e)}"}), 500

    # AI 메시지 데이터 생성 (UUID 문자열로 변환)
    assistant_msg_id = str(uuid.uuid4())

    # AI 응답 시각 (UTC, timezone-aware 객체)
    reply_sent_at = datetime.now(timezone.utc).isoformat()

    # AI 응답 데이터 생성
    assistant_chat_data = {
        "msgId": assistant_msg_id,
        "msgSenderRole": "AI",
        "msgContent": ai_reply,
        "msgSentAt": reply_sent_at,
        "msgSenderUUID": "ai-uuid-1234-5678-90ab-cdef12345678",  # 어시스턴트의 UUID로 설정
        "parentMsgId": user_msg_id,
        "msgType": "T",  # 메시지 타입 추가 (T for text)
        "msgWorkspaceId": "111"
    }

    # Spring Boot API를 통해 AI 응답 저장
    try:
        response_assistant = requests.post(
            f"{SPRING_BOOT_API_URL}/api/chat/save",
            json=assistant_chat_data,
            headers=headers  # 토큰 포함
        )
        if response_assistant.status_code != 201:
            log.error(f"Failed to save AI message: {response_assistant.text}")
            return jsonify({"error": "Failed to save AI message."}), 500
    except Exception as e:
        log.error(f"Exception when saving assistant message: {str(e)}")
        return jsonify({"error": f"Exception when saving assistant message: {str(e)}"}), 500

    return jsonify({"reply": ai_reply})



# TTS 음성 변환 엔드포인트
@app.route("/speak", methods=["POST"])
def speak():
    text = request.json.get("text")
    tts = gTTS(text=text, lang="ko", slow=False)
    speech_file_path = Path("speech.mp3")
    tts.save(speech_file_path)
    return send_file(speech_file_path, mimetype="audio/mpeg")


# STT 변환 엔드포인트 (옵션)
@app.route("/transcribe", methods=["POST"])
def transcribe():
    audio_file = request.files["file"]
    audio_path = Path("uploaded_audio.mp3")
    audio_file.save(audio_path)

    with open(audio_path, "rb") as f:
        transcription = openai.Audio.transcriptions.create(
            model="whisper-1",
            file=f
        )

    return jsonify({"transcription": transcription["text"]})


if __name__ == "__main__":
    app.run(debug=True, port=5000)  # 포트 번호 변경 가능
