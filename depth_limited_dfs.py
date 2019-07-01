graph = {"Oradea":{"Zerind":71,"Sibiu":151},"Zerind":{"Oradea":71,"Arad":75},"Arad":{"Zerind":75,"Sibiu":140,"Timisoara":118},"Timisoara":{"Arad":118,"Lugoj":111},"Lugoj":{"Timisoara":111,"Mehadia":70},"Mehadia":{"Lugoj":70,"Dobreta":75},"Dobreta":{"Mehadia":75,"Craiova":120},"Craiova":{"Dobreta":120,"Rimnicu Vilcea":146,"Pitesti":138},"Sibiu":{"Arad":140,"Oradea":151,"Rimnicu Vilcea":80,"Fagaras":99},"Rimnicu Vilcea":{"Sibiu":80,"Craiova":146,"Pitesti":97},"Fagaras":{"Sibiu":99,"Bucharest":211},"Pitesti":{"Bucharest":101,"Rimnicu Vilcea":97,"Craiova":138},"Bucharest":{"Fagaras":211,"Pitesti":101,"Giurgiu":90,"Urziceni":85},"Giurgiu":{"Bucharest":90},"Urziceni":{"Bucharest":85,"Hirsova":98,"Vaslui":142},"Hirsova":{"Urziceni":98,"Eforie":86},"Eforie":{"Hirsova":86},"Vaslui":{"Urziceni":142,"Iasi":92},"Iasi":{"Vaslui":92,"Neamt":87},"Neamt":{"Iasi":87}}
start, goal = 'Arad', 'Bucharest'

fringe, visited, parent = [], [], {}
maxDeepth=int(input("Enter maximum deepth: "))

fringe.append((start, 0))
visited.append(start)
parent[start] = None

found=False
while len(fringe) > 0:
    u, d = fringe[-1]
    del fringe[-1]
    adjDict = graph[u]
    if d >= maxDeepth:
        continue
    for v in adjDict.keys():
        if v not in visited:
            visited.append(v)
            parent[v] = u
            if v == goal:
                found=True
                break
            fringe.append((v, d + 1))
    if found:
        break
        
if goal not in parent.keys():
    print('Cutoff, cannot find with depth limit = ', maxDeepth)
else:
    dist, curr, path = 0, goal, []
    path.append(curr)
    while parent[curr] != None:
        path.append(parent[curr])
        dist = dist + graph[curr][parent[curr]]
        curr = parent[curr]
        
    path.reverse()
    print("Path: ", end=" ")
    for x in path:
        print(x, end=" ")
    print("\nDistance: ", dist)