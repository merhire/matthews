import pandas as pd

# Загружаем датасет
df = pd.read_csv("data/online_food_delivery_dataset.csv.csv")

# Вывод первых строк
print("Исходные данные:")
print(df.head())

# Удаляем лишний столбец
if "Unnamed: 13" in df.columns:
    df = df.drop(columns=["Unnamed: 13"])


# -------------------------------
# 1. Проверка пропущенных значений
# -------------------------------

print("\nКоличество пропущенных значений:")
print(df.isnull().sum())


# -------------------------------
# 2. Заполнение пропусков
# -------------------------------

# Числовые столбцы
numeric_cols = [
    "Age",
    "Family size",
    "latitude",
    "longitude",
    "Pin code"
]

# Заполняем пропуски медианой
for col in numeric_cols:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].median())


# Категориальные столбцы
categorical_cols = [
    "Gender",
    "Marital Status",
    "Occupation",
    "Monthly Income",
    "Educational Qualifications",
    "Customer Type",
    "Output",
    "Feedback"
]

# Заполняем пропуски самым частым значением
for col in categorical_cols:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])


print("\nПропуски после обработки:")
print(df.isnull().sum())


# -------------------------------
# 3. Очистка текстовых данных
# -------------------------------

# Удаляем случайные пробелы
for col in categorical_cols:
    df[col] = df[col].str.strip()


# -------------------------------
# 4. Преобразование категорий
# -------------------------------

# Gender:
# Female -> 0
# Male -> 1
df["Gender"] = df["Gender"].map({
    "Female": 0,
    "Male": 1
})


# Output:
# No -> 0
# Yes -> 1
df["Output"] = df["Output"].map({
    "No": 0,
    "Yes": 1
})


# Feedback:
# Negative -> 0
# Positive -> 1
df["Feedback"] = df["Feedback"].map({
    "Negative": 0,
    "Positive": 1
})


# Monthly Income имеет естественный порядок,
# поэтому можно преобразовать в числа
df["Monthly Income"] = df["Monthly Income"].map({
    "No Income": 0,
    "Below Rs.10000": 1,
    "10001 to 25000": 2,
    "25001 to 50000": 3,
    "More than 50000": 4
})


# -------------------------------
# 5. One-Hot Encoding
# -------------------------------

# Эти признаки не имеют естественного числового порядка,
# поэтому используем One-Hot Encoding

ohe_cols = [
    "Marital Status",
    "Occupation",
    "Educational Qualifications",
    "Customer Type"
]

df = pd.get_dummies(
    df,
    columns=ohe_cols,
    drop_first=True,
    dtype=int
)


# -------------------------------
# 6. Нормализация
# -------------------------------

# Pin code нормализовать обычно нет смысла,
# так как это фактически идентификатор района.
normalize_cols = [
    "Age",
    "Family size",
    "latitude",
    "longitude"
]

for col in normalize_cols:

    min_value = df[col].min()
    max_value = df[col].max()

    if max_value != min_value:
        df[col] = (
            (df[col] - min_value)
            /
            (max_value - min_value)
        )


# -------------------------------
# 7. Результат
# -------------------------------

print("\nПервые строки после обработки:")
print(df.head())


print("\nТипы данных:")
print(df.dtypes)


print("\nМинимальные значения:")
print(df[normalize_cols].min())


print("\nМаксимальные значения:")
print(df[normalize_cols].max())


# -------------------------------
# 8. Сохранение
# -------------------------------

df.to_csv(
    "processed_online_food.csv",
    index=False
)

print("\nОбработанный файл сохранён:")
print("processed_online_food.csv")