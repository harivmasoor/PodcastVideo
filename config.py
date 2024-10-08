import os
from dotenv import load_dotenv
import google.generativeai as genai


# Load .env file explicitly
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# Get the API key, with a fallback to None
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the .env file")



# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-pro-latest')

print(f"Using Gemini API Key: {GEMINI_API_KEY[:5]}...{GEMINI_API_KEY[-5:]}")



