import gzip
import csv
import networkx as nx
import pandas as pd


#Código para gerar a partir do twitter_combined.txt.gz o twitter_network.csv

input_path = "data/twitter_combined.txt.gz"
output_path = "csv_files/twitter_network.csv"

with gzip.open(input_path, 'rt') as infile, open(output_path, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['source', 'target'])  # Cabeçalho do CSV
    for line in infile:
        nodes = line.strip().split()
        if len(nodes) == 2:
            writer.writerow(nodes)

print(f"Arquivo CSV salvo como {output_path}")