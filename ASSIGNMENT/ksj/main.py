from dotenv import load_dotenv
from pathlib import Path
import os


load_dotenv()

key = os.getenv("MY_SECRET_KEY")
print(key)