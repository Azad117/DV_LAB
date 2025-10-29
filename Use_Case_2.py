import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/startup.csv")

df['Amount_Million'] = pd.to_numeric(df['Amount_Million'], errors='coerce').fillna(0)

df['YearMonth'] = pd.to_datetime(df['Year'].astype(str) + "-01-01")

top10 = df.sort_values(by='Amount_Million', ascending=False).head(10).copy()

best_startup = top10.iloc[0]['Startup']
worst_startup = top10.iloc[-1]['Startup']
avg_funding = top10['Amount_Million'].mean().round(2)

print("\n=== Top 10 Startups by Total Funding (in Million USD) ===")
print(top10[['Startup', 'Amount_Million']].to_string(index=False))

print("\n=== Summary Metrics ===")
print(f"Highest Funded Startup : {best_startup}")
print(f"Lowest Funded Startup  : {worst_startup}")
print(f"Average Funding (Top 10): {avg_funding} Million USD")

plt.figure(figsize=(10,6))
plt.bar(top10['Startup'], top10['Amount_Million'], color='skyblue')
plt.title("Top 10 Startups by Total Funding (Million USD)")
plt.xlabel("Startup")
plt.ylabel("Total Funding (Million USD)")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))
for startup in top10['Startup']:
    temp = df[df['Startup'] == startup]
    plt.plot(temp['YearMonth'], temp['Amount_Million'], marker='o', linewidth=2, label=startup)
plt.title("Funding Trend for Top 10 Startups")
plt.xlabel("Year")
plt.ylabel("Funding (Million USD)")
plt.legend(fontsize='small', ncol=2)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()


industries = top10.groupby('Industry').size()
plt.figure(figsize=(6,6))
plt.pie(industries, labels=industries.index, autopct='%1.1f%%', startangle=140)
plt.title("Industry Distribution among Top 10 Startups")
plt.tight_layout()
plt.show()



#Output:


=== Top 10 Startups by Total Funding (in Million USD) ===
    Startup  Amount_Million
QuantumLeap            20.0
  DeepScale            19.0
    FinWave            13.0
    MetaLab            11.5
  JetStream            11.0
  NeuroPath            10.0
  InnoSpace             9.0
  PlatformX             6.2
    SafeNet             5.4
     AeroAI             5.0

=== Summary Metrics ===
Highest Funded Startup : QuantumLeap
Lowest Funded Startup  : AeroAI
Average Funding (Top 10): 11.01 Million USD
