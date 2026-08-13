# -*- coding: utf-8 -*-


def quick_sort(arr):
    """快速排序（递归实现）"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    test = [3, 6, 8, 10, 1, 2, 1]
    print("排序前:", test)
    print("排序后:", quick_sort(test))
