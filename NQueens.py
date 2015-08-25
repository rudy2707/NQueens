#!/usr/bin/python3
# -*- coding:utf-8 -*-

N = 4

def plot_queens(queens, conflicts=None):
    for i in range(len(queens)):
        for j in range(len(queens)):
            if i == queens[j]:
                print("x", end=' ')
            else:
                print("o", end=' ')
        print("")


def search_conflicts(queens):
    print("test")


def main():
    queens = [1, 2, 3, 2]
    plot_queens(queens)

if __name__ == '__main__':
    main()