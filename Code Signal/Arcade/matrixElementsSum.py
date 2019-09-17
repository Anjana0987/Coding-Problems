'''
Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

Example

For matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
the output should be matrixElementsSum(matrix) = 9.

There are several haunted rooms, so we'll disregard them as well as any rooms beneath them. Thus, the answer is 1 + 5 + 1 + 2 = 9.

For matrix = [[1, 1, 1, 0], 
          [0, 5, 0, 1], 
          [2, 1, 3, 10]]
the output should be matrixElementsSum(matrix) = 9.
'''
def matrixElementsSum(matrix):
    costSum = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if x>0:
                if matrix[x-1][y] == 0:
                    matrix[x][y] = 0
            costSum += matrix[x][y]
    return costSum
                
