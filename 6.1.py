N = 8
a = [3, 5, 8, 10, 14, 17, 21, 39]


# 目的の値keyの添字を返す（存在しない場合は-1)
def binary_search(key):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return -1


print(binary_search(10))  # => 3
print(binary_search(3))  # => 0
print(binary_search(39))  # => 7
print(binary_search(-10))  # => -1
