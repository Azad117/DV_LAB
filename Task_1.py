import pandas as pd
import numpy as np

a = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/plant_disease_data.csv")
print(a)

sh = a.shape
print(sh)
a.info()
a.describe()
print(a.head())
pd.isna(a).sum()
a.dropna()
a.duplicated()
a.drop_duplicates()



#Output:
       Plant_ID Plant_Type Leaf_Color  Leaf_Spot_Size  Humidity  Temperature  \
0     PLANT_0001       Corn      Brown            3.80     69.49        30.68   
1     PLANT_0002     Potato      Brown            6.96     45.72        34.57   
2     PLANT_0003       Corn     Yellow            3.08     86.21        29.29   
3     PLANT_0004       Rice     Yellow            0.50     87.46        16.71   
4     PLANT_0005       Rice      Green            1.58     43.38        26.23   
...          ...        ...        ...             ...       ...          ...   
2495  PLANT_2496       Rice      Green            9.10     52.27        29.90   
2496  PLANT_2497      Wheat      Brown            7.10     75.40        31.62   
2497  PLANT_2498      Wheat      Green            9.53     47.66        23.76   
2498  PLANT_2499       Rice      Brown            6.77     73.22        18.53   
2499  PLANT_2500     Potato     Yellow            9.00     72.87        27.76   

        Disease_Status  
0       Mild Infection  
1       Mild Infection  
2              Healthy  
3              Healthy  
4     Severe Infection  
...                ...  
2495           Healthy  
2496    Mild Infection  
2497           Healthy  
2498    Mild Infection  
2499    Mild Infection  

[2500 rows x 7 columns]
(2500, 7)
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2500 entries, 0 to 2499
Data columns (total 7 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   Plant_ID        2500 non-null   object 
 1   Plant_Type      2500 non-null   object 
 2   Leaf_Color      2500 non-null   object 
 3   Leaf_Spot_Size  2500 non-null   float64
 4   Humidity        2500 non-null   float64
 5   Temperature     2500 non-null   float64
 6   Disease_Status  2500 non-null   object 
dtypes: float64(3), object(4)
memory usage: 136.8+ KB
     Plant_ID Plant_Type Leaf_Color  Leaf_Spot_Size  Humidity  Temperature  \
0  PLANT_0001       Corn      Brown            3.80     69.49        30.68   
1  PLANT_0002     Potato      Brown            6.96     45.72        34.57   
2  PLANT_0003       Corn     Yellow            3.08     86.21        29.29   
3  PLANT_0004       Rice     Yellow            0.50     87.46        16.71   
4  PLANT_0005       Rice      Green            1.58     43.38        26.23   

     Disease_Status  
0    Mild Infection  
1    Mild Infection  
2           Healthy  
3           Healthy  
4  Severe Infection  
Plant_ID	Plant_Type	Leaf_Color	Leaf_Spot_Size	Humidity	Temperature	Disease_Status
0	PLANT_0001	Corn	Brown	3.80	69.49	30.68	Mild Infection
1	PLANT_0002	Potato	Brown	6.96	45.72	34.57	Mild Infection
2	PLANT_0003	Corn	Yellow	3.08	86.21	29.29	Healthy
3	PLANT_0004	Rice	Yellow	0.50	87.46	16.71	Healthy
4	PLANT_0005	Rice	Green	1.58	43.38	26.23	Severe Infection
...	...	...	...	...	...	...	...
2495	PLANT_2496	Rice	Green	9.10	52.27	29.90	Healthy
2496	PLANT_2497	Wheat	Brown	7.10	75.40	31.62	Mild Infection
2497	PLANT_2498	Wheat	Green	9.53	47.66	23.76	Healthy
2498	PLANT_2499	Rice	Brown	6.77	73.22	18.53	Mild Infection
2499	PLANT_2500	Potato	Yellow	9.00	72.87	27.76	Mild Infection
2500 rows × 7 columns
