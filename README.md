# Projeto de Grafos: Detecção de Desinformação no Twitter

Este projeto foi desenvolvido como parte da disciplina **Teoria e Aplicação de Grafos** (TAG) — Universidade de Brasília (2025/1), com o objetivo de analisar redes sociais e identificar potenciais espalhadores de fake news utilizando algoritmos clássicos de grafos.

## 🔍 Objetivo
Utilizar dados reais do Twitter para construir um grafo de interações entre usuários (menções, retweets), e aplicar algoritmos de PageRank, detecção de comunidades e medidas de centralidade para entender a estrutura da rede e detectar nós influentes na propagação de desinformação.

## 🧰 Tecnologias e Bibliotecas
- Python 3
- [NetworkX](https://networkx.org/) — para manipulação de grafos
- [Matplotlib](https://matplotlib.org/) — para visualização
- [Pandas](https://pandas.pydata.org/) — para manipulação de dados

## 📊 Resultados
- Cálculo de PageRank para identificar usuários mais influentes
- Detecção de comunidades usando `greedy_modularity_communities`
- Visualização do grafo com tamanho dos nós proporcional ao PageRank e coloração por comunidade


## 📎 Fontes de Dados
- [SNAP Twitter Data](https://snap.stanford.edu/data/twitter.tar.gz)
- [Fake News Dataset - Kaggle](https://www.kaggle.com/datasets/mrisdal/fake-news)

---
> Projeto desenvolvido para fins acadêmicos — TAG/UnB 2025/1 ✨
