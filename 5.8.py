INF = 1 << 29
# 入力
S, T = input().split()
# DPテーブル定義
dp = [[INF] * (len(T) + 1) for _ in range(len(S) + 1)]
# DP初期条件
dp[0][0] = 0
# DPループ
for i in range(len(S)+1):
    for j in range(len(T)+1):
        # 変更操作
        if i > 0 and j > 0:
            if S[i-1] == T[j-1]:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1])
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] +1)
        # 削除操
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
        # 挿入操作
        if j > 0:
            dp[i][j] = min(dp[i][j], dp[i][j-1] +1)
    # 答えの出力
print(dp[len(S)][len(T)])

'''
logistic algorithm
'''