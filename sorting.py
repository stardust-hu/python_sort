# -*- coding: utf-8 -*-
# Created by yhu on 2017/10/7.
# Describe:


def straight_insert_sort(lists, print_flag=False):
    """直接插入排序"""
    n = len(lists)
    for i in range(1, n):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if key < lists[j]:
                lists[j+1] = lists[j]
                lists[j] = key
            j -= 1
        if print_flag is True:
            print lists
    return lists


def shell_sort(lists, step=2, print_flag=False):
    """希尔排序"""
    n = len(lists)
    increment = n / step
    while increment > 0:
        for i in range(increment):
            j = i + increment
            while j < n:
                key = lists[j]
                k = j - increment
                while k >= 0:
                    if key < lists[k]:
                        lists[k+increment] = lists[k]
                        lists[k] = key
                    k -= increment
                j += increment
        increment /= step

        if print_flag is True:
            print lists
    return lists


def simple_selection_sort(lists, print_flag):
    """简单选择排序"""
    n = len(lists)
    for i in range(n):
        min_data = lists[i]
        for j in range(i, n):
            if lists[j] < min_data:
                min_data = lists[j]
                lists[j] = lists[i]
                lists[i] = min_data
        if print_flag is True:
            print lists
    return lists


def heap_sort(lists, print_flag=False):
    """堆排序"""
    pass


def bubble_sort(lists, print_flag=False):
    """冒泡排序"""
    n = len(lists)
    for i in range(n):
        for j in range(n-i-1):
            if lists[j] > lists[j+1]:
                lists[j+1], lists[j] = lists[j], lists[j+1]
        if print_flag is True:
            print lists
    return lists


def quick_sort(lists, left, right, print_flag=False):
    """快速排序"""
    if print_flag is True:
        print lists

    if left >= right:
        return lists

    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] > key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left-1, print_flag)
    quick_sort(lists, left+1, high, print_flag)
    return lists

if __name__ == '__main__':
    pass
