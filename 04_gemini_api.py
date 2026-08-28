# API --> Application Programming Interface 

from dotenv import load_dotenv 
import os 
from google import genai 

# .env file load krna
load_dotenv()

# api key lo
api_key = os.getenv("GEMINI_API")

# client bnao
client = genai.Client(api_key=api_key)

# swaal pucho
response = client.models.generate_content(
    model = "gemini-3.6-flash",
    contents = "python kya hai? 3 line mei explain karo"
)

print(response.text)