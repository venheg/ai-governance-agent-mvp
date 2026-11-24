# AI Governance Agent — MVP Starter

This is the first, beginner-friendly application shell for the AI Governance Agent.

## What is included

- Dashboard
- AI use-case registration
- Assessment inventory
- Basic submit-for-review workflow
- Human review placeholder

The first version uses Streamlit session state. This means records are temporary and may reset when the app restarts.

## Safety

Use fictional demonstration data only. Do not enter personal, confidential, regulated, or organisationally sensitive information.

This prototype does not provide legal advice, certify compliance, or approve AI systems for deployment.

## Option 1 — Run locally on your computer

1. Install Python 3.11 or newer.
2. Extract this ZIP file.
3. Open a terminal in the extracted folder.
4. Create a virtual environment:

   Windows:
   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   ```

   macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

5. Install packages:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the app:

   ```bash
   streamlit run app.py
   ```

7. Open the local URL shown in the terminal (usually http://localhost:8501).

## Option 2 — Deploy with Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload `app.py` and `requirements.txt` to the repository.
3. Sign in to Streamlit Community Cloud using GitHub.
4. Create an app and select your repository.
5. Set the main file path to `app.py`.
6. Deploy.

See the official Streamlit Community Cloud documentation:
https://docs.streamlit.io/deploy/streamlit-community-cloud

## Next development steps

1. Add persistent storage with SQLite.
2. Add Gemini API integration using Streamlit secrets.
3. Add document upload and extraction.
4. Add governance policy retrieval (RAG).
5. Add evidence-based risk and control assessment.
6. Generate an assessment report.
7. Expand reviewer workflow and audit history.

Never put an API key directly in `app.py` or commit it to GitHub.
