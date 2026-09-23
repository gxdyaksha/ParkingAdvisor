\# 🚗 AI Parking Advisor



AI Parking Advisor is a Python-based application that evaluates parking suitability using Fuzzy Logic and provides practical parking advice.



\## Features



\- Crowd Level input

\- Parking Space Size input

\- Parking situation description

\- Fuzzy Logic based suitability score

\- Poor, Moderate, and Good suitability classification

\- AI-powered parking advice using Gemini

\- Fallback advice when Gemini is unavailable

\- Streamlit web interface



\## Technologies Used



\- Python

\- Streamlit

\- NumPy

\- Scikit-Fuzzy

\- LangChain

\- Google Gemini API

\- python-dotenv



\## How It Works



The user provides:



1\. Crowd Level

2\. Parking Space Size

3\. Parking Situation



The application uses Fuzzy Logic to calculate a Parking Suitability Score between 0 and 100.



The score is classified as:



\- Below 40: Poor Suitability

\- 40 to below 70: Moderate Suitability

\- 70 and above: Good Suitability



The application then generates practical parking advice based on the parking conditions.



\## Project Structure



```text

ParkingAdvisor/

│

├── app.py

├── fuzzy\_logic.py

├── gemini\_advisor.py

├── test\_fuzzy.py

├── test\_gemini.py

├── .env

├── .gitignore

└── venv/

