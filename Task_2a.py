import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/sentimentdataset.csv')
platform_likes_top5 = df.groupby("Platform")['Likes'].sum().sort_values(ascending=False).head(5)
plt.figure(figsize = (4,4))
platform_likes_top5.plot(kind='pie',autopct = '%1.1f%%',startangle=140,colors=['Skyblue','lightgreen','lightcoral','lightsalmon','lightsteelblue'])

plt.title('Top 5 Platforms by Total Likes')
plt.ylabel("")
plt.show()


top5_countries = df.nlargest(5,'Likes')
plt.figure(figsize = (10,6))
plt.bar(top5_countries['Country'],top5_countries['Likes'],color=['skyblue','lightcoral','lightgreen','lightsalmon','lightsteelblue'])
plt.xlabel('Country')
plt.ylabel('Total Likes')
plt.title('Top 5 Countries by Total Likes')
plt.show()

data={
    'Text':['Enjoying a beautiful day at the Park','Traffic was terrible this morning','Just Finished an amazing workout','Excited about the upcoming weekend gateway','Trying out a new recipe for dinner tonight'],
    'Retweets':[15,5,20,8,12],
    'Likes':[30,20,40,15,25]

}
df = pd.DataFrame(data)
sns.set(style='whitegrid')
plt.figure(figsize=(10,6))
sns.scatterplot(x='Retweets',y='Likes',data = df,color='blue',alpha=0.7)
plt.title("Scatter Plot of Retweets vs Likes")
plt.show()



#Output:

