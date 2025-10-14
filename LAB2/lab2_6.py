dict = {"Зубенко Михаил": "10", "Чарльз Леклерк": "9", 
        "Леонель Пепси": "2", "Лена Комбаин": "2"}

current = None
max_value = -1

for i in dict:
    value = int(dict[i])
    if value > max_value:
        max_value = value
        current = i

print(f"{current}: {dict[current]}")
