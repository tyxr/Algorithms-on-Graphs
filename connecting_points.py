#Uses python3
import sys
import math
class Edge:
    def __init__(self,a,b,c):
        self.left = a
        self.right = b
        self.weight = c
def weight(x,y,i,j):
    length = ((x[i]-x[j])**2+(y[i]-y[j])**2)**(0.5)
    return length

def get_parent(node):
    global parent
    if node!=parent[node]:
        get_parent(parent[node])
    return parent[node]

def merge(left,right,weigh):
    global rank
    global parent
    global m
    global total_w
    l_parent = get_parent(left)
    r_parent = get_parent(right)
    if l_parent!=r_parent:
        total_w += weigh
        m = m + 1
        if rank[l_parent]>rank[r_parent]:
            parent[r_parent] = l_parent
            
        elif rank[l_parent]==rank[r_parent]:
            rank[l_parent]+=1
            parent[r_parent] = l_parent
            
        else:
            parent[l_parent] = r_parent
            
    else:
        pass
def minimum_distance(x, y):
    #write your code here
    global rank
    global parent
    global m
    global total_w
    total_w = 0
    m = 0
    n = len(x)
    edges = []
    rank = [1] * n
    parent = list(range(0, n))
    parent_list = set(range(0, n))
    for i in range(n):
        for j in range(i+1,n):
            edges.append(Edge(i,j,weight(x,y,i,j)))
    edges = sorted(edges, key=lambda edge: edge.weight)
    
    for i in range(len(edges)):
        if m==n-1:
            return total_w
            
        merge(edges[i].left,edges[i].right,edges[i].weight)





if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
