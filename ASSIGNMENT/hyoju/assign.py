from dotenv import load_dotenv
import os

# .env 파일 활성화
load_dotenv()

# .env 파일에서 MY_SECRET_KEY 값 가져오기
key = os.getenv("MY_SECRET_KEY")
print(key)