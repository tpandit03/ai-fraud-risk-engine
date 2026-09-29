import argparse
import pandas as pd
from .engine import FraudRiskEngine

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/transactions.csv")
    parser.add_argument("--transaction", type=int, required=True)
    args = parser.parse_args()

    df = pd.read_csv(args.data)
    engine = FraudRiskEngine(df)
    scored = engine.score(df)
    row = scored.iloc[args.transaction]
    print(f"Transaction: {row['transaction_id']}")
    print(f"Risk score: {row['risk_score']:.2f}")
    print(f"Decision: {row['decision']}")
    print(f"Reasons: {', '.join(row['rule_reasons']) or 'ML signal only'}")
    print(f"Audit: {row['audit_event']}")

if __name__ == "__main__":
    main()
