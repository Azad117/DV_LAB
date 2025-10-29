from wordcloud import WordCloud
import matplotlib.pyplot as plt

details = "Visualization is the visual and interactive expploration and graphic representation of data of any type. This course cover data visualization concepts, practices and tools particularly for analyzing and presenting business data. Students will evaluate ,design,and,develop effective visualization and dashboards,using various development tools."
wordcloud = WordCloud(width=800, height=800, background_color='white',stopwords = [] ,min_font_size = 10).generate(details)

plt.figure(figsize = (5,5),facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()


#Output:

