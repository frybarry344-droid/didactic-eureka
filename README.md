# didactic-eureka

Streamlit app: Business Comeback Story Generator

How to run locally:

1. Create a virtual environment (recommended):
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate     # Windows PowerShell

2. Install dependencies:
   pip install -r requirements.txt

3. Run the app:
   streamlit run app.py

Deploy to Streamlit Community Cloud:

1. Push the repository to GitHub.
2. On https://share.streamlit.io click "New app", point it to this repository, select the branch and the main file `app.py`, then deploy.

Notes:
- The app currently imports only `streamlit`. If you add other dependencies, include them in `requirements.txt`.
- If you want a specific Python version included with the push (e.g., 3.11), tell me and I can add a runtime.txt or other config.