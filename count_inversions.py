#!/usr/bin/env python

"""
Counts inversions of an array of integer numbers.
"""

__author__ = "Tristana Sondon"
__copyright__ = "Copyright 2014, Tristana Sondon"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "tristana.sondon@gmail.com"

import sys

def merge(a1, a2):
    i = 0
    j = 0
    k = 0
    n1 = len(a1)
    n2 = len(a2)
    r = [0] * (n1 + n2)
    inversion_counter = 0
    while i < n1 or j < n2:
        if i < n1 and j < n2:
            if a1[i] < a2[j]:
                r[k] = a1[i]
                i += 1
            else:
                r[k] = a2[j]
                j += 1
                inversion_counter += n1 - i
        elif i < n1:
            for e in a1[i:]:
                r[k] = e
                i += 1
                k += 1
        else:
            for e in a2[j:]:
                r[k] = e
                j += 1
                k += 1
        k += 1
    return r, inversion_counter


def _merge_sort_and_count_inv(a, ictot):
    n = len(a)
    if n > 0:
        if n == 1:
            ictot = 0
            return a, ictot 
        else:
            al, icl = _merge_sort_and_count_inv(a[:n/2], ictot)
            ar, icr = _merge_sort_and_count_inv(a[n/2:], ictot)
        sorted_array, invc = merge(al, ar)
        ictot = ictot + invc + icl + icr
        return sorted_array, ictot
    return [], 0

def count_inversions(input_array):
    return _merge_sort_and_count_inv(input_array, 0)
    

if __name__ == "__main__":

    try:
        filename = sys.argv[1]
        with open(filename, 'r') as inputfile:
            number_list = inputfile.read().splitlines()
        number_list = [int(n) for n in number_list]
        sorted_array, inversion_count =  count_inversions(number_list)
        # print sorted_array
        print "Number of Inversions: ", inversion_count

    except:
        print "Use: count_inversions <input_file>"


# TODO: Add tests
# number_list = [2,1,4,3]
# number_list = [6,5,4,3,2,1]
