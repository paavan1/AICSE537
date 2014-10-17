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
def solve_puzzle(puzzle, listoflistofstacks, argv):
    """Solve the sudoku puzzle."""
    puzzle = recursive_backtracking(puzzle, listoflistofstacks)
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

def choose_variable(puzzle, listoflistofstacks):
	minimumvalues = [100,100,100]
	for i in range(0,9):
		for j in range(0,9):
			if((len(listoflistofstacks[i][j]) < minimumvalues[2]) and (len(listoflistofstacks[i][j])>1) and (puzzle[i][j]==0)):
				minimumvalues = [i, j, len(listoflistofstacks[i][j])]
	if(minimumvalues[0] == 100):
		for i in range(0,9):
			for j in range(0,9):
				if (puzzle[i][j]==0):
					return [i,j]
		return False

		
	else:
		return [minimumvalues[0],minimumvalues[1]]
def check_complete(puzzle):
	if(choose_variable(puzzle,listoflistofstacks) == False):
		return True
	return False
def build_stacks(puzzle):
	listoflistofstacks = []
	rowsofstacks = []
	allpossible = [1,2,3,4,5,6,7,8,9]
	for i in range(0,9):
		rowsofstacks = []
		for j in range(0,9):
			if (puzzle[i][j] == 0):
				rowsofstacks.append(allpossible)
			else:
				rowsofstacks.append([puzzle[i][j]])
		listoflistofstacks.append(rowsofstacks)
	return listoflistofstacks


def propogate_constraints(puzzle,lister, x, y, value):
#collums
	for i in range(0,9):
		if(( value in lister[x][i]) and (puzzle[x][i]==0) and (len(lister[x][i]) > 1) ):
			lister[x][i].remove(value)
			print "removed"
#			if (len(lister[x][i])==1):
#				propogate_constraints(lister, x, i, lister[x][i][0])
#rows
#	for j in range(0,9):
#		if value in lister[j][y]:
#			lister[j][y].remove(value)
#			if (len(lister[j][y])==1):
#				 propogate_constraints(lister, j, y, lister[j][y][0])

#box
#	box_x = x/3
#	box_y = y/3
#	for i in range(0,3):
#		for j in range(0,3):
#			if value in lister[box_x + i][box_y + j]:
#				lister[box_x + i][box_y + j].remove(value)
#				if (len(lister[box_x + i][box_y + j])==1):
#					 propogate_constraints(lister, box_x + i,box_y + j, lister[box_x + i][box_y + j][0])

	return lister	




def recursive_backtracking(puzzle, listoflistofstacks):
	if ((check_valid(puzzle) == True) and (check_complete(puzzle) == True)):
		return puzzle
	[x_val, y_val] = choose_variable(puzzle,listoflistofstacks)
	savedstack = listoflistofstacks
	for value in savedstack[x_val][y_val]:
	 	savedstack2 = listoflistofstacks
		puzzle[x_val][y_val] = value
#		listoflistofstacks[x_val][y_val] = [value]
#		listoflistofstacks = propogate_constraints(puzzle,listoflistofstacks, x_val, y_val, value)
		if (check_valid(puzzle) == True):
			print "true"
			result = recursive_backtracking(puzzle, listoflistofstacks)
			if (result != False):
				return result
		else:
		  	print "false"
		listoflistofstacks = savedstack2
	puzzle[x_val][y_val] = 0
#	listoflistofstacks = savedstack
	return False

#===================================================#
puzzle = load_sudoku('puzzle.txt')
print "solving ..."
listoflistofstacks = build_stacks(puzzle)
t0 = time()
solution = solve_puzzle(puzzle, listoflistofstacks, sys.argv)
t1 = time()
print "completed. time usage: %f" %(t1 - t0), "secs."

save_sudoku('solution.txt', solution)


