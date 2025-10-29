import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Fixed typo in 'saeborn'
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/testset.csv')
data.columns = data.columns.str.strip()
data['datetime_utc'] = pd.to_datetime(data['datetime_utc'])
data.set_index('datetime_utc', inplace=True)

plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x=data.index, y='_tempm')
plt.title("Line Graph of Temp Over Time")
plt.xlabel("Date")
plt.ylabel("Temp (°C)")
plt.grid(True)

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


data['_tempm'].fillna(data['_tempm'].mean(), inplace=True)
x = data.index.view(np.int64).reshape(-1, 1)
y = data['_tempm'].values
model = LinearRegression()
model.fit(x, y)
slope = model.coef_[0]
intercept = model.intercept_
plt.figure(figsize=(10, 6))
plt.scatter(data.index, data['_tempm'], label='Temperature Data', color='blue')
plt.plot(data.index, slope * x + intercept, color='red', label='Trend Line', linewidth=2, linestyle='-')
plt.title("Line Graph of Temp Over Time")
plt.xlabel("Date")
plt.ylabel("Temp (°C)")
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


monthly_mean_temp = data['_tempm'].resample('ME').mean()

monthly_mean_temp.plot(kind='area', color='skyblue', alpha=0.7)
plt.title('Monthly Mean Temperature in Chennai')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



#Output:


