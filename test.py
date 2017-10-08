# -*- coding: utf-8 -*-
# Created by yhu on 2017/10/7.
# Describe:

import sorting

lists = [49, 38, 65, 97, 76, 13, 27, 49, 55, 04]


def main():
    # sorting.straight_insert_sort(lists, print_flag=True)
    # sorting.shell_sort(lists, step=2, print_flag=True)
    # sorting.simple_selection_sort(lists, print_flag=True)
    # sorting.bubble_sort(lists, print_flag=True)
    sorting.quick_sort(lists, 0, len(lists)-1, print_flag=True)


if __name__ == '__main__':
    main()
