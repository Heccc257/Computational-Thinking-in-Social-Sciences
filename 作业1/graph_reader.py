import matplotlib.pyplot as plt
import os

def read_gragh(graph_path, club_num=0):
    n = 0
    edges = []
    with open(graph_path, "r") as f:
        n = int(f.readline())
        edges = eval(f.readline())
    
    members = [i + 1 for i in range(n - club_num)]
    clubs = [i + 1 + len(members) for i in range(club_num)]

    return n, edges, clubs, members
