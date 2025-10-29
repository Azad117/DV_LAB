import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import squarify
import plotly.express as px

df=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/USA_cars_datasets.csv')
print(df)

brand_total_price = df.groupby('brand')['price'].sum().reset_index()
plt.figure(figsize=(18, 12))
squarify.plot(sizes=brand_total_price['price'], label=brand_total_price['brand'], alpha=0.4)
plt.axis('off')
plt.title('Tree Map of Total Price by Brand')
plt.show()

sunburst_data = df.groupby(['brand', 'model']).sum().reset_index()
fig = px.sunburst(sunburst_data, path=['brand', 'model'], values='price', title='Sunburst Display of Total Price by Brand and Model')
fig.show()


#Output:

      Unnamed: 0  price      brand    model  year   title_status   mileage  \
0              0   6300     toyota  cruiser  2008  clean vehicle  274117.0   
1              1   2899       ford       se  2011  clean vehicle  190552.0   
2              2   5350      dodge      mpv  2018  clean vehicle   39590.0   
3              3  25000       ford     door  2014  clean vehicle   64146.0   
4              4  27700  chevrolet     1500  2018  clean vehicle    6654.0   
...          ...    ...        ...      ...   ...            ...       ...   
2494        2494   7800     nissan    versa  2019  clean vehicle   23609.0   
2495        2495   9200     nissan    versa  2018  clean vehicle   34553.0   
2496        2496   9200     nissan    versa  2018  clean vehicle   31594.0   
2497        2497   9200     nissan    versa  2018  clean vehicle   32557.0   
2498        2498   9200     nissan    versa  2018  clean vehicle   31371.0   

       color                  vin        lot       state country  \
0      black    jtezu11f88k007763  159348797  new jersey     usa   
1     silver    2fmdk3gc4bbb02217  166951262   tennessee     usa   
2     silver    3c4pdcgg5jt346413  167655728     georgia     usa   
3       blue    1ftfw1et4efc23745  167753855    virginia     usa   
4        red    3gcpcrec2jg473991  167763266     florida     usa   
...      ...                  ...        ...         ...     ...   
2494     red    3n1cn7ap9kl880319  167722715  california     usa   
2495  silver    3n1cn7ap5jl884088  167762225     florida     usa   
2496  silver    3n1cn7ap9jl884191  167762226     florida     usa   
2497   black    3n1cn7ap3jl883263  167762227     florida     usa   
2498  silver    3n1cn7ap4jl884311  167762228     florida     usa   

          condition  
0      10 days left  
1       6 days left  
2       2 days left  
3     22 hours left  
4     22 hours left  
...             ...  
2494    1 days left  
2495  21 hours left  
2496  21 hours left  
2497    2 days left  
2498  21 hours left  

[2499 rows x 13 columns]
