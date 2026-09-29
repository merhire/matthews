import pandas as pd

df = pd.read_csv("XAU_15m_data.csv", sep=";")

print(df.head())

print("\nКоличество пропущенных значений:")
print(df.isnull().sum())

numeric_cols = ["Open", "High", "Low", "Close", "Volume"]

# Заполнение пропусков медианой
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Если вдруг есть пропуски в Date
if df["Date"].isnull().any():
    df["Date"] = df["Date"].fillna(df["Date"].mode()[0])

print("\nПропуски после заполнения:")
print(df.isnull().sum())



df["Date"] = pd.to_datetime(
    df["Date"],
    format="%Y.%m.%d %H:%M"
)
df["year"] = df["Date"].dt.year
df["month"] = df["Date"].dt.month
df["day"] = df["Date"].dt.day
df["hour"] = df["Date"].dt.hour
df["minute"] = df["Date"].dt.minute

for col in numeric_cols:

    min_value = df[col].min()
    max_value = df[col].max()

    df[col] = (
        (df[col] - min_value)
        /
        (max_value - min_value)
    )


processed_df = df.drop(columns=["Date"])

print("\nПервые строки после обработки:")
print(processed_df.head())

print("\nМинимальные значения:")
print(processed_df[numeric_cols].min())

print("\nМаксимальные значения:")
print(processed_df[numeric_cols].max())

processed_df.to_csv(
    "processed_xau_15m.csv",
    index=False
)
