import os
from dotenv import load_dotenv
from google import genai

# Load API Key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_summary(report_text):

    prompt = f"""
    You are MediLens AI, an expert AI healthcare assistant.

    Analyze the uploaded medical report carefully.

    Your response must be:
    - Professional
    - Short and concise
    - Easy for non-medical users to understand
    - Written in Markdown
    - Maximum 250 words

    Never invent laboratory values.
    Use only the information present in the report.

    If some information is missing, do not guess.

    Return the response EXACTLY in the following format.

    # 📋 Key Findings

    - Mention the most important findings.
    - Highlight only abnormal or significant values.
    - If everything appears normal, mention that.

    ---

    # 🩺 Medical Explanation

    Explain what the findings mean in simple language.

    Maximum 3-4 short sentences.

    ---

    # 💡 Recommendations

    Provide 4-6 personalized recommendations based on the report.

    Examples:
    - Diet
    - Exercise
    - Lifestyle
    - Hydration
    - Follow-up tests
    - Doctor consultation

    If the report looks normal,
    suggest healthy lifestyle recommendations.

    ---

    # ⚠ Disclaimer

    This AI-generated summary is for informational purposes only and should not replace consultation with a qualified healthcare professional.

    Medical Report:

    {report_text}
    """

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return response.text

    except Exception:

        return """
    ⚠️ **AI Service Unavailable**

    The AI service is currently unavailable.

    This may happen because:

    - Daily Gemini API quota has been reached.
    - Temporary network issue.

    Please try again later.
    """