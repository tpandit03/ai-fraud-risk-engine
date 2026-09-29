import pandas as pd

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    x = df.copy()
    x["hour"] = pd.to_datetime(x["timestamp"]).dt.hour
    x["is_night"] = x["hour"].apply(lambda h: int(h < 6 or h >= 23))
    x["amount_log"] = (x["amount"] + 1).apply(lambda v: __import__("math").log(v))
    return x
