import os
from dotenv import load_dotenv

load_dotenv(override=True)

s = os.environ.get('secret')
print(s)