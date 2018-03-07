#Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    #write your code here
    n = len(adj)

    dist = [65535 for _ in range(n)]
    dist[s] = 0

    final = [0 for _ in range(n)]
    final[s] = 1

    pre = [0 for _ in range(n)]
    
    q = 0
    for i in adj[s]:
        
        dist[i] = cost[s][q]
        q = q+1
    w = -1
    for i in range(n-1):
        mintemp = 65535
        for j in range(n):
            if final[j]==0 and dist[j]<mintemp:
                w = j
                mintemp = dist[j]
        if w ==-1:
            return -1
        final[w] = 1
        
        for k in range(n):
            if final[k]==0 and (k in adj[w]):
                if mintemp+cost[w][adj[w].index(k)] < dist[k]:
                    dist[k] = mintemp+cost[w][adj[w].index(k)]
                    pre[k] = [w]
    if dist[t] != 65535:
        return dist[t]
    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    '''adj = [[1], [2], [3], [4], [5], [6], [7], [8], [9], []]
    cost = [[1], [1], [1], [1], [1], [1], [1], [1], [1], []]
    s = 0
    t = 9'''
    
    print(distance(adj, cost, s, t))
    #print(adj,cost,s,t)
