import sys

class Graph:
    
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for _ in range(vertices)]for _ in range(vertices)]
        
    def minKey(self,key,mstSet):
        min_val=sys.maxsize
        min_index=-1
        
        for v in range(self.V):
            if key[v]<min_val and not mstSet[v]:
                min_val=key[v]
                min_index=v
                
        return min_index
        
    def primsMST(self):
        key=[sys.maxsize]*self.V
        parent=[None]*self.V
        key[0]=0
        mstSet=[False]*self.V
        parent[0]=-1
        
        for _ in range(self.V):
            u=self.minKey(key,mstSet)
            mstSet[u]=True
            for v in range(self.V):
               if self.graph[u][v] and not mstSet[v] and key[v]> self.graph[u][v]:
                key[v]=self.graph[u][v]
                parent[v]=u
                
        self.printMST(parent)
        
    def printMST(self,parent):
        print("Edge) \tweight")
        for i in range(1,self.V):
            print(f"{parent[i]}-{i} \t{self.graph[i] [parent[i]]}")
            
if __name__ == "__main__":
    g=Graph(5)
    
    g.graph=[
        [0,2,0,6,0],
        [2,0,3,8,5],
        [0,3,0,0,7],
        [6,8,0,0,9],
        [0,5,7,9,0]]
    g.primsMST()
            