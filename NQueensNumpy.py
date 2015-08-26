#!/usr/bin/python3
# -*- coding:utf-8 -*-

import colorama
import numpy

# Modification of the programme by using Numpy.

# Number of queens
N = 10

def plot_queens(queens, conflicts=None):
    """Print the board with the queens.

    A queen is represented by a 'x' on the board and an empty case by a 'o'.
    If there is a conflicts, the 'x' is red, else it's green.

    Keyword arguments:
    queens      -- the list with the positions of the queens
    conflicts   -- optional list with the conflicts between the queens
    """

    colorama.init()

    # If conflicts is not provided, we create a list with 0
    if conflicts is None:
        conflicts = numpy.zeros(N,)
    # Print the board.
    # A queen is represented by a 'x', an empty case by a 'o'
    for i in range(N):
        for j in range(N):
            if i == queens[j]:
                # If a queen threat another one, the color is red, else green
                if conflicts[j]:
                    print(colorama.Fore.RED + "x" + colorama.Style.RESET_ALL, end=' ')
                else:
                    print(colorama.Fore.GREEN + "x" + colorama.Style.RESET_ALL, end=' ')
            else:
                print("o", end=' ')
        print("")


def search_conflicts(queens):
    """Search the conflicts between the queens.

    The positions of the queens are stored in a list.
    The index represents the column and the value the line number.

    There is no conflict in the column or the line, so we only need to check the diagonals.
    If the difference of the i and the j position are the same between the queens,
    they are on the same diagonal.

    Keyword arguments:
    queens      -- the list with the positions of the queens
    """

    conflicts = numpy.zeros(N,)

    # Find conflicts in diagonals
    for i in range(N):
        for j in range(N):
            if i != j:
                if abs(queens[j] - queens[i]) == abs(j - i):
                    conflicts[j] = 1

    return conflicts

def main():
    """Main function."""
    # Generate the first position of the queens and print it.
    queens = numpy.arange(0, N)
    numpy.random.shuffle(queens)

    cnt = 1

    print("First board :")
    plot_queens(queens, search_conflicts(queens))

    # Look for a solution by generating random boards.
    while any(search_conflicts(queens)):
        numpy.random.shuffle(queens)
        cnt = cnt + 1

    print("\nA solution :")
    plot_queens(queens, search_conflicts(queens))
    print("\nNumber of tries : ", cnt)


if __name__ == '__main__':
    main()