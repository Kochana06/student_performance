import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


df = pd.read_csv("student_eligibility.csv")


df["Eligibility"] = df["Eligibility"].map({
    "Yes": 1,
    "No": 0
})

X = df[["CGPA", "Attendance"]]
y = df["Eligibility"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)


accuracy = model.score(X_test, y_test)
print(f"Accuracy : {accuracy*100:.2f}%")

joblib.dump(model, "student_model.pth")

print("Model saved successfully.")