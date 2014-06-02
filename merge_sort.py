#!/usr/bin/env python

"""
Merge Sort Algorithm
"""

__author__ = "Tristana Sondon"
__copyright__ = "Copyright 2014, Tristana Sondon"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "tristana.sondon@gmail.com"


def merge(a1, a2):
    r = []
    i = 0
    j = 0
    n1 = len(a1)
    n2 = len(a2)

    while i < n1 or j < n2:
        if i < n1 and j < n2:
            if a1[i] < a2[j]:
                r.append(a1[i])
                i += 1
            else:
                r.append(a2[j])
                j += 1
        elif i < n1:
            for e in a1[i:]:
                r.append(e)
                i += 1
        else:
            for e in a2[j:]:
                r.append(e)
                j += 1
    return r


def merge_sort(a):
    n = len(a)
    if n > 0:
        if n == 1:
            return a
        else:
            al = merge_sort(a[:n/2])
            ar = merge_sort(a[n/2:])
        return merge(al, ar)
    return []


if __name__ == "__main__":

    # TODO: write this as tests
    a = [3, 7, 1, 8, 2, 4, 6, 5]
    print a, " --> ", merge_sort(a)

    a = [3, 7, 1, 8, 2, 4, 6, 5, 0]
    print a, " --> ", merge_sort(a)

    a = [3, 7, 1, -8, 2, -4, 6, 5, 0]
    print a, " --> ", merge_sort(a)

    a = [9,8,7]
    print a, " --> ", merge_sort(a)

    a = [8,8,8]
    print a, " --> ", merge_sort(a)

    a = [8,1]
    print a, " --> ", merge_sort(a)

    a = [2]
    print a, " --> ", merge_sort(a)

    a = []
    print a, " --> ", merge_sort(a)


