#Uses python3

import sys

sys.setrecursionlimit(200000)
def reverse(adj):
    n = len(adj)
    r_adj = [[] for _ in range(n)]
    for i in range(n):
        if adj[i]!=None:
            for j in adj[i]:
                r_adj[j].append(i)
    return r_adj

def DFS(adj,i):
    
    global visited
    global re_order
    
    visited[i] = 1
    
    
    if adj[i]!=None:
        for j in adj[i]:

            if visited[j]==0:
                
                DFS(adj,j)
    re_order.append(i)

def DFSTraverse(adj):
    global visited

    visited = [0 for _ in range(len(adj))]

    for i in range(len(adj)):
        if (visited[i]==0):
            DFS(adj,i)


def number_of_strongly_connected_components(adj):
    global re_order
    global visited
    re_order = []
    result = 0
    r_adj = reverse(adj)
    DFSTraverse(r_adj)

    visited = [0 for _ in range(len(adj))]
    re_order.reverse()
    
    for i in range(len(re_order)):
        j = re_order[i]
        
        if (visited[j]==0):
            DFS(adj,j)
            
            result = result + 1


    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    #adj = [[1],[],[1],[2]]

    print(number_of_strongly_connected_components(adj))
