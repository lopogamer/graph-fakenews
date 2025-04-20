import gzip
import csv
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

#CSV files
CSV_FILE = 'csv_files/twitter_network.csv'
CSV_FILE_SAMPLE = 'csv_files/twitter_network_sample.csv'

# Load dataset (format: source, target)
df = pd.read_csv(CSV_FILE_SAMPLE)
g = nx.DiGraph()

# Adicionar arestas com peso baseado na frequência de interação
for _, row in df.iterrows():
    u = row['source']
    v = row['target']
    if g.has_edge(u, v):
        g[u][v]['weight'] += 1
    else:
        g.add_edge(u, v, weight=1)


print(f'Nodes {g.number_of_nodes()}')
print(f'Edges {g.number_of_edges()}')

# PageRank
pagerank = nx.pagerank(g, alpha=0.85)

# Top 10 nós mais influentes segundo PageRank
top_10 = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:10]
print("Top 10 nós mais influentes (PageRank):")
for i, (node, score) in enumerate(top_10, 1):
    print(f"{i}. {node} - Score: {score:.6f}")

# Detecção de comunidades
from networkx.algorithms.community import greedy_modularity_communities
communities = greedy_modularity_communities(g)

# Desenhar o grafo
plt.figure(figsize=(10, 7))
nx.draw(g, with_labels=False, node_size=20)
plt.show()
