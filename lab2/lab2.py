import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


df = pd.read_csv("data/processed_online_food.csv")


X_reg = df.drop(columns=["Age"])
y_reg = df["Age"]

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg,
    y_reg,
    test_size=0.2,
    random_state=42
)

reg_model = LinearRegression()
reg_model.fit(X_train_reg, y_train_reg)

y_pred_reg = reg_model.predict(X_test_reg)

mse = mean_squared_error(y_test_reg, y_pred_reg)
rmse = mse ** 0.5
mae = mean_absolute_error(y_test_reg, y_pred_reg)

print("ЛИНЕЙНАЯ РЕГРЕССИЯ")
print("MSE:", mse)
print("RMSE:", rmse)
print("MAE:", mae)


X_clf = df.drop(columns=["Output", "Feedback"])
y_clf = df["Output"]

X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(
    X_clf,
    y_clf,
    test_size=0.2,
    random_state=42,
    stratify=y_clf
)

clf_model = LogisticRegression(max_iter=2000)
clf_model.fit(X_train_clf, y_train_clf)

y_pred_clf = clf_model.predict(X_test_clf)

accuracy = accuracy_score(y_test_clf, y_pred_clf)
precision = precision_score(y_test_clf, y_pred_clf, zero_division=0)
recall = recall_score(y_test_clf, y_pred_clf, zero_division=0)
f1 = f1_score(y_test_clf, y_pred_clf, zero_division=0)
cm = confusion_matrix(y_test_clf, y_pred_clf)

print("\nЛОГИСТИЧЕСКАЯ РЕГРЕССИЯ")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
print("Матрица ошибок:")
print(cm)