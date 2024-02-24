G = nx.DiGraph() # 空の有向グラフ生成

# 重み付きグラフの生成
nodes = [1, 2, 3, 4] # ノード
edges = [(1, 2, 8), (1, 3, -3), (2, 1, 5), (2, 4, 2), (3, 2, 4), (4, 3, 1)]

G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

# 各ノードの座標
pos = {1:(0,1), 2:(1,1), 3:(0,0), 4:(1,0)}

# 重み（距離）の表示
#nx.draw_networkx_edge_labels(G, pos)

# 重みのみの表示
edge_labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)

# 描画
nx.draw(G, pos, with_labels=True)