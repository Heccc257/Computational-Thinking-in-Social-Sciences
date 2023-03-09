
def all_edges(maps, members, x):
    ans = 0
    for i in members:
        ans += (i != x and maps[x][i] == True)
    return ans

def homo_edges(maps, members, join, x):
    ans = 0
    for i in members:
        # print("homo_edges", i, x, maps[x][i])
        if i != x and maps[x][i] == True and join[i] == join[x]:
            ans += 1
    return ans

def calc(maps, clubs, members):
    join = {}
    for m in members: join[m] = ""
    
    for c in clubs:
        for m in members:
            if maps[c][m] == True:
                join[m] = join[m] + str(c) + "," 
    # print(join)
    homo_coe = {}
    for x in members:
        # print(x, homo_edges(maps, members, join, x), all_edges(maps, members, x))
        try:
            homo_coe[x] = 1.0 * homo_edges(maps, members, join, x) / all_edges(maps, members, x)
        except:
            homo_coe[x] = 0
    # print(homo_coe)
    # exit(0)
    return join, homo_coe
