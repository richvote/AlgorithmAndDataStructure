INF = 1 << 60
# 入力
N = int(input())
c = [[int(input()) for j in range(N + 1)] for i in range(N + 1)]
# DPテーブル定義
dp = [INF] * (N + 1)
# DP初期条件
dp[0] = 0
# DPループ
for i in range(N + 1):
    for j in range(i):
        dp[i] = min(dp[i], dp[j] + c[j][i])
# 答えの出力
print(dp[N])
