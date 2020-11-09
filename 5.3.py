INF = 1 << 60
# 入力
N = int(input())
h = [int(input()) for _ in range(N)]

# 初期化(最小化問題なのでINFに初期化)
dp = [INF] * N

# 初期条件
dp[0] = 0

# ループ
for i in range(1, N):
    dp[i] = min(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]))
    if i > 1:
        dp[i] = min(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]))

# 答え
print(dp[N - 1])
'''
7
2
9
4
5
1
6
10
'''
