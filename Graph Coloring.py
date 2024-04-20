def issafe(node, color, graph, colors, n):
    for i in range(n):
        if graph[node][i] and colors[i]==color:
            return False
    return True

def graph_coloring(graph, m, colors, n,k=0):
    if k==n:
        print(colors)
        return
    for color in range(1,m+1):
        if issafe(k, color, graph, colors, n):
            colors[k]=color
            graph_coloring(graph, m, colors, n,k+1)
            colors[k]=0

def main():
    n=int(input('Enter number of vertices:'))
    m=int(input('Enter number of colors:'))
    graph=[]
    print('Enter adjancencey matrix:')      
    for _ in range(n):
          row=list(map(int, input().split()))
          graph.append(row)
    colors=[0]*n
    print('Total Solutions')
    graph_coloring(graph, m, colors, n)

if __name__=='__main__':
          main()
