import pandas as pd

df = pd.read_csv("cars_dataset.csv")
print(df.head(10))
print(df.info())
print(df.isnull().sum())

driver_code_mode = df["driver_code"].mode()[0]
df["driver_code"] = df["driver_code"].fillna(driver_code_mode)

car_number_mode = df["car_number"].mode()[0]
df["car_number"] = df["car_number"].fillna(car_number_mode)

finish_position_median = df["finish_position"].median()
df["finish_position"] = df["finish_position"].fillna(finish_position_median)

speed_mean = df["fastest_lap_speed_kph"].mean()
df["fastest_lap_speed_kph"] = df["fastest_lap_speed_kph"].fillna(speed_mean)

print(df.isnull().sum())