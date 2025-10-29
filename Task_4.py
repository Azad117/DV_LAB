import pandas as pd
import matplotlib.pyplot as plt
from joypy import joyplot
import seaborn as sns

df = pd.read_csv('student-mat.csv')
print(df.head())

avg_grade_by_mjob = df.groupby('Mjob')['G3'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(avg_grade_by_mjob.index, avg_grade_by_mjob.values, color='skyblue')
plt.xlabel('Mother\'s Job')
plt.ylabel('Average Final Grade (G3)')
plt.title('Average Final Grade by Mother\'s Job')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

categorical_column = 'Mjob'
continuous_column = 'G3'
plt.figure(figsize=(12, 8))
sns.kdeplot(data=df, x=continuous_column, hue=categorical_column, fill=True, common_norm=False)
plt.xlabel('Final Grade (G3)')
plt.title(f'Kernel Density Plot of {continuous_column} by {categorical_column}')
plt.legend(title=categorical_column)
plt.show()

categorical_column = 'Mjob'
continuous_column = 'G3'
plt.figure(figsize=(12, 8))
sns.violinplot(data=df, x=categorical_column, y=continuous_column)
plt.xlabel(categorical_column)
plt.ylabel('Final Grade (G3)')
plt.title(f'Violin Plot for {continuous_column} by {categorical_column}')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

categorical_column = 'Mjob'
continuous_column = 'G3'

plt.figure(figsize=(12, 8))
joyplot(
    data=df,
    by=categorical_column,
    column=continuous_column,
    kind='kde',
    fill=True,
    linecolor="black",
    grid=True,
    linewidth=1,
    legend=True,
)

plt.xlabel('Final Grade (G3)')
plt.title(f'Ridgeline Plot for {continuous_column} by {categorical_column}')
plt.show()

sns.lmplot(data=df, x='age', y='G3', height=6, line_kws={'color': 'red'})

plt.title('Scatter Plot with Fit Line: Age vs Final Grade')
plt.xlabel('Age')
plt.ylabel('Final Grade (G3)')
plt.show()



#output:

  school sex  age address famsize Pstatus  Medu  Fedu     Mjob      Fjob  ...  \
0     GP   F   18       U     GT3       A     4     4  at_home   teacher  ...   
1     GP   F   17       U     GT3       T     1     1  at_home     other  ...   
2     GP   F   15       U     LE3       T     1     1  at_home     other  ...   
3     GP   F   15       U     GT3       T     4     2   health  services  ...   
4     GP   F   16       U     GT3       T     3     3    other     other  ...   

  famrel freetime  goout  Dalc  Walc health absences  G1  G2  G3  
0      4        3      4     1     1      3        6   5   6   6  
1      5        3      3     1     1      3        4   5   5   6  
2      4        3      2     2     3      3       10   7   8  10  
3      3        2      2     1     1      5        2  15  14  15  
4      4        3      2     1     2      5        4   6  10  10  
