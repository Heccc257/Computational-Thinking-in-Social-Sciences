import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import argparse 
import random
import graph_reader
import draw
import iteration
import os
parser = argparse.ArgumentParser(description='main')
parser.add_argument('--th1', default=3, type=int, help='三元闭包门槛')
parser.add_argument('--th2', default=2, type=int, help='社团闭包门槛')
parser.add_argument('--th3', default=2, type=int, help='会员闭包门槛')
parser.add_argument('--graph_path', default="graphs/example.gr", type=str, help='path to read')
parser.add_argument('--result_dir', default="./result/", type=str, help='path to store the results')
args = parser.parse_args()

result_dir = args.result_dir

if result_dir.endswith("/") == False:
    result_dir += '/'
th1, th2, th3 = args.th1, args.th2, args.th3
n, edges, clubs, members = graph_reader.read_gragh(args.graph_path, 2)

plt.ion() # 非阻塞模式

if os.path.exists(result_dir) == False:
    os.mkdir(result_dir)
epoch = 1

log = open(result_dir + "result.log", 'w', encoding='utf-8')

log.write("共有{}个点, {}条边\n".format(n, len(edges)))

draw.load_graph(n, edges, clubs, members)
plt.savefig(result_dir + "epoch_0" + ".jpg")
plt.show()
plt.close()
while True:
    # os.system("pause")
    ternary, community, membership, join, homo_coe = iteration.iterate(edges, clubs, members, th1, th2, th3)

    if len(ternary) + len(community) + len(membership) == 0:
        print("已经收敛，迭代结束")
        log.write("已经收敛，迭代结束")
        break

    edges = edges + ternary + community + membership

    draw.load_graph(n, edges, clubs, members)
    plt.savefig(result_dir + "epoch_" + str(epoch) + ".jpg")
    plt.show()
    plt.close()

    log.write("----- 第{}次迭代".format(epoch) + ': -----\n')
    print("----- 第{}次迭代: -----".format(epoch))


    log.write("三元闭包导致的新边:\n")
    log.write(str(ternary) + '\n')
    log.write("社团闭包导致的新边:\n")
    log.write(str(community) + '\n')
    log.write("会员闭包导致的新边:\n")
    log.write(str(membership) + '\n')
    
    log.write("参加社团的情况为:\n")
    log.write(str(join) + '\n')
    log.write("参加社团的情况为:\n")
    log.write(str(homo_coe) + '\n')
    epoch += 1
    log.write('\n')

log.close()