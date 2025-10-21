import matplotlib.pyplot as plt
import numpy as np

categories = ['Технологии', 'Спорт', 'Искусство', 'Путешествия', 'Еда']
preferences = [30, 15, 25, 20, 10]


fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(
    preferences,
    labels=categories,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'edgecolor': 'black'}
)

ax.set_title('Предпочтения пользователей по категориям', fontsize=16)

ax.axis('equal') 

plt.setp(autotexts, size=10, weight="bold", color="white")
plt.savefig('lab4_2.png', dpi=1000)
plt.show()