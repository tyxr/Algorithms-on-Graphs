#Uses python3

import sys

def reach(adj, x, y):
    DFSTraverse(adj,x)
    if visited[y]==1:
        return 1
    else:
        return 0

def DFS(adj,i):
    
    global visited
    
    visited[i]=1
    
    
    if adj[i]!=None:
        for j in adj[i]:

            if visited[j]==0:
                
                DFS(adj,j)
            else:
                pass
    else:
        pass
def DFSTraverse(adj,x):
    global visited
    visited = [0 for _ in range(len(adj))]
    '''for i in range(len(adj)):
        if (visited[i]==0):
            DFS(adj,i)'''
    DFS(adj,x)
        
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
