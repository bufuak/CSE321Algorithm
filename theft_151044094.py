# First i missunderstood the problem so solved for starting point anywhere on
# first row and finished in last row. So I reversed given 2 dim matrix to solve for
# our problem. First i create a reversed matrix from our coins matrix, but reversed
# and dp table for it. Fill the dp tables first row with our row values. And then
# we start to look values from row 2 as we know our last values calculated, its just most
# value from back and current index value. Keep this result to dp table to current index.
# After all calculations, we must look at the n-1 th row in dp for biggest path value. Return it

def theft(coins):
    size = len(coins)
    result = 0
    reversed = [[0 for row in range(0,size)] for col in range(0,size)]
    for i in range(0,size):
        for j in range(0,size):
            reversed[j][i]=coins[i][j]
    dp =[[0 for row in range(0,size+2)] for col in range(0,size)]
    for i in range(0,size):
        dp[0][i+1] = reversed[0][i]

    for i in range(1,size):
        for j in range(1,size+1):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j+1],dp[i-1][j]) + reversed[i][j-1]
            print(dp)
    for i in range(0,size+1):
        result = max(result,dp[size-1][i])
    return result

amountOfMoneyInLand= [[1,3,1,5], [2,2,4,1], [5,0,2,3], [0,6,1,2]]
res = theft(amountOfMoneyInLand)
print(res)
#Output: 16
amountOfMoneyInLand= [[10,33,13,15], [22,21,4,1], [5,0,2,3], [0,6,14,2]]
res = theft(amountOfMoneyInLand)
print(res)
#Output: 83