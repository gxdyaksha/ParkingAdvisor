import streamlit as st

from fuzzy_logic import calculate_parking_suitability
from gemini_advisor import get_parking_advice


st.set_page_config(
    page_title="AI Parking Advisor",
    page_icon="🚗"
)

st.title("🚗 AI Parking Advisor")

st.write(
    "Welcome to the Parking Difficulty & Suitability Advisor."
)


# -----------------------------
# Parking Conditions
# -----------------------------

st.header("📊 Parking Conditions")

crowd_level = st.slider(
    "Crowd Level",
    0,
    10,
    5
)

parking_space = st.slider(
    "Parking Space Size",
    0,
    10,
    5
)


# -----------------------------
# Parking Situation
# -----------------------------

st.header("📝 Parking Situation")

situation = st.text_area(
    "Describe your parking situation:",
    placeholder="Example: The parking area is crowded and the space is small."
)


# -----------------------------
# Analyze Parking
# -----------------------------

if st.button("🔍 Analyze Parking"):

    if situation.strip():

        # Calculate suitability
        score = calculate_parking_suitability(
            crowd_level,
            parking_space
        )

        # -----------------------------
        # Score
        # -----------------------------

        st.header("📈 Parking Suitability Score")

        st.metric(
            "Suitability",
            f"{score}/100"
        )

        st.progress(int(score))

        # -----------------------------
        # Result
        # -----------------------------

        if score < 40:

            st.error("❌ Poor Suitability")

            result_message = (
                "This parking space may be difficult or risky to use."
            )

        elif score < 70:

            st.warning("⚠️ Moderate Suitability")

            result_message = (
                "This parking space can be used, but extra caution is recommended."
            )

        else:

            st.success("✅ Good Suitability")

            result_message = (
                "This parking space appears suitable for parking."
            )

        st.write(result_message)


        # -----------------------------
        # Input Summary
        # -----------------------------

        st.header("📋 Parking Analysis")

        st.write(f"**Crowd Level:** {crowd_level}/10")
        st.write(f"**Parking Space Size:** {parking_space}/10")
        st.write(f"**Suitability Score:** {score}/100")


        # -----------------------------
        # AI Advice
        # -----------------------------

        st.header("🤖 Parking Advice")

        try:

            advice = get_parking_advice(
                situation,
                crowd_level,
                parking_space,
                score
            )

            if isinstance(advice, list):

                for item in advice:

                    if isinstance(item, dict):
                        st.write(item.get("text", ""))
                    else:
                        st.write(item)

            else:
                st.write(advice)

        except Exception:

            if score < 40:

                st.info(
                    "AI advice is temporarily unavailable. "
                    "Based on the score, consider finding a larger "
                    "or less crowded parking space."
                )

            elif score < 70:

                st.info(
                    "AI advice is temporarily unavailable. "
                    "The space can be used, but park carefully "
                    "and check the surrounding clearance."
                )

            else:

                st.info(
                    "AI advice is temporarily unavailable. "
                    "Based on the suitability score, this space "
                    "appears suitable for parking."
                )

    else:

        st.warning(
            "Please describe your parking situation."
        )