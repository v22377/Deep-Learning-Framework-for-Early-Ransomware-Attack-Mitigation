import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Sample training data
X = np.array([
    [10, 20, 5],
    [200, 90, 80],
    [15, 30, 10],
    [250, 85, 70]
])

# Labels
# 0 = Safe
# 1 = Malicious
y = [0, 1, 0, 1]

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

def predict_model(features):
    prediction = model.predict([features])
    return prediction[0]
