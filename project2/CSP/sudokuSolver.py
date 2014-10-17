# SUDOKU SOLVER

import sys
from time import time
from sudokuUtil import *

# Please implement function solve_puzzle
# input puzzle: 2D list, for example:
# [ [0,9,5,0,3,2,0,6,4]
#   [0,0,0,0,6,0,1,0,0]
#   [6,0,0,0,0,0,0,0,0]
#   [2,0,0,9,0,3,0,0,6]
#   [0,7,6,0,0,0,0,0,3]
#   [3,0,0,0,0,0,0,0,0]
#   [9,0,0,5,0,4,7,0,1]
#   [0,5,0,0,2,1,0,9,0]
#   [0,0,8,0,0,6,3,0,5] ]
# Return a 2D list with all 0s replaced by 1 to 9.
# You can utilize argv to distinguish between algorithms
# (basic backtracking or with MRV and forward checking).
# For example: python sudokuSolver.py backtracking
def solve_puzzle(puzzle, argv):
    """Solve the sudoku puzzle."""
    puzzle = recursive_backtracking(puzzle)
    if (puzzle == False):
        return "Failed"
    return puzzle
def allUnique(x):
    seen = list()
    return not any(i in seen or seen.append(i) for i in x if i != 0)
def check_valid(puzzle):
    check = list()
    for i in range(0,9):
        check.append(allUnique(puzzle[i][:]))
    for i in range(0,9):
        check.append(allUnique([row[i] for row in puzzle]))
    for i in [0,3,6]:
        for j in [0,3,6]:
            check.append(allUnique([puzzle[i+0][j+0],puzzle[i+0][j+1],puzzle[i+0][j+2],puzzle[i+1][j+0],puzzle[i+1][j+1],puzzle[i+1][j+2],puzzle[i+2][j+0],puzzle[i+2][j+1],puzzle[i+2][j+2]]))
    return all(check)





def choose_variable(puzzle):
	for i in range(0,9):
		for j in range(0,9):
			if(puzzle[i][j] == 0):
				return [i,j]
	
	return False


def check_complete(puzzle):
	if(choose_variable(puzzle) == False):
		return True
	return False


def recursive_backtracking(puzzle):
	if ((check_valid(puzzle) == True) and (check_complete(puzzle) == True)):
		return puzzle
	[x_val, y_val] = choose_variable(puzzle)
	for value in range(1,10):
		puzzle[x_val][y_val] = value
		if (check_valid(puzzle) == True):
			result = recursive_backtracking(puzzle)
			if (result != False):
				return result
	puzzle[x_val][y_val] = 0
	return False

#===================================================#
puzzle = load_sudoku('puzzle.txt')
print "solving ..."
t0 = time()
solution = solve_puzzle(puzzle, sys.argv)
t1 = time()
print "completed. time usage: %f" %(t1 - t0), "secs."

save_sudoku('solution.txt', solution)


