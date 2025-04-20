# Graph Theory Project: Misinformation Detection on Twitter

This project was developed as part of the course **"Teoria e Aplicação de Grafos"** (TAG) — University of Brasília (2025/1). Its main goal is to analyze social networks and identify potential fake news spreaders using classic graph algorithms.

## 🔍 Objective
Use real Twitter data to build a graph of interactions between users (mentions, retweets), and apply PageRank, community detection algorithms, and centrality measures to understand the network structure and detect influential nodes in the spread of misinformation.

## 🧰 Technologies and Libraries
- Python 3
- [NetworkX](https://networkx.org/) — for graph manipulation
- [Matplotlib](https://matplotlib.org/) — for visualization
- [Pandas](https://pandas.pydata.org/) — for data handling

## 📊 Results
- PageRank calculation to identify the most influential users
- Community detection using `greedy_modularity_communities`
- Graph visualization with node size proportional to PageRank and coloring by community

## ⚙️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/graph-fakenews.git
   cd graph-fakenews
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the notebook `main.ipynb`

## 📎 Data Sources
- [SNAP Twitter Data](https://snap.stanford.edu/data/twitter.tar.gz)
- [Fake News Dataset - Kaggle](https://www.kaggle.com/datasets/mrisdal/fake-news)

---
> Academic project — TAG/UnB 2025/1 ✨
