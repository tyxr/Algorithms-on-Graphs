#Uses python3

import sys


wrong = False
def DFS(adj,i):
    
    global visited
    global stack
    global wrong
    
    visited[i]=1
    if adj[i]!=None:
        for j in adj[i]:
            
            if j in stack:
                
                wrong = True
                return

            if visited[j]==0:
                stack.append(j)   
                DFS(adj,j)
    stack.remove(i)

def acyclic(adj):
    global visited
    global stack
    global wrong
    visited = [0 for _ in range(len(adj))]
    for i in range(len(adj)):
        
        stack = []
        if (visited[i]==0):
            stack.append(i)
            DFS(adj,i)
        
        if wrong==True:
            return 1
        
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
