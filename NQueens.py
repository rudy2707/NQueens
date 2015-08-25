#!/usr/bin/python3
# -*- coding:utf-8 -*-

import random

# Number of queens
N = 4

# def plot_queens(queens, conflicts=None):


def search_conflicts(queens):
    conflicts = [0] * N

    # find conflicts in diagonals
    for i in range(N):
        for j in range(N):
            if i != j:
                if abs(queens[j] - queens[i]) == abs(j - i):
                    conflicts[j] = 1

    return conflicts

def main():
    # generate the queens
    queens = random.sample(range(N), N)

    print(search_conflicts(queens))

if __name__ == '__main__':
    main()