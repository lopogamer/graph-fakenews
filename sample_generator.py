import pandas as pd

# Carregar o arquivo original
df = pd.read_csv('csv_files/twitter_network.csv')

# Criar uma amostra aleatória de 500 interações
df_sample = df.sample(n=500, random_state=42)

# Salvar como novo CSV
df_sample.to_csv('csv_files/twitter_network_sample.csv', index=False)