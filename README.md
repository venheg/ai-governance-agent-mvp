# AI Governance Agent — Phase 2

## Setup
1. Create a Gemini API key in Google AI Studio: https://aistudio.google.com/
2. Install Python 3.11+ and run `pip install -r requirements.txt`.
3. Create `.streamlit/secrets.toml` containing:

   GEMINI_API_KEY = "YOUR_API_KEY"
   GEMINI_MODEL = "gemini-2.5-flash-lite"

4. Run `streamlit run app.py`.

For Streamlit Community Cloud, add the same TOML entries under the app's
Secrets settings. Never commit `secrets.toml` or put API keys in source code.
Docs: https://docs.streamlit.io/develop/concepts/connections/secrets-management

Check current model availability, quotas, pricing and data terms:
https://ai.google.dev/gemini-api/docs/pricing

Use synthetic data only. The Gemini API free tier may use submitted content
to improve Google's products. Do not submit personal, confidential, sensitive,
regulated or restricted organisational information.

This prototype provides preliminary observations only. It does not provide
legal advice, certify compliance or approve AI deployment.

## Test
Open Governance Agent, select the sample Customer Support Assistant, and ask:
"Help me assess this AI use case. Ask for missing information one question
at a time." Answer using fictional details, then click "Prepare preliminary
governance assessment".

## Known limitations
Session data is temporary. Document processing, policy-grounded RAG, validated
risk scoring, PDF export, persistent storage, production authentication and
tamper-resistant audit trails are not included yet.
