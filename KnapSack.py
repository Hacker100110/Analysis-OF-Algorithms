def knapsack(w, p, m):
    n=len(w)
    dp=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if w[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]= max(dp[i-1][j],p[i-1]+dp[i-1][j - w[i-1]])


    included_items=[]
    m1=m
    for i in range(n, 0, -1):
        if dp[i][m1]!= dp[i-1][m1]:
            included_items.append(i-1)
            m1=w[i-1]


    return dp[n][m],sorted(included_items),dp

def main():
    n=int(input('Enter number of items:'))
    w=list(map(int, input('Enter weights :').split()))
    p=list(map(int, input('Enter Profit :').split()))
    m=int(input('Enter capacity:'))

    maxval,included_items,dp=knapsack(w, p, m)

    print('Table:')
    print('--------------------------')
    for row in dp:
        print(row)
    print("Maximum Value:",maxval)
    print("Items Included:",included_items)

if __name__=='__main__':
    main()
        
    
