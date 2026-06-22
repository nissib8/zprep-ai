import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_questions(resume_text):
    prompt = f"""
    Based on this resume:

    {resume_text}

    Generate:

    5 HR Questions
    5 Technical Questions
    5 Project Questions

    Return the output in HTML format using:

    <h2> section titles
    <ul>
    <li>questions</li>
    </ul>

    Do not use markdown.
    """

    response = model.generate_content(prompt)
    return response.text