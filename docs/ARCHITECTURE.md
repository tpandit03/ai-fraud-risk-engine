# Architecture

```text
                +------------------+
Transactions -->| Feature Builder  |
                +--------+---------+
                         |
             +-----------+-----------+
             |                       |
             v                       v
      Deterministic Rules       ML Anomaly Model
             |                       |
             +-----------+-----------+
                         v
                  Risk Aggregator
                         |
             +-----------+-----------+
             |                       |
             v                       v
        Decision + Reasons      Audit Event
```

## Why hybrid?

Rules provide explicit controls for known risk patterns. ML detects patterns not encoded in rules. Neither layer should silently override the other; the combined score and reasons are recorded.

## Production extension

- Calibrated supervised model
- Feature store
- Online velocity service
- Model registry
- Champion/challenger evaluation
- Human review queue
- Drift monitoring
- Bias/fairness testing
- Immutable audit storage
