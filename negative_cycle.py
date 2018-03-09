#Uses python3

import sys

def is_negative(backup,adj,cost):
    value = 0
    #print(backup)
    for i in range(len(backup)-1):
        value = value + cost[backup[i]][adj[backup[i]].index(backup[i+1])]
    return value



def DFS(adj,i):
    
    global visited
    global stack
    global wrong
    global backup
    
    visited[i]=1
    if adj[i]!=None:
        for j in adj[i]:
            
            if j in stack:
                k = stack.index(j)
                backup = stack[k:]
                backup.append(j)
                value = is_negative(backup,adj,cost)
                if value<0:
                    wrong=True
            
                return

            if visited[j]==0:
                stack.append(j)   
                DFS(adj,j)
    stack.remove(i)

def negative_cycle(adj, cost):
    global visited
    global stack
    global wrong
    global backup
    
    wrong = False
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
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
