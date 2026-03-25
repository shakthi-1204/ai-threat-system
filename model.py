import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

data = pd.DataFrame({
    "packets": np.random.randint(10, 100, 500),
    "bytes": np.random.randint(100, 1200, 500),
    "duration": np.random.randint(1, 10, 500)
})

def label_attack(row):
    if row["packets"] > 80:
        return "Flood Attack"
    elif row["bytes"] > 950:
        return "Data Exfiltration"
    elif row["duration"] < 3 and row["packets"] > 60:
        return "DoS Attack"
    else:
        return "Normal"

data["label"] = data.apply(label_attack, axis=1)

X = data[["packets", "bytes", "duration"]]
y = data["label"]

model = RandomForestClassifier()
model.fit(X, y)

def predict(p, b, d):
    result = model.predict([[p, b, d]])[0]
    prob = max(model.predict_proba([[p, b, d]])[0]) * 100
    return result, round(prob, 2)