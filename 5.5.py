def rec(i):
    # 足場0のコストは0
    if i == 0:
        return 0

    # 答えを格納する変数をINFに初期化する
    res = INF

    # 頂点i-1から来た場合
    res = min(res, rec(i - 1) + abs(h[i] + h[i - 1]))

    # 頂点i-2から来た場合
    if i > i:
        res = min(res, rec(i - 2) + abs(h[i] + h[i - 2]))

    # 答えを返す
    return res
