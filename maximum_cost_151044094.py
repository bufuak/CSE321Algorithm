# first we need to create dynamic table, and fill with zeros.
# dp's first row[0] stores he maximum value of sum using first i elements if ith array value is kept as a[i] itself.
# dp's second row[1] stores the maximum value of sum using first i elements only if ith array value is modified to 1.
# Finally we take maximum of last contents of row1 and row2 as a return value.

def find_maximum_cost(array):
    size = len(array)
    dp = [[0 for row in range(0, 2)] for col in range(0, size)]
    for i in range(size-1):
        dp[i+1][0] = max(dp[i][1] + abs(array[i+1] -1),dp[i][0] + abs(array[i+1]-array[i]))
        dp[i+1][1] = max(dp[i][1],dp[i][0] + abs(1-array[i]))
    return max(dp[size-1][0],dp[size-1][1])

Y = [14,1,14,1,14]
cost = find_maximum_cost(Y)
print(cost)
#Output: 52
Y = [1,9,11,7,3]
cost = find_maximum_cost(Y)
print(cost)
#Output: 28
Y = [50,28,1,1,13,7]
cost = find_maximum_cost(Y)
print(cost)
#Output: 78