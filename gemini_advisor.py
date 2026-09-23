import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key
)


def get_parking_advice(
    situation,
    crowd_level,
    parking_space,
    score
):

    prompt = f"""
You are an AI Parking Suitability Advisor.

Analyze the following parking information:

Crowd Level: {crowd_level}/10
Parking Space Size: {parking_space}/10
Suitability Score: {score}/100

Parking Situation:
{situation}

Give short, practical parking advice.

Your answer should:
1. Give a clear recommendation.
2. Explain the main reason.
3. Give 2 or 3 practical parking tips.

Do not mention that you are an AI.
"""

    try:

        response = llm.invoke(prompt)

        return response.content

    except Exception:

        if score < 40:

            return """
**Recommendation: Avoid this parking space if possible.**

The space has low suitability because the parking conditions may make
maneuvering and exiting difficult.

**Tips:**
1. Look for a larger parking space.
2. Check the surrounding vehicles before parking.
3. Make sure there is enough room to open the doors and exit safely.
"""

        elif score < 70:

            return """
**Recommendation: Park with caution.**

The parking space has moderate suitability, so check the surrounding
area before parking.

**Tips:**
1. Check the available space carefully.
2. Keep enough clearance from nearby vehicles.
3. Make sure you have a safe exit route.
"""

        else:

            return """
**Recommendation: This parking space appears suitable.**

The parking conditions and available space indicate that parking should
be relatively comfortable.

**Tips:**
1. Park centrally within the marked space.
2. Check surrounding vehicles before opening the doors.
3. Keep the exit path clear.
"""