# AI Fraud Risk Engine

An explainable fraud-risk prototype for financial transactions. It combines deterministic fraud rules with a machine-learning model and produces an auditable risk decision.

## What it demonstrates

**Transaction → Feature Validation → Rules + ML → Risk Score → Explanation → Audit Record**

The goal is not to claim production fraud-detection accuracy. The repository demonstrates how AI can be placed inside a controlled financial-risk workflow.

## Features

- Synthetic transaction generator
- Feature engineering
- Deterministic fraud rules
- Isolation Forest anomaly model
- Combined risk scoring
- Explainable reason codes
- Audit-ready JSON output
- Unit tests

## Run

```bash
python -m venv .venv
# activate it
pip install -r requirements.txt
python scripts/generate_data.py
python -m src.cli --transaction 5
pytest
```

## Risk logic

The prototype combines:
- High transaction amount
- Unusual transaction hour
- High-velocity behavior
- Cross-border transaction indicator
- ML anomaly score

The rule layer remains deterministic and explainable. The ML layer is treated as one signal rather than the sole decision-maker.

## Disclaimer

Synthetic portfolio project only. It is not a production fraud model, does not establish compliance, and must not be used for real customer decisions without proper model validation, fairness testing, security controls, monitoring, and regulatory review.
