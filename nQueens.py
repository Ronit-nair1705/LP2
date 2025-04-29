def isSafe(mat,row,col):
    n=len(mat)
    
    for i in range(row):
        if mat[i][col]:
            return False
    
    for i,j in zip(range(row -1,-1,-1),range(col -1,-1,-1)):
        if mat[i][j]:
            return False
        
    for i,j in zip(range(row -1,-1,-1),range(col+1,n)):
        if mat[i][j]:
            return False
        
    return True
    
def placeQueens(row,mat):
    n=len(mat)
    
    if row==n:
        return True
    
    for i in range(n):
        if isSafe(mat,row,i):
            mat[row][i]=1
            if placeQueens(row+1,mat):
               return True
            mat[row][i]=0
    return False
            
def nQueens(n):
    mat=[[0 for _ in range(n)]for _ in range(n)]
    
    if placeQueens(0,mat):
        
        ans=[]
        for i in range(n):
            for j in range(n):
                if mat[i][j]:
                    ans.append(j+1)
        return ans
    else:
        return[-1]
        
if __name__ == "__main__":
    
    n=4
    
    ans=nQueens(n)
    
    print(" ".join(map(str,ans)))