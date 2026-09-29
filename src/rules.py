def evaluate_rules(row) -> list[str]:
    reasons = []
    if row["amount"] >= 15000:
        reasons.append("HIGH_AMOUNT")
    if row["is_night"] == 1:
        reasons.append("NIGHT_TRANSACTION")
    if row["velocity_1h"] >= 5:
        reasons.append("HIGH_VELOCITY")
    if row["cross_border"] == 1:
        reasons.append("CROSS_BORDER")
    return reasons
