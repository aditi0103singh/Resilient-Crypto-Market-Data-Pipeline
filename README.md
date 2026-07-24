<div align="center">

# 🚀 Serverless Crypto ETL Pipeline
### Production-grade, fault-tolerant data pipeline running entirely on serverless architecture.

[![CI/CD Pipeline Status](https://github.com/aditi0103singh/Resilient-Crypto-Market-Data-Pipeline/actions/workflows/main.yml/badge.svg)](https://github.com/aditi0103singh/Resilient-Crypto-Market-Data-Pipeline/actions)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

## 📌 Overview
An automated data pipeline designed to ingest real-time cryptocurrency metrics from external APIs, validate data integrity, and handle network instability gracefully. Built to run on zero-overhead serverless infrastructure with strict separation of configuration and secrets.

---

## 📊 System Architecture

<div align="center" style="font-family: monospace; text-align: center;">

[ CoinGecko API ]<br>
│<br>
▼ (HTTPS / Rate-Limited Retry Session w/ Backoff)<br>
┌────────────────────────────────────────────────────────┐<br>
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GitHub Actions (Serverless) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; │<br>
│ &nbsp;┌──────────────────────────────────────────────────┐ &nbsp;│<br>
│ &nbsp;│ Python ETL Pipeline &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; │ &nbsp;│<br>
│ &nbsp;│ &nbsp;├── Robust HTTP Adapter (Transient Fault Handling)│ &nbsp;│<br>
│ &nbsp;│ &nbsp;├── Defensive Payload Checks (Data Quality) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; │ &nbsp;│<br>
│ &nbsp;│ &nbsp;└── Structured Logging & Monitoring &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; │ &nbsp;│<br>
│ &nbsp;└──────────────────────────────────────────────────┘ &nbsp;│<br>
└────────────────────────────────────────────────────────┘<br>
│<br>
▼ (Secure Environment Variables via Secrets)<br>
[ Secure Database / Destination ]

</div>

## 🛠️ Tech Stack & Engineering Highlights

* **Language:** Python
* **Orchestration / Compute:** GitHub Actions (Serverless Cron triggers)
* **Resilience:** `requests`, `urllib3` (Configured with custom retry strategies and exponential backoff for `429`, `500`, `502`, `503`, `504` errors).
* **Data Quality:** Implemented pre-transformation payload validation checks to catch empty or malformed responses.
* **Security:** Zero hardcoded credentials managed through GitHub Secrets.

## 📁 Repository Structure

```text
├── .github/
│   └── workflows/          # GitHub Actions CI/CD pipeline definitions
├── requirements.txt        # Python package dependencies
├── main.py                 # Core ETL script (Extraction, Validation, Load)
└── README.md               # Project documentation

## ⚙️ Local Setup & Installation

**1. Clone the repository:**
```bash
git clone [https://github.com/aditi0103singh/Resilient-Crypto-Market-Data-Pipeline.git](https://github.com/aditi0103singh/Resilient-Crypto-Market-Data-Pipeline.git)
cd Resilient-Crypto-Market-Data-Pipeline

* Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies:

pip install -r requirements.txt

* Configure environment variables:
  Create a .env file in the root directory:

COINGECKO_API_KEY=your_api_key_here


8 Run the pipeline locally:
python main.py

💡 Engineering Decisions & Trade-offs

Why Serverless over EC2/VPS? For scheduled batch processing jobs, maintaining a 24/7 virtual machine incurs unnecessary idle costs. GitHub Actions acts as a lightweight, zero-maintenance serverless runner that executes the script on a schedule and shuts down immediately.

Fault Tolerance Strategy: Third-party APIs are inherently unstable. Coupling HTTP retry adapters with structural data validation ensures the pipeline either recovers automatically from transient network failures or fails cleanly without corrupting downstream databases.