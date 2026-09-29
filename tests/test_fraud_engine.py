import pandas as pd
from src.features import build_features
from src.rules import evaluate_rules
from src.engine import FraudRiskEngine

def test_rules():
    row = {
        "amount": 20000, "is_night": 1, "velocity_1h": 7, "cross_border": 1
    }
    reasons = evaluate_rules(row)
    assert set(reasons) == {"HIGH_AMOUNT","NIGHT_TRANSACTION","HIGH_VELOCITY","CROSS_BORDER"}

def test_engine():
    df = pd.DataFrame([
        ["A","2026-08-01 10:00:00",100,1,0],
        ["B","2026-08-01 11:00:00",150,1,0],
        ["C","2026-08-01 12:00:00",200,2,0],
        ["D","2026-08-01 13:00:00",300,1,0],
        ["E","2026-08-01 14:00:00",400,2,0],
        ["F","2026-08-01 15:00:00",500,2,0],
        ["G","2026-08-01 16:00:00",600,1,0],
        ["H","2026-08-01 17:00:00",700,1,0],
        ["I","2026-08-01 18:00:00",800,1,0],
        ["J","2026-08-01 19:00:00",900,1,0],
    ], columns=["transaction_id","timestamp","amount","velocity_1h","cross_border"])
    engine = FraudRiskEngine(df)
    out = engine.score(df)
    assert "risk_score" in out
    assert out["decision"].isin(["ALLOW","MONITOR","REVIEW"]).all()
