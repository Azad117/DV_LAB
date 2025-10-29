import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
import networkx as nx

# Download required NLTK data packages
nltk.download('punkt_tab')
nltk.download('stopwords')

# Sample text
text = "Data analysis involves inspecting, cleansing, transforming, and modeling data with the goal of discovering useful information, informing conclusions, and supporting decision-making. Visualization is a crucial step in understanding patterns and trends in data. This course will cover the key concepts, best practices, and tools for effective data visualization and analysis.Students will learn to build interactive dashboards and reports using popular visualization libraries and platforms."

# Tokenize and preprocess
tokens = word_tokenize(text.lower())  # convert to lowercase and tokenize
stop_words = set(stopwords.words('english'))  # English stopwords set
filtered_tokens = [word for word in tokens if word not in stop_words]  # remove stopwords

# Generate bigrams from filtered tokens
bigrams = list(nltk.bigrams(filtered_tokens))

# Build graph based on bigrams containing the root word
root_word = "data"
G = nx.Graph()
for bigram in bigrams:
    if root_word in bigram:
        G.add_edge(bigram[0], bigram[1])

# Draw the bigram graph
plt.figure(figsize=(10, 8))
nx.draw_networkx(G, with_labels=True, node_color='skyblue', pos=nx.spring_layout(G))
plt.title("Bigram Graph")
plt.axis('off')
plt.show()



#Output:

