import networkx as nx

def load_graph(n, edges, clubs, members):

    G = nx.Graph()
    # 添加节点
    G.add_nodes_from([i for i in range(1, n+1)])

    # 添加边
    G.add_edges_from(edges)

    # 定义节点的颜色和形状
    node_colors = []
    for i in members: node_colors.append("yellow")
    for i in clubs: node_colors.append("red")

    pos = nx.kamada_kawai_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color=node_colors)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
