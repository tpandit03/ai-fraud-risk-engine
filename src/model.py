from sklearn.ensemble import IsolationForest
import pandas as pd

FEATURES = ["amount_log", "velocity_1h", "cross_border", "is_night"]

class FraudModel:
    def __init__(self):
        self.model = IsolationForest(random_state=42, contamination=0.08)
        self.fitted = False

    def fit(self, df: pd.DataFrame):
        self.model.fit(df[FEATURES])
        self.fitted = True
        return self

    def score(self, df: pd.DataFrame):
        if not self.fitted:
            raise RuntimeError("Model must be fitted first.")
        raw = -self.model.decision_function(df[FEATURES])
        mn, mx = raw.min(), raw.max()
        if mx == mn:
            return pd.Series([0.0] * len(df), index=df.index)
        return (raw - mn) / (mx - mn)
