import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/department_performance_2024.csv")

df.set_index('Month', inplace=True)
yearly_avg = df.mean().round(2).sort_values(ascending=False)
best_month = df.idxmax()
worst_month = df.idxmin()
monthly_changes = df.diff().round(2)


print("\n=== Yearly Average Performance (Descending) ===")
print(yearly_avg)
print("\n=== Best and Worst Month per Department ===")
for dept in df.columns:
    print(f"{dept}: Best = {best_month[dept]},  Worst = {worst_month[dept]}")



plt.figure(figsize=(10,6))
for dept in df.columns:
    plt.plot(df.index, df[dept], marker='o', linewidth=2, label=dept)
plt.title("Monthly Performance by Department")
plt.xlabel("Month")
plt.ylabel("Performance Score (0-100)")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
plt.bar(yearly_avg.index, yearly_avg.values)
plt.title("Average Yearly Performance by Department")
plt.xlabel("Department")
plt.ylabel("Average Performance Score (0-100)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()



#Output:

=== Yearly Average Performance (Descending) ===
Sales        70.30
Finance      57.68
Marketing    54.05
R&D          49.08
HR           46.83
dtype: float64

=== Best and Worst Month per Department ===
Sales: Best = Dec-2024,  Worst = Jan-2024
Marketing: Best = Dec-2024,  Worst = Feb-2024
HR: Best = Dec-2024,  Worst = Jan-2024
Finance: Best = Dec-2024,  Worst = Feb-2024
R&D: Best = Dec-2024,  Worst = Feb-2024
