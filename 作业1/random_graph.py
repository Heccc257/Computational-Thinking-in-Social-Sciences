import argparse 
import random

parser = argparse.ArgumentParser(description='generate a random graph')
parser.add_argument('--nodes', default=10, type=int, help='number of nodes')
parser.add_argument('--edges', default=30, type=int, help='number of edges')
parser.add_argument('--graph_name', default="tem_graph", type=str, help='path to store the graph')
args = parser.parse_args()


# if __name__ == "__main__":

# print(args.nodes)
n = args.nodes
edges = [(i+1, j+1) for i in range(n) for j in range(i+1, n)]
# print(edges)

random.shuffle(edges)
edges = edges[0: args.edges]
# print(edges)

with open("graphs\\" + args.graph_name + ".gr", "w") as f:
    f.write(str(n) + '\n')
    f.write(str(edges))
    
# python .\random_graph.py --nodes 20 --edges 40 --graph_path example.gr