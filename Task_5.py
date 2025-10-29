import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/creditcard.csv')
print(df)


numeric_subset = df[['Age', 'Debt', 'YearsEmployed']]
sns.pairplot(numeric_subset)
plt.show()

attributes = ["Age", "Debt", "CreditScore"]
fig = px.parallel_coordinates(df, color="Approved", dimensions=attributes,color_continuous_scale=px.colors.diverging.Tealrose,color_continuous_midpoint=0.5)
fig.show()


first_20_entries = df.head(20)
age = first_20_entries['Age']
debt = first_20_entries['Debt']
credit_score = first_20_entries['CreditScore']
plt.figure(figsize=(10, 6))
plt.plot(age, debt, label='Debt', color='blue')
plt.plot(age, credit_score, label='Credit Score', color='green')
plt.xlabel('Age')
plt.ylabel('Value')
plt.title('Line Graph: Age, Debt, and Credit Score')
plt.legend()
plt.grid(True)
plt.show()

grouped_data = first_20_entries.groupby('Age').sum()[['Debt', 'CreditScore']]
grouped_data.plot(kind='bar', stacked=True, figsize=(12, 8))
plt.xlabel('Age')
plt.ylabel('Value')
plt.title('Stacked Bar Chart: Debt and Credit Score by Age')
plt.legend(title='Attribute')
plt.show()



#Output:

     Gender    Age    Debt  Married  BankCustomer         Industry Ethnicity  \
0         1  30.83   0.000        1             1      Industrials     White   
1         0  58.67   4.460        1             1        Materials     Black   
2         0  24.50   0.500        1             1        Materials     Black   
3         1  27.83   1.540        1             1      Industrials     White   
4         1  20.17   5.625        1             1      Industrials     White   
..      ...    ...     ...      ...           ...              ...       ...   
685       1  21.08  10.085        0             0        Education     Black   
686       0  22.67   0.750        1             1           Energy     White   
687       0  25.25  13.500        0             0       Healthcare    Latino   
688       1  17.92   0.205        1             1  ConsumerStaples     White   
689       1  35.00   3.375        1             1           Energy     Black   

     YearsEmployed  PriorDefault  Employed  CreditScore  DriversLicense  \
0             1.25             1         1            1               0   
1             3.04             1         1            6               0   
2             1.50             1         0            0               0   
3             3.75             1         1            5               1   
4             1.71             1         0            0               0   
..             ...           ...       ...          ...             ...   
685           1.25             0         0            0               0   
686           2.00             0         1            2               1   
687           2.00             0         1            1               1   
688           0.04             0         0            0               0   
689           8.29             0         0            0               1   

          Citizen  ZipCode  Income  Approved  
0         ByBirth      202       0         1  
1         ByBirth       43     560         1  
2         ByBirth      280     824         1  
3         ByBirth      100       3         1  
4    ByOtherMeans      120       0         1  
..            ...      ...     ...       ...  
685       ByBirth      260       0         0  
686       ByBirth      200     394         0  
687       ByBirth      200       1         0  
688       ByBirth      280     750         0  
689       ByBirth        0       0         0  

