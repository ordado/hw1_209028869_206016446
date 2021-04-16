import sys
import pandas
import math


def sum(values):
    s = 0
    for value in values:
        s += value
    return s


def mean(values):
    s = sum(values)
    return s / len(values)


def median(values):
    l = len(values) / 2
    if l % 2 != 0:
        l = round(l) - 1
        return values[l]
    l = round(l)
    return (values[l] + values[l - 1]) / 2
