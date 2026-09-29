import json
from datetime import datetime, timezone
from .features import build_features
from .rules import evaluate_rules
from .model import FraudModel

class FraudRiskEngine:
    def __init__(self, training_df):
        self.model = FraudModel().fit(build_features(training_df))

    def score(self, df):
        x = build_features(df)
        x["ml_risk"] = self.model.score(x)
        x["rule_reasons"] = x.apply(evaluate_rules, axis=1)
        x["rule_risk"] = x["rule_reasons"].apply(lambda r: min(len(r) / 4, 1.0))
        x["risk_score"] = (0.55 * x["ml_risk"] + 0.45 * x["rule_risk"]) * 100
        x["decision"] = x["risk_score"].apply(
            lambda s: "REVIEW" if s >= 60 else ("MONITOR" if s >= 35 else "ALLOW")
        )
        x["audit_event"] = x.apply(self._audit_event, axis=1)
        return x

    @staticmethod
    def _audit_event(row):
        return json.dumps({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "transaction_id": row["transaction_id"],
            "decision": row["decision"],
            "risk_score": round(float(row["risk_score"]), 2),
            "reason_codes": row["rule_reasons"],
            "model_component": round(float(row["ml_risk"]), 4),
            "rules_component": round(float(row["rule_risk"]), 4),
        })
