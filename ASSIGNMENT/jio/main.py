import os
from dotenv import load_dotenv
from openai import OpenAI

# .env 로드
load_dotenv()

# 환경변수에서 API 키 가져오기
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-4o-mini",
    input="오늘 저녁에 뭐 먹었을까?"
)

print(response.output_text)
print(response)