'''
入力
4
5 6
12 4
14 7
21 2
答え
23
'''
INF = 1 << 60
# 入力
N = int(input())
h, s = zip(*[map(int, input().split()) for _ in range(N)])

# 二分探索
left = 0
right = INF
while right - left > 1:
    mid = (left + right) // 2

    # 判定
    ok = True
    t = [0] * N  # 風船を割るまでの制限時間
    for i in range(N):
        # そもそもmidが初期高度よりも低かったらfalse
        if mid < h[i]:
            ok = False
        else:
            t[i] = (mid - h[i]) // s[i]
    # 時間が差し迫っている順にソート
    t.sort()
    for i in range(N):
        if t[i] < i:
            ok = False  # 時間切れ発生
    if ok:
        right = mid
    else:
        left = mid
print(right)
