import streamlit as st
from datetime import date
import pandas as pd

st.set_page_config(
    page_title="AI Governance Agent",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Session state (temporary MVP data)
# -----------------------------
if "use_cases" not in st.session_state:
    st.session_state.use_cases = [
        {
            "id": "AIG-001",
            "name": "Customer Support Assistant",
            "business_unit": "Customer Operations",
            "owner": "Alex Morgan",
            "purpose": "Answer routine customer questions and route complex cases.",
            "model_provider": "Example AI Provider",
            "data_types": "Names, contact details, support conversations",
            "deployment": "Proposed",
            "status": "Draft",
            "created": str(date.today()),
        }
    ]

if "review_notes" not in st.session_state:
    st.session_state.review_notes = {}

# -----------------------------
# Sidebar navigation
# -----------------------------
st.sidebar.title("🛡️ AI Governance Agent")
st.sidebar.caption("MVP • Demonstration environment")
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Register AI use case", "Assessment inventory", "Human review", "About the MVP"],
)

st.sidebar.divider()
st.sidebar.caption("Prototype notice")
st.sidebar.info(
    "This first version stores demonstration records in session memory. "
    "Records may reset when the app restarts. Do not enter confidential or personal data."
)

# -----------------------------
# Dashboard
# -----------------------------
if page == "Dashboard":
    st.title("AI Governance Dashboard")
    st.write("A central workspace to register AI use cases and prepare them for governance assessment.")

    total = len(st.session_state.use_cases)
    drafts = sum(1 for x in st.session_state.use_cases if x["status"] == "Draft")
    submitted = sum(1 for x in st.session_state.use_cases if x["status"] == "Submitted")
    reviewed = sum(1 for x in st.session_state.use_cases if x["status"] == "Reviewed")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Registered use cases", total)
    c2.metric("Drafts", drafts)
    c3.metric("Awaiting review", submitted)
    c4.metric("Reviewed", reviewed)

    st.subheader("Recent AI use cases")
    if st.session_state.use_cases:
        df = pd.DataFrame(st.session_state.use_cases)
        st.dataframe(
            df[["id", "name", "business_unit", "owner", "deployment", "status"]],
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No AI use cases registered yet. Select 'Register AI use case' to begin.")

    st.subheader("MVP workflow")
    cols = st.columns(5)
    steps = [
        ("1", "Register", "Capture the AI use case"),
        ("2", "Assess", "Collect information and evidence"),
        ("3", "Evaluate", "Identify risks and control gaps"),
        ("4", "Report", "Prepare the assessment report"),
        ("5", "Review", "Human governance review"),
    ]
    for col, (number, title, description) in zip(cols, steps):
        with col:
            st.markdown(f"### {number}. {title}")
            st.caption(description)

# -----------------------------
# Register use case
# -----------------------------
elif page == "Register AI use case":
    st.title("Register a new AI use case")
    st.write("Enter fictional demonstration information for the first prototype.")

    with st.form("use_case_form"):
        name = st.text_input("AI application name *", placeholder="e.g. Customer Support Assistant")
        purpose = st.text_area("Business purpose *", placeholder="What will the AI application do?")
        business_unit = st.text_input("Business function *", placeholder="e.g. Customer Operations")
        owner = st.text_input("Business owner *", placeholder="Name or role")
        technical_owner = st.text_input("Technical owner", placeholder="Name or role")
        model_provider = st.text_input("AI model / provider", placeholder="e.g. Example AI Provider")
        data_types = st.text_area(
            "Types of data processed",
            placeholder="e.g. Customer contact details, support conversations",
        )
        deployment = st.selectbox(
            "Deployment stage",
            ["Proposed", "Proof of concept", "Pilot", "Production"],
        )
        submitted = st.form_submit_button("Save AI use case", type="primary")

    if submitted:
        if not name.strip() or not purpose.strip() or not business_unit.strip() or not owner.strip():
            st.error("Please complete all fields marked with an asterisk (*).")
        else:
            next_number = len(st.session_state.use_cases) + 1
            record = {
                "id": f"AIG-{next_number:03d}",
                "name": name.strip(),
                "business_unit": business_unit.strip(),
                "owner": owner.strip(),
                "technical_owner": technical_owner.strip(),
                "purpose": purpose.strip(),
                "model_provider": model_provider.strip(),
                "data_types": data_types.strip(),
                "deployment": deployment,
                "status": "Draft",
                "created": str(date.today()),
            }
            st.session_state.use_cases.append(record)
            st.success(f"Use case {record['id']} has been registered.")
            st.info("Next development step: connect this record to the Gemini-powered assessment workflow.")

# -----------------------------
# Inventory
# -----------------------------
elif page == "Assessment inventory":
    st.title("AI use-case inventory")
    st.write("View the use cases registered in this prototype.")

    if not st.session_state.use_cases:
        st.info("No records available.")
    else:
        for item in st.session_state.use_cases:
            with st.expander(f"{item['id']} — {item['name']} ({item['status']})"):
                st.write(f"**Business function:** {item['business_unit']}")
                st.write(f"**Business owner:** {item['owner']}")
                st.write(f"**Purpose:** {item['purpose']}")
                st.write(f"**AI model/provider:** {item.get('model_provider', 'Not provided')}")
                st.write(f"**Data types:** {item.get('data_types', 'Not provided')}")
                st.write(f"**Deployment stage:** {item['deployment']}")
                st.write(f"**Created:** {item['created']}")

                if item["status"] == "Draft":
                    if st.button("Submit for human review", key=f"submit_{item['id']}"):
                        item["status"] = "Submitted"
                        st.success("Submitted to the human review queue.")
                        st.rerun()

# -----------------------------
# Human review
# -----------------------------
elif page == "Human review":
    st.title("Human governance review")
    st.write("This is a workflow placeholder. Formal approval authority remains with the organisation's designated reviewer.")

    pending = [x for x in st.session_state.use_cases if x["status"] == "Submitted"]
    if not pending:
        st.info("There are no assessments awaiting review. Submit a draft from the Assessment inventory.")
    else:
        for item in pending:
            with st.expander(f"{item['id']} — {item['name']}"):
                st.write(f"**Business purpose:** {item['purpose']}")
                st.write(f"**Owner:** {item['owner']}")
                note = st.text_area("Reviewer notes", key=f"note_{item['id']}")
                decision = st.selectbox(
                    "Demonstration review outcome",
                    ["Further information required", "Reviewed – not an approval"],
                    key=f"decision_{item['id']}",
                )
                if st.button("Save review note", key=f"review_{item['id']}"):
                    st.session_state.review_notes[item["id"]] = {
                        "notes": note,
                        "outcome": decision,
                    }
                    item["status"] = "Reviewed"
                    st.success("Review note saved. This prototype does not grant deployment approval.")
                    st.rerun()

# -----------------------------
# About
# -----------------------------
elif page == "About the MVP":
    st.title("About this MVP")
    st.markdown(
        """
        **Product vision**

        Help organisations register AI use cases and prepare evidence-based
        governance assessments with human oversight.

        **Current implementation**

        - Streamlit navigation and dashboard
        - AI use-case registration
        - Session-based demonstration inventory
        - Basic submission and human-review workflow

        **Not yet implemented**

        - Gemini integration
        - Document upload and extraction
        - Policy knowledge base / RAG
        - Risk scoring and control mapping
        - PDF assessment report
        - Persistent database and production authentication

        **Important:** This is a learning and demonstration prototype, not a
        compliance certification or production governance system.
        """
    )

st.sidebar.divider()
st.sidebar.caption("AI Governance Agent • MVP build 0.1")
