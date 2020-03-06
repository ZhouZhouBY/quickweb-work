class fibonacci(object):
    def of(n):
        dp = [1]*n
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

for i in range(1,201):
    print(fibonacci.of(i))
