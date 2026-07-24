<div align="center">

# 🚀 Serverless Crypto ETL Pipeline
### Production-grade, fault-tolerant data pipeline running entirely on serverless architecture.

[![CI/CD Pipeline Status](https://github.com/aditi0103singh/Resilient-Crypto-Market-Data-Pipeline/actions/workflows/main.yml/badge.svg)](https://github.com/aditi0103singh/Resilient-Crypto-Market-Data-Pipeline/actions)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

## 📌 Overview
The world of data engineering is ever-changing, with new tools and technologies emerging regularly. Building an effective, reliable ingestion framework can be challenging when dealing with unstable third-party APIs. 

**Resilient Crypto Market Data Pipeline** is an automated, production-grade data pipeline designed to ingest real-time cryptocurrency metrics from external APIs, validate structural data integrity, and handle network instability gracefully. Built to run on zero-overhead serverless infrastructure, it implements best practices in modern data engineering such as robust fault tolerance, automated CI/CD scheduling, and strict separation of configuration and secrets.

---

## 📊 System Architecture

```text
                                  [ CoinGecko API ] 
                                          │
                   ▼ (HTTPS / Rate-Limited Retry Session w/ Backoff)
┌────────────────────────────────────────────────────────────────────────┐
│                      GitHub Actions (Serverless)                       │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │ Python ETL Pipeline                                              │  │
│  │  ├── Robust HTTP Adapter (Transient Fault Handling)              │  │
│  │  ├── Defensive Payload Checks (Data Quality)                     │  │
│  │  └── Structured Logging & Monitoring                             │  │
│  └──────────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────┘
                                          │
                     ▼ (Secure Environment Variables via Secrets)
                         [ Secure Database / Destination ]
## 🛠️ Tech Stack & Engineering Highlights
* Language: Python 3.10+

* Orchestration / Compute: GitHub Actions (Serverless Cron triggers)

* Resilience: requests, urllib3 (Configured with custom retry strategies and exponential backoff for 429, 500, 502, 503, 504 errors).
 
* Data Quality: Implemented pre-transformation payload validation checks to catch empty or malformed responses and raise clean warnings instead of unhandled exceptions.

* Security: Zero hardcoded credentials; managed entirely through environment variables (python-dotenv & GitHub Actions Secrets).

## 📁 Repository Structure
Plaintext
├── .github/
│   └── workflows/          # GitHub Actions CI/CD pipeline definitions
├── requirements.txt        # Python package dependencies
├── main.py                 # Core ETL script (Extraction, Validation, Load)
└── README.md               # Project documentation
⚙️ Local Setup & Installation


1. Clone the repository:
git clone [https://github.com/aditi0103singh/Resilient-Crypto-Market-Data-Pipeline.git](https://github.com/aditi0103singh/Resilient-Crypto-Market-Data-Pipeline.git)
cd Resilient-Crypto-Market-Data-Pipeline

2. Create and activate a virtual environment:
For Mac/Linux:
python3 -m venv venv
source venv/bin/activate

For Windows (PowerShell):
python -m venv venv
.\venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Configure environment variables:
Create a .env file in the root directory:
COINGECKO_API_KEY=your_api_key_here

5. Run the pipeline locally:
python main.py

## 💡 Engineering Decisions & Trade-offs

Why Serverless over EC2/VPS? For scheduled batch processing jobs, maintaining a 24/7 virtual machine incurs unnecessary idle costs. GitHub Actions acts as a lightweight, zero-maintenance serverless runner that executes the script on a schedule and shuts down immediately.

Fault Tolerance Strategy: Third-party APIs are inherently unstable. Coupling HTTP retry adapters with structural data validation ensures the pipeline either recovers automatically from transient network failures or fails cleanly without corrupting downstream databases.

👤 Author
Aditi Singh

Check out my other projects and repositories on GitHub.