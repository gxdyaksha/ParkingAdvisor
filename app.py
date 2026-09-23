import streamlit as st

from fuzzy_logic import calculate_parking_suitability
from gemini_advisor import get_parking_advice


st.set_page_config(
    page_title="AI Parking Advisor",
    page_icon="🚗",
    layout="centered"
)


# -----------------------------
# Header
# -----------------------------

st.title("🚗 AI Parking Advisor")

st.write(
    "Welcome to the Parking Difficulty & Suitability Advisor."
)

st.divider()


# -----------------------------
# Parking Conditions
# -----------------------------

st.header("📊 Parking Conditions")

crowd_level = st.slider(
    "Crowd Level",
    min_value=0,
    max_value=10,
    value=5,
    help="0 = Very Low Crowd, 10 = Extremely Crowded"
)

parking_space = st.slider(
    "Parking Space Size",
    min_value=0,
    max_value=10,
    value=5,
    help="0 = Very Small, 10 = Very Large"
)


# -----------------------------
# Parking Situation
# -----------------------------

st.header("📝 Parking Situation")

situation = st.text_area(
    "Describe your parking situation:",
    placeholder=(
        "Example: The parking area is crowded and "
        "the parking space is small."
    ),
    height=120
)


# -----------------------------
# Analyze Parking
# -----------------------------

if st.button("🔍 Analyze Parking", use_container_width=True):

    if situation.strip():

        # Calculate fuzzy suitability score
        score = calculate_parking_suitability(
            crowd_level,
            parking_space
        )

        # -----------------------------
        # Score
        # -----------------------------

        st.divider()

        st.header("📈 Parking Suitability Score")

        st.metric(
            "Suitability",
            f"{score}/100"
        )

        st.progress(
            min(max(int(score), 0), 100)
        )


        # -----------------------------
        # Suitability Result
        # -----------------------------

        if score < 40:

            st.error("❌ Poor Suitability")

            result_message = (
                "This parking space may be difficult or risky to use."
            )

        elif score < 70:

            st.warning("⚠️ Moderate Suitability")

            result_message = (
                "This parking space can be used, "
                "but extra caution is recommended."
            )

        else:

            st.success("✅ Good Suitability")

            result_message = (
                "This parking space appears suitable for parking."
            )

        st.write(result_message)


        # -----------------------------
        # Parking Analysis
        # -----------------------------

        st.divider()

        st.header("📋 Parking Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Crowd Level",
                f"{crowd_level}/10"
            )

        with col2:
            st.metric(
                "Parking Space",
                f"{parking_space}/10"
            )

        st.write(
            f"**Suitability Score:** {score}/100"
        )


        # -----------------------------
        # AI Parking Advice
        # -----------------------------

        st.divider()

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
                        text = item.get("text", "")

                        if text:
                            st.write(text)

                    else:
                        st.write(item)

            else:

                st.write(advice)

        except Exception:

            if score < 40:

                st.info(
                    "AI advice is temporarily unavailable. "
                    "Based on the score, consider finding a "
                    "larger or less crowded parking space."
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