import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)


df = pd.read_csv("data/processed_xau_15m.csv")

print("Размер датасета:", df.shape)
print("\nПервые строки:")
print(df.head())

features = ["Open", "High", "Low", "Volume"]

X_reg = df[features]
y_reg = df["Close"]

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg,
    y_reg,
    test_size=0.2,
    random_state=42,
)

reg_model = LinearRegression()
reg_model.fit(X_train_reg, y_train_reg)

y_pred_reg = reg_model.predict(X_test_reg)

mse = mean_squared_error(y_test_reg, y_pred_reg)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test_reg, y_pred_reg)
r2 = r2_score(y_test_reg, y_pred_reg)

print("\n===== ЛИНЕЙНАЯ РЕГРЕССИЯ =====")
print("Целевой признак: Close")
print("Признаки:", features)
print(f"MSE  = {mse:.10f}")
print(f"RMSE = {rmse:.10f}")
print(f"MAE  = {mae:.10f}")
print(f"R^2  = {r2:.10f}")

print("\nКоэффициенты модели:")
for name, coef in zip(features, reg_model.coef_):
    print(f"{name}: {coef:.10f}")
print(f"Свободный коэффициент: {reg_model.intercept_:.10f}")

sample_size = 300
plt.figure(figsize=(10, 5))
plt.plot(y_test_reg.iloc[:sample_size].to_numpy(), label="Фактический Close")
plt.plot(y_pred_reg[:sample_size], label="Предсказанный Close")
plt.title("Линейная регрессия: фактические и предсказанные значения")
plt.xlabel("Наблюдение")
plt.ylabel("Нормализованный Close")
plt.legend()
plt.tight_layout()
plt.savefig("regression_result.png", dpi=150)
plt.close()


median_close = df["Close"].median()
df["price_class"] = (df["Close"] > median_close).astype(int)

X_clf = df[features]
y_clf = df["price_class"]

X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(
    X_clf,
    y_clf,
    test_size=0.2,
    random_state=42,
    stratify=y_clf,
)

clf_model = LogisticRegression(max_iter=1000)
clf_model.fit(X_train_clf, y_train_clf)

y_pred_clf = clf_model.predict(X_test_clf)

accuracy = accuracy_score(y_test_clf, y_pred_clf)
precision = precision_score(y_test_clf, y_pred_clf)
recall = recall_score(y_test_clf, y_pred_clf)
f1 = f1_score(y_test_clf, y_pred_clf)
cm = confusion_matrix(y_test_clf, y_pred_clf)

print("\n===== ЛОГИСТИЧЕСКАЯ РЕГРЕССИЯ =====")
print(f"Медианное значение Close: {median_close:.10f}")
print("Класс 0: Close <= медианы")
print("Класс 1: Close > медианы")
print(f"Accuracy  = {accuracy:.6f}")
print(f"Precision = {precision:.6f}")
print(f"Recall    = {recall:.6f}")
print(f"F1-score  = {f1:.6f}")

print("\nМатрица ошибок:")
print(cm)

print("\nClassification report:")
print(classification_report(y_test_clf, y_pred_clf, digits=6))

# Визуализация confusion matrix без seaborn
plt.figure(figsize=(5, 4))
plt.imshow(cm)
plt.title("Confusion matrix")
plt.xlabel("Предсказанный класс")
plt.ylabel("Истинный класс")
plt.xticks([0, 1], ["0", "1"])
plt.yticks([0, 1], ["0", "1"])

for i in range(2):
    for j in range(2):
        plt.text(j, i, str(cm[i, j]), ha="center", va="center")

plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=150)
plt.close()

# ------------------------------------------------------------
# 4. Сохранение результатов в текстовый файл для GitHub
# ------------------------------------------------------------
with open("lab2_results.txt", "w", encoding="utf-8") as file:
    file.write("Лабораторная работа №2\n")
    file.write("Задачи регрессии и классификации\n\n")

    file.write("ЛИНЕЙНАЯ РЕГРЕССИЯ\n")
    file.write("Целевой признак: Close\n")
    file.write(f"MSE = {mse:.10f}\n")
    file.write(f"RMSE = {rmse:.10f}\n")
    file.write(f"MAE = {mae:.10f}\n")
    file.write(f"R^2 = {r2:.10f}\n\n")

    file.write("ЛОГИСТИЧЕСКАЯ РЕГРЕССИЯ\n")
    file.write(f"Медианное значение Close = {median_close:.10f}\n")
    file.write(f"Accuracy = {accuracy:.6f}\n")
    file.write(f"Precision = {precision:.6f}\n")
    file.write(f"Recall = {recall:.6f}\n")
    file.write(f"F1-score = {f1:.6f}\n")
    file.write("Матрица ошибок:\n")
    file.write(str(cm))
    file.write("\n\nClassification report:\n")
    file.write(classification_report(y_test_clf, y_pred_clf, digits=6))

print("\nРезультаты сохранены в lab2_results.txt")
print("Графики сохранены в regression_result.png и confusion_matrix.png")
