import streamlit as st

st.set_page_config(page_title="Fintech Loan Eligibility Checker", page_icon="💸", layout="centered")
st.title("💸 Fintech Loan Eligibility Checker")
st.write("""
This is a **mock eligibility tool** inspired by real-world fintech lending apps (like KreditBee, PaySense, CASHe, MoneyTap, NIRA, etc).
Get an instant mock result — no hard inquiry, no credit impact.
""")

with st.form("fintech_loan_form"):
    age = st.number_input("Your Age", min_value=18, max_value=60, value=25)
    employment = st.selectbox("Your Employment Type", ["Salaried", "Self-Employed", "Gig/Freelancer", "Student", "Other"])
    net_monthly_income = st.number_input("Net Monthly Income (₹)", min_value=0, value=20000, step=1000)
    existing_emi = st.number_input("Total Ongoing Monthly Loan EMIs (₹)", min_value=0, value=0, step=500)
    desired_loan_amount = st.number_input("Desired Loan Amount (₹)", min_value=1000, max_value=500000, value=50000, step=1000)
    tenure_months = st.selectbox("Preferred Loan Tenure (Months)", [3, 6, 9, 12, 18, 24, 36])
    credit_score = st.selectbox("Do you know your credit score?", ["I don't know", "Below 600", "600-650", "651-700", "Above 700"])
    bank_account = st.selectbox("Do you have an active bank account?", ["Yes", "No"])
    digital_id = st.selectbox("Do you have Aadhaar/ID proof and PAN?", ["Yes", "No"])
    submit = st.form_submit_button("Check My Eligibility (Mock)")

def fintech_mock_eligibility(age, employment, net_income, existing_emi, loan_amt, tenure, credit_score, bank_ac, digital_id):
    max_loan = min(net_income * 10, 500000)  # Most fintechs give up to 10x monthly income, capped
    dti_ratio = (existing_emi + (loan_amt/tenure)) / (net_income + 1e-6)  # simple DTI
    score = 0
    reasons = []
    # Age
    if not (18 <= age <= 60):
        reasons.append("Not in the eligible age range (18–60).")
    else:
        score += 1
    # Income
    if net_income < 10000:
        reasons.append("Minimum monthly income should be ₹10,000+.")
    else:
        score += 1
    # Bank account & KYC
    if bank_ac != "Yes" or digital_id != "Yes":
        reasons.append("Active bank account and digital KYC (Aadhaar/PAN) are mandatory.")
    else:
        score += 1
    # Credit score
    if credit_score in ["I don't know", "Above 700", "651-700", "600-650"]:
        score += 1
    else:
        reasons.append("Most fintechs require a 600+ credit score (but some may offer loans based on alternative data).")
    # DTI check (EMI should not exceed 50% of income)
    if dti_ratio > 0.5:
        reasons.append("Requested EMI plus ongoing EMIs is high for your income (should be under 50%).")
    else:
        score += 1
    # Employment: Most types accepted
    if employment == "Other":
        reasons.append("Employment type is less preferred — may face extra checks.")
    else:
        score += 1

    eligible = (score >= 5) and (loan_amt <= max_loan)
    
    # Estimated max loan
    estimated_loan = round(max_loan/1000) * 1000

    # Result summary
    summary = {
        "eligible": eligible,
        "score": score,
        "max_loan": estimated_loan,
        "dti": dti_ratio,
        "reasons": reasons
    }
    return summary

if submit:
    summary = fintech_mock_eligibility(
        age, employment, net_monthly_income, existing_emi,
        desired_loan_amount, tenure_months,
        credit_score, bank_account, digital_id
    )
    st.markdown("---")
    if summary["eligible"]:
        st.success(
            f"🎉 **You are likely eligible for a fintech app loan!**\n\n"
            f"**Estimated Maximum Loan:** ₹{summary['max_loan']:,}\n"
            f"**Debt-to-Income Ratio:** {summary['dti']*100:.1f}%"
        )
    else:
        st.error(
            "Based on your details, you may **not be eligible** for a fintech loan right now."
        )
    st.markdown("#### Why?")
    if summary["reasons"]:
        for reason in summary["reasons"]:
            st.write("-", reason)
    else:
        st.write("✅ Meets all typical fintech eligibility checks.")

    st.info("**Note:** This is a mock result. Actual fintech app criteria may vary, and some apps may approve you even if you don't meet all these checks — especially if you have good alternative digital data (UPI, phone usage, etc.).\n\nNo data is saved, and there's no impact on your actual credit score.")

st.markdown("---")
st.caption("© 2025 Fintech App Loan Eligibility Checker — For mock/demo/education only.")
