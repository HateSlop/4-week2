from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("MY_SECRET_KEY")

print(key)