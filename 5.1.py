INF = 1 << 60
# 入力
N = int(input())
h = [int(input()) for _ in range(N)]
# 配列dpを定義(配列全体を無限大を表す値に初期化)
dp = [INF] * N
# 初期条件
dp[0] = 0

# ループ
for i in range(1, N):
    if i == 1:
        dp[i] = abs(h[i] - h[i - 1])
    else:
        dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]),
                    dp[i - 2] + abs(h[i] - h[i - 2]))

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
