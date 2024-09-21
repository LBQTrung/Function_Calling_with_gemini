import os
import dotenv
import google.generativeai as genai
from function_calling import CONTEXT_PROMPT
dotenv.load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro"
)

chat = model.start_chat(
    history=[
        {"role": "user", "parts": CONTEXT_PROMPT
        },
        {"role": "model", "parts": "OK. What do you want?"},
    ]
)