'''
6 15
2 3
1 2
3 6
2 1
1 3
5 85
'''
# 入力
N, W = map(int, input().split())
weight, value = zip(*[map(int, input().split()) for _ in range(N)])

# DPテーブル定義
dp = [[0] * (W + 1) for _ in range(N + 1)]

# DPループ
for i in range(N):
    for w in range(W + 1):
        # i番目の品物を選ぶ場合
        if w - weight[i] >= 0:
            dp[i + 1][w] = max(dp[i + 1][w], dp[i][w - weight[i]] + value[i])
        # i番目の品物を選ばない場合
        dp[i + 1][w] = max(dp[i + 1][w], dp[i][w])

# 最適地の出力
print(dp[N][W])
for i in dp:
   print(i)
