from pathlib import Path
import random
import pandas as pd

random.seed(7)
rows = []
for i in range(500):
    amount = round(random.lognormvariate(7.1, 0.8), 2)
    velocity = random.randint(0, 3)
    cross_border = random.random() < 0.12
    hour = random.randint(0, 23)
    rows.append([
        f"TX-{i:05d}",
        f"2026-08-{random.randint(1,28):02d} {hour:02d}:{random.randint(0,59):02d}:00",
        amount, velocity, int(cross_border)
    ])

# Inject a handful of synthetic suspicious records.
for j, idx in enumerate([11, 88, 201, 377]):
    rows[idx][2] = 25000 + j * 7000
    rows[idx][3] = 8
    rows[idx][4] = 1

df = pd.DataFrame(rows, columns=["transaction_id","timestamp","amount","velocity_1h","cross_border"])
Path("data").mkdir(exist_ok=True)
df.to_csv("data/transactions.csv", index=False)
print("Generated", len(df), "synthetic transactions.")
