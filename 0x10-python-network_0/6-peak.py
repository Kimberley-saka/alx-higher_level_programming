#!/usr/bin/python3
"""
Finds peak
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers
    """

    list1 = list_of_integers
    n = len(list1)
    if n == 0:
        return None
    if n == 1:
        return list1[0]
    if list1[0] >= list1[1]:
        return list1[0]
    if list1[n-1] >= list1[n-2]:
        return list1[n-1]
    for i in range(1, n-1):
        if list1[i] >= list1[i-1] and list1[i] >= list1[i+1]:
            return list1[i]
