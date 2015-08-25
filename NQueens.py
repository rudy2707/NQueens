#!/usr/bin/python3
# -*- coding:utf-8 -*-

import colorama
import random

# Number of queens
N = 20

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

    print("First board :")
    plot_queens(queens, search_conflicts(queens))

    # Generate a random board while there are conflicts.
    while any(search_conflicts(queens)):
        queens = random.sample(range(N), N)

    print("\nA solution :")
    plot_queens(queens, search_conflicts(queens))


if __name__ == '__main__':
    main()