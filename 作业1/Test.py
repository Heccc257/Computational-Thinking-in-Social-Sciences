import networkx as nx
import matplotlib.pyplot as plt

# 创建一个有向图
G = nx.Graph()

# 添加节点
G.add_nodes_from([1, 2, 3, 4, 5])

# 添加边
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# 定义节点的颜色和形状
node_colors = ["red", "blue", "green", "yellow", "red"]

# 绘制图形
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color=node_colors)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)

# 显示图形
plt.show()
