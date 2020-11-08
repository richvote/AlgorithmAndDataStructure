def func(i, w, a):
    # ベースケース
    if i == 0:
        if w == 0:
            return True
        else:
            return False

    # a[i-1]を選ばない場合
    if func(i - 1, w, a):
        return True
    # a[i-1]を選ぶ場合
    if func(i - 1, w - a[i - 1], a):
        return True
    # どちらもFalseの場合はFalse
    return False


# 入力
N, W = map(int, input().split())
a = [int(input()) for _ in range(N)]

# 再帰的に解く
if func(N, W, a):
    print("Yes")
else:
    print("No")
