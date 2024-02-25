import matplotlib.pyplot as plt
import networkx as nx

# グラフの隣接行列を定義
graph = [
    [0, 7, float('inf'), 8],
    [float('inf'), 0, 5, float('inf')],
    [float('inf'), float('inf'), 0, 2],
    [float('inf'), float('inf'), float('inf'), 0]
]
MAX_LENGTH = len(graph[0])

# グラフオブジェクトの作成
G = nx.DiGraph()

# ノードを追加
for node in range(MAX_LENGTH):
    G.add_node(node)

# エッジを追加
for i in range(MAX_LENGTH):
    for j in range(MAX_LENGTH):
        if graph[i][j] != float('inf') and graph[i][j] != 0:
            G.add_edge(i, j, weight=graph[i][j])

# グラフの描画
pos = nx.spring_layout(G)  # ノードの位置を決定
edge_labels = nx.get_edge_attributes(G, 'weight')  # エッジの重みを取得

# ノードとエッジを描画
nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='k', width=2, linewidths=1, font_size=15, arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# 表示
plt.axis('off')  # 軸を非表示にする
plt.show()
