import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Sample dataset (synthetic but meaningful)
data = {
    "temp": [20, 22, 25, 28, 30, 32, 35, 18, 21, 27],
    "humidity": [85, 80, 60, 70, 50, 45, 40, 90, 88, 65],
    "wind": [5, 4, 3, 3, 2, 2, 3, 6, 5, 3],
    "rain": [1, 1, 0, 1, 0, 0, 0, 1, 1, 0]
}

df = pd.DataFrame(data)

X = df[["temp", "humidity", "wind"]]
y = df["rain"]

model = LogisticRegression()
model.fit(X, y)

# Save model
with open("weather_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully and saved as weather_model.pkl")