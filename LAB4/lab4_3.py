import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
np.random.seed(42) 
data_matrix = np.random.rand(10, 10)


plt.figure(figsize=(10, 8))

sns.heatmap(
    data_matrix,
    annot=True,          
    fmt='.2f',           
    cmap='viridis',
    linewidths=0.5,
    linecolor='black',
    cbar=True
)

plt.title('Тепловая карта матрицы 10x10 случайных чисел со значениями', fontsize=14)
plt.xlabel('Столбцы', fontsize=12)
plt.ylabel('Строки', fontsize=12)
plt.savefig('lab4_3.png', dpi=1000)
plt.show()