import numpy as np
import matplotlib.pyplot as plt
import math

a = np.linspace(0, 5, 100)

z1 = 2 * np.sin(3*math.pi - 2*a)**2 * np.cos(5*math.pi + 2*a)**2
z2 = 1/4 - 1/4 * np.sin(5/2*math.pi - 8*a)

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(a, z1, color='blue', linewidth=2, label='z1')
ax1.set_xlabel('a (радианы)', fontsize=12)
ax1.set_ylabel('z1', color='blue', fontsize=12)
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.plot(a, z2, color='red', linestyle='--', linewidth=2, label='z2')
ax2.set_ylabel('z2', color='red', fontsize=12)
ax2.tick_params(axis='y', labelcolor='red')

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='center left', bbox_to_anchor=(1.05, 0.5), fontsize=11)

plt.title('Графики функций z1 и z2', fontsize=14, fontweight='bold')
ax1.grid(True, linestyle=':', alpha=0.7)

plt.savefig('lab4_1.png', dpi=1000)

plt.tight_layout()

plt.show()
