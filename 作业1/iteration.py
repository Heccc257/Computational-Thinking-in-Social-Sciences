
import homogenization

def count_share_members(a, b, maps, tags):
    count = 0
    for item in tags:
        if item != a and item != b \
            and maps[a][item] == True and maps[b][item] == True:
            count += 1
    return count

def iterate(edges, clubs, members, th1, th2, th3):
    # print(members)
    maps = [
        [0 for i in range(len(members) + len(clubs) + 1)] for i in range(len(members) + len(clubs) + 1)
    ]
    for (a, b) in edges:
        maps[a][b] = maps[b][a] = 1

    # 三元闭包
    ternary = []
    for i in members:
        for j in members:
            if i >= j or maps[i][j] == True: continue
            if count_share_members(i, j, maps, members) >= th1:
                ternary.append((i, j))
    # print(ternary)

    # 社团闭包
    community = []
    for i in members:
        for j in members:
            if i >= j or maps[i][j] == True: continue
            if count_share_members(i, j, maps, clubs) >= th2:
                community.append((i, j))
    # print(community)

    # 会员闭包
    membership = []
    for c in clubs:
        for i in members:
            if maps[i][c] == True: continue
            if count_share_members(c, i, maps, members) >= th3:
                membership.append((c, i))
    # print(membership)

    join, homo_coe = homogenization.calc(maps, clubs, members)

    return ternary, community, membership, join, homo_coe