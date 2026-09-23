# 🚗 AI Parking Advisor

AI Parking Advisor is a Python-based intelligent parking assistance application that evaluates parking suitability using Fuzzy Logic and provides practical parking recommendations using Google Gemini AI.

## 🌐 Live Demo

👉 https://gxdyaksha-parkingadvisor-app-c71ujy.streamlit.app/

## 📂 GitHub Repository

👉 https://github.com/gxdyaksha/ParkingAdvisor

## 📌 Project Overview

Finding a suitable parking space can be difficult when an area is crowded or the available space is limited.

AI Parking Advisor analyzes parking conditions using:

- Crowd Level
- Parking Space Size
- Parking Situation Description

The application uses Fuzzy Logic to calculate a Parking Suitability Score between 0 and 100.

Google Gemini AI is then used to provide practical parking advice based on the described situation.

## ✨ Features

- Crowd Level input
- Parking Space Size input
- Parking situation description
- Fuzzy Logic based suitability calculation
- Parking Suitability Score from 0 to 100
- Poor, Moderate, and Good suitability classification
- AI-powered parking advice using Google Gemini
- Fallback advice when Gemini is unavailable
- User input validation
- Interactive Streamlit web interface

## 🛠️ Technologies Used

- Python
- Streamlit
- NumPy
- Scikit-Fuzzy
- LangChain
- Google Gemini API
- python-dotenv

## 🧠 How It Works

The user provides three types of information:

1. Crowd Level
2. Parking Space Size
3. Parking Situation

The application first processes the Crowd Level and Parking Space Size using Fuzzy Logic.

The Fuzzy Logic system uses membership functions and predefined rules to calculate a Parking Suitability Score between 0 and 100.

The score is classified into three categories:

| Score | Classification |
|---|---|
| Below 40 | Poor Suitability |
| 40 to below 70 | Moderate Suitability |
| 70 and above | Good Suitability |

After calculating the suitability score, the parking situation description is sent to the Gemini AI component to generate practical parking advice.

## 🔬 Fuzzy Logic

The Fuzzy Logic system considers:

### Crowd Level

- Low
- Medium
- High

### Parking Space

- Small
- Medium
- Large

### Suitability

- Poor
- Moderate
- Good

The system combines these values through fuzzy rules and uses centroid defuzzification to produce the final numerical suitability score.

## 🤖 Gemini AI

Google Gemini is used to generate natural-language parking advice.

The AI considers the user's parking situation and provides recommendations such as:

- Looking for a larger parking space
- Checking surrounding vehicles
- Ensuring sufficient space for entering and exiting safely

If Gemini is unavailable, the application provides fallback parking advice.

## 📁 Project Structure

```text
ParkingAdvisor/
│
├── app.py
├── fuzzy_logic.py
├── gemini_advisor.py
├── test_fuzzy.py
├── test_gemini.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/