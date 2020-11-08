# 入力受け取り
N, W = map(int, input().split())
a = [int(input()) for _ in range(N)]
# bitは2^N通りの部分集合全体を動きます。
exist = False
for bit in range(0, 1 << N):
    # print(bin(bit))
    sum = 0 # 部分集合に含まれる要素の和
    for i in range(N):
        # i番目の要素a[i]が部分集合に含まれているかどうか
        if bit & (1 << i):
            sum += a[i]
        # sumがWに一致するかどうか
        if sum == W:
            exist = True

if exist:
    print("Yes")
else:
    print("No")
'''
5 10
1
2
4
5
11
'''
