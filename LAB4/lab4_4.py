import matplotlib.pyplot as plt
import numpy as np

items = ['Огурцы', 'Помидоры', 'Гранаты', 'Пистолеты']
quantities = [85, 120, 50, 15]

colors = ['#66BB6A', '#EF5350', '#EC407A', '#78909C']

fig, ax = plt.subplots(figsize=(10, 6))

y_pos = np.arange(len(items))

bars = ax.barh(y_pos, quantities, color=colors, edgecolor='black', linewidth=1.2)

for bar in bars:
    width = bar.get_width()
    ax.text(width + 3, bar.get_y() + bar.get_height()/2, f'{width}',
            ha='left', va='center', fontsize=10, color='black', weight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(items, fontsize=12, weight='bold')
ax.set_xlabel('Условные Единицы', fontsize=12, weight='bold')
ax.set_title('Наличие различных предметов', fontsize=16, weight='bold', color='#333333')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

ax.set_xlim(0, max(quantities) * 1.2)

ax.xaxis.grid(True, linestyle='--', alpha=0.6)

plt.savefig('lab4_4.png', dpi=1000)
plt.tight_layout()
plt.show()