# Fintech Loan Eligibility Tools

This repository contains two user-friendly Streamlit-based loan eligibility apps:
- *Fintech Friendly Loan Eligibility App*
- *Multitype Loan Eligibility Predictor*

Both are built for educational, demo, and mock assessment purposes, inspired by real-world fintech and banking practices.

---

## 1️⃣ Fintech Friendly Loan Eligibility App

### Overview

A fast, intuitive web app that helps users check their eligibility for instant fintech loans (like KreditBee, CASHe, NIRA, etc.).  
It uses relaxed, fintech-style criteria and provides an estimated maximum loan amount based on user inputs.

### Features

- Instant eligibility check (no credit impact)
- Considers age, employment type, income, credit score, ongoing EMIs, KYC, and bank account status
- Shows reasons for ineligibility
- Estimates maximum loan amount as per fintech norms
- For demo/education only (does not store any data)

  ---

  ## 2️⃣ Multitype Loan Eligibility Predictor

### Overview

A versatile web app that allows users to check their mock eligibility for various types of loans:
- Personal Loan
- Home Loan
- Car Loan
- Business Loan
- Education Loan

Criteria are customized for each loan type, matching typical requirements of banks and NBFCs.

### Features

- Select loan type and enter relevant details
- Custom eligibility rules for different loans (age, income, credit, job/business stability, etc.)
- Explains reasons for eligibility/ineligibility for transparency
- No real data stored or submitted; demo/mock use only

### How to Run

1. Ensure you have Python and Streamlit installed:
   bash
   pip install streamlit
   
2. Run the app:
   bash
   streamlit run fintech_multitype_loan_eligibility_app.py
   

3. Open the provided local URL in your browser.

---

## Demo / Disclaimer

- These tools are for educational and demonstration purposes only.
- Real fintech and bank decisions may use additional data and different criteria.
- No personal data is stored, and results do *not* impact your actual credit score.

  ---
