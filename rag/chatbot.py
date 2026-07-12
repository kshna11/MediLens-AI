import os
from dotenv import load_dotenv
from google import genai

from rag.vector_store import load_vector_store

# Load environment variables
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_question(question):

    # Load FAISS database
    db = load_vector_store()

    # Retrieve relevant chunks
    docs = db.similarity_search(
        question,
        k=5
    )

    # Merge retrieved text
    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
You are MediLens AI, an AI Healthcare Assistant.

You have two sources of information:

1. Uploaded medical report (highest priority)
2. Your medical knowledge

Rules:

- Analyze the uploaded report first.
- Use report findings whenever available.
- If the user asks about lifestyle, diet, exercise, precautions, disease explanation, or medicines, combine the report findings with your medical knowledge.
- Never invent lab values.
- Keep answers concise (100–150 words).
- Use simple language suitable for non-medical users.

Return every response in the following format:

## 📋 Report Findings

| Test | Result | Status |
|------|--------|--------|
| Example | 4.5 mmol/L | 🟢 Normal |

(Only include relevant values related to the user's question.)

## 🩺 Explanation

Explain the findings in 2–3 short sentences.

## 💡 Recommendations

- Give 3–5 personalized recommendations.
- If the report does not contain enough information, provide general medical advice.

## ⚠ Medical Disclaimer

This information is AI-generated and should not replace consultation with a qualified healthcare professional.

Uploaded Medical Report:

{context}

User Question:

{question}
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