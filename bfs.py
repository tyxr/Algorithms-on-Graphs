#Uses python3

import sys
import queue

def distance(adj, s, t):
    
    visited = [-1 for _ in range(len(adj))]
    n = 0
    if adj[s]!= None:
        temp = adj[s]
        visited[s] = n
    
    while(temp!=None):
        next_list = []
        
        for i in temp:
            if i == t:
                return n+1
            if visited[i]==-1:
                visited[i]=n+1
                next_list.extend(adj[i])
        temp = next_list
        n = n + 1
        
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
