import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Employee.csv')
categorical_column = 'Gender'
category_counts = df[categorical_column].value_counts()
plt.pie(category_counts,labels = category_counts.index,autopct = '%1.1f%%',startangle=90,colors=['skyblue','lightcoral'])
plt.title(f'Pie Chart of{categorical_column}')
plt.axis('equal')
plt.show()

categorical_column = 'City'
category_counts = df[categorical_column].value_counts()
plt.bar(category_counts.index,category_counts.values,color=['skyblue','lightcoral','lightgreen','lightsalmon','lightsteelblue'])
plt.title(f'Bar Chart of {categorical_column}')
plt.xlabel(categorical_column)
plt.ylabel('Count')
plt.show()

continuous_column = 'Age'
plt.hist(df[continuous_column], bins=10, edgecolor='black')
plt.title(f'{continuous_column} Distribution')
plt.xlabel(continuous_column)
plt.ylabel('Frequency')
plt.show()


sns.kdeplot(df[continuous_column], fill=True)
plt.title(f'Density Plot of {continuous_column}')
plt.xlabel(continuous_column)
plt.ylabel('Density')
plt.show()

continuous_column = 'JoiningYear'
sns.rugplot(df[continuous_column], height=0.5)
plt.title(f'Rug Plot of {continuous_column}')
plt.xlabel(continuous_column)
plt.yticks([])
plt.show()


#Output:
