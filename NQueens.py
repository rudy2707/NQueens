#!/usr/bin/python3
# -*- coding:utf-8 -*-

import colorama

N = 4

def plot_queens(queens, conflicts=None):
    colorama.init()

    # If conflicts is not provided, we create a list with 0.
    if conflicts is None:
        conflicts = [0] * N
    # Print the board.
    # A queen is represented by a 'x', an empty case by a 'o'.
    for i in range(N):
        for j in range(N):
            if i == queens[j]:
                # If a queen threat another one, the color is red, else green.
                if conflicts[j]:
                    print(colorama.Fore.RED + "x" + colorama.Style.RESET_ALL, end=' ')
                else:
                    print(colorama.Fore.GREEN + "x" + colorama.Style.RESET_ALL, end=' ')
            else:
                print("o", end=' ')
        print("")


def search_conflicts(queens):
    print("test")


def main():
    queens = [1, 2, 3, 2]
    conflicts = [0, 1, 0, 1]
    plot_queens(queens, conflicts)

if __name__ == '__main__':
    main()