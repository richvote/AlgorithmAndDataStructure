# Frog問題をメモ化再帰で解く

def rec(i):
    # dpの値が更新されていたらそのままリターン
    if dp[i] < INF:
        return dp[i]
    # ベースケース: 足場0のコストは0
    if i == 0:
        return 0

    # 答えを表す変数をINFで初期化
    res = INF

    # 足場i-1から来た場合
    res = min(res, rec(i - 1) + abs(h[i] - h[i - 1]))

    # 足場i-2から来た場合
    if i > 1:
        res = min(res, rec(i - 2) + abs(h[i] - h[i - 2]))

    # 結果をメモしながら返す
    dp[i] = res
    return dp[i]


INF = 1 << 60
N = int(input())
h = [int(input()) for _ in range(N)]
dp = [INF] * N
print(rec(N - 1))

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
