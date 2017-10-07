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


def shell_sort(lists, print_flag=False):
    pass


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


def heap_sort(lists, print_flag=False):
    pass

if __name__ == '__main__':
    pass
