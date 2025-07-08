import streamlit as st

st.set_page_config(page_title="Multitype Loan Eligibility Predictor", page_icon="💸", layout="centered")
st.title("💸 Multitype Loan Eligibility Predictor")
st.write("Fill in your details to check your eligibility for various loan types. For mock/demo use only.")

with st.form("loan_eligibility_form"):
    loan_type = st.selectbox(
        "Select Loan Type",
        [
            "Personal Loan",
            "Home Loan",
            "Car Loan",
            "Business Loan",
            "Education Loan",
        ],
    )

    # Common inputs
    age = st.number_input("Applicant Age", min_value=16, max_value=80, value=30)
    credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=700)
    monthly_income = st.number_input("Applicant Monthly Income (₹ or $)", min_value=0, value=30000, step=1000)
    employment_type = st.selectbox("Applicant Type", ["Salaried", "Self-Employed", "Business Owner", "Student"])
    employment_years = st.number_input("Years in Current Employment/Business", min_value=0, value=2, step=1)
    loan_amount = st.number_input("Requested Loan Amount", min_value=1000, value=100000, step=1000)
    loan_term = st.number_input("Loan Term (Months)", min_value=6, max_value=480, value=60, step=6)

    # Extra fields for business loan
    if loan_type == "Business Loan":
        business_vintage = st.number_input("Years Business in Operation", min_value=0, value=3, step=1)
        annual_turnover = st.number_input("Annual Turnover (₹ or $)", min_value=0, value=1000000, step=10000)
        collateral = st.selectbox("Collateral (if any)", ["None", "Property", "Equipment", "Other"])

    # Extra fields for education loan
    if loan_type == "Education Loan":
        coapplicant_income = st.number_input("Co-applicant Monthly Income (₹ or $)", min_value=0, value=30000, step=1000)
        admission_confirmed = st.selectbox("Admission to Recognized Institute?", ["Yes", "No"])
        collateral_edu = st.selectbox("Collateral for high-value loan?", ["No", "Yes"])
        coapplicant = st.selectbox("Co-applicant (Usually Parent/Guardian)?", ["Yes", "No"])

    submit = st.form_submit_button("Check Eligibility")

def check_personal():
    eligible = True
    reasons = []
    if not (21 <= age <= 60):
        eligible = False
        reasons.append("Age must be between 21 and 60 years.")
    if monthly_income < 15000:
        eligible = False
        reasons.append("Minimum monthly income should be ₹15,000 or $2,000.")
    if credit_score < 650:
        eligible = False
        reasons.append("Credit score must be at least 650.")
    if employment_type == "Salaried" and employment_years < 0.5:
        eligible = False
        reasons.append("At least 6 months in current salaried job.")
    if employment_type == "Self-Employed" and employment_years < 2:
        eligible = False
        reasons.append("At least 2 years of self-employment.")
    # Simple DTI check (loan EMI max 50% of income, no actual EMI calc here)
    if loan_amount / max(1, loan_term) > 0.5 * monthly_income:
        eligible = False
        reasons.append("Requested loan amount is high for your income/term.")
    return eligible, reasons

def check_home():
    eligible = True
    reasons = []
    if not (21 <= age <= 70):
        eligible = False
        reasons.append("Age must be between 21 and 70 years.")
    if monthly_income < 25000:
        eligible = False
        reasons.append("Minimum monthly income should be ₹25,000 or $3,000.")
    if credit_score < 700:
        eligible = False
        reasons.append("Credit score must be at least 700.")
    if employment_type == "Salaried" and employment_years < 2:
        eligible = False
        reasons.append("Salaried applicants need 2+ years in job.")
    if employment_type == "Self-Employed" and employment_years < 3:
        eligible = False
        reasons.append("Self-employed need 3+ years business stability.")
    return eligible, reasons

def check_car():
    eligible = True
    reasons = []
    if not (21 <= age <= 65):
        eligible = False
        reasons.append("Age must be between 21 and 65 years.")
    if monthly_income < 20000:
        eligible = False
        reasons.append("Minimum monthly income should be ₹20,000 or $2,500.")
    if credit_score < 650:
        eligible = False
        reasons.append("Credit score must be at least 650.")
    if employment_type == "Salaried" and employment_years < 1:
        eligible = False
        reasons.append("Salaried: 1+ year experience required.")
    if employment_type == "Self-Employed" and employment_years < 2:
        eligible = False
        reasons.append("Self-employed: 2+ years in business required.")
    return eligible, reasons

def check_business():
    eligible = True
    reasons = []
    if not (21 <= age <= 65):
        eligible = False
        reasons.append("Age must be between 21 and 65 years.")
    if business_vintage < 2:
        eligible = False
        reasons.append("Business must be operational for at least 2 years.")
    if annual_turnover < 1000000:
        eligible = False
        reasons.append("Annual turnover should be ₹10 lakh+ ($50,000+).")
    if credit_score < 650:
        eligible = False
        reasons.append("Credit score must be at least 650.")
    # Collateral is optional, not mandatory
    return eligible, reasons

def check_education():
    eligible = True
    reasons = []
    if not (18 <= age <= 35):
        eligible = False
        reasons.append("Age must be between 18 and 35 years.")
    if admission_confirmed != "Yes":
        eligible = False
        reasons.append("Admission to a recognized institute is mandatory.")
    if coapplicant != "Yes":
        eligible = False
        reasons.append("Co-applicant (parent/guardian) is mandatory.")
    # For high-value loans, collateral is required (arbitrary: >7.5 lakh or $20,000)
    if loan_amount > 750000 and collateral_edu != "Yes":
        eligible = False
        reasons.append("Collateral required for high-value education loans.")
    return eligible, reasons

if submit:
    if loan_type == "Personal Loan":
        eligible, reasons = check_personal()
    elif loan_type == "Home Loan":
        eligible, reasons = check_home()
    elif loan_type == "Car Loan":
        eligible, reasons = check_car()
    elif loan_type == "Business Loan":
        eligible, reasons = check_business()
    elif loan_type == "Education Loan":
        eligible, reasons = check_education()
    else:
        eligible, reasons = False, ["Invalid loan type."]

    st.markdown("---")
    if eligible:
        st.success(f"🎉 You are **likely eligible** for a {loan_type.lower()}!")
    else:
        st.error(f"❌ You are **not eligible** for a {loan_type.lower()} based on provided details.")

    st.markdown("#### Explanation:")
    for reason in reasons:
        st.write("-", reason)
    st.info("> This is a mock assessment tool. Actual bank/FI policies may vary.")

st.markdown("---")
st.caption("© 2025 Multitype Loan Predictor Demo. For educational/mock use only.")
