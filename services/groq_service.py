
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()



client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


client = Groq(
    api_key=api_key,
    timeout=60.0,
    max_retries=3
)
