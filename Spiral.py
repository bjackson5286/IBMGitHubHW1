#  File: Spiral.py

#  Description: Create a spiral of numbers

#  Student Name: Christopher Herrod

#  Student UT EID: cbh2528

#  Partner Name: Brynne Jackson

#  Partner UT EID: bj8733

#  Course Name: CS 313E

#  Unique Number: 51130/51135

#  Date Created: 1/31/2022

#  Date Last Modified:2/1/2022

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

import sys


def create_spiral(n):
    #make a matrix based on the dimensions passed on in the parameters

    spiral_matrix = []

    for i in range(n):
        spiral_matrix.append([])
        for j in range(n):
            spiral_matrix[i].append(j)
    
    #initializes a matrix with n elements in each list and n lists
    #spiral_matrix = [[ 0 for i in range(n)] for j in range(n)]


    #find center index of matrix
    index = [n//2, n//2]

    #initialize element number
    element = 1

    #start spiral with right direction
    direction = 'r'

    #edit spiral with 1 starting at center index
    spiral_matrix[index[0]][index[1]] = 1

    #initialize counters by direction
    r_step = 1
    l_step = 2
    u_step = 2
    d_step = 1


    while True:

        if direction == 'r':
            if element >= n**2:
                break
            for num in range(r_step):
                element += 1
                index = get_index(index[0],index[1],direction)
                spiral_matrix[index[0]][index[1]] = element
                if element >= n**2:
                    break
                #print(spiral_matrix)
                
            if element >= n**2:
                break
            direction = 'd'
            r_step += 2

        if element >= n**2:
            break
        if direction == 'l':

            for num in range(l_step):
                element += 1
                index = get_index(index[0],index[1],direction)
                spiral_matrix[index[0]][index[1]] = element


            direction = 'u'
            l_step += 2     

        if direction == 'd':

            for num in range(d_step):
                element += 1
                index = get_index(index[0],index[1],direction)
                spiral_matrix[index[0]][index[1]] = element


            direction = 'l'
            d_step += 2


        if direction == 'u':

            for num in range(u_step):
                element += 1
                index = get_index(index[0],index[1],direction)
                spiral_matrix[index[0]][index[1]] = element


            direction = 'r'
            u_step += 2
            
    
    return spiral_matrix

#takes in points of current index & desired direction and returns new index
def get_index(p1, p2, direction):
    
    index = [0,0]
    if direction == 'r':
        index = [p1, p2+1]

    if direction == 'l':
        index = [p1, p2-1]

    if direction == 'd':
        index = [p1+1, p2]

    if direction == 'u':
        index = [p1-1, p2]

    return index
         

## Input: spiral is a 2-D list and n is an integer
## Output: returns an integer that is the sum of the
##         numbers adjacent to n in the spiral
##         if n is outside the range return 0
         
def sum_adjacent_numbers(spiral, n):
    
    #first find the index of the number in the matrix
    count_dimension = 0
    index_num = [0,0]
    for row in range(len(spiral)):
        #keep track of spiral dimension
        count_dimension += 1
        for col in range(len(spiral[row])):
            if spiral[row][col] == n:
                index_num = [row, col]

    #initialize sum on num
    sum_num = 0
    
    #find down num
    if index_num[0] < (count_dimension-1):
        sum_num += spiral[(index_num[0]+1)][index_num[1]]
        #print('down num', sum_num)

    #find up num
    if index_num[0] > 0:
        sum_num += spiral[(index_num[0]-1)][index_num[1]]
        #print('up num', spiral[(index_num[0]-1)][index_num[1]])

    #find right num
    #direct right
    if index_num[1] < (count_dimension-1):
        sum_num += spiral[index_num[0]][(index_num[1]+1)]
        #print('right num', spiral[index_num[0]][(index_num[1]+1)])
        #bottom right corner
        if index_num[0] < (count_dimension-1):
            #print('bottom right num', spiral[(index_num[0]+1)][(index_num[1]+1)])
            sum_num += spiral[(index_num[0]+1)][(index_num[1]+1)]
        #top right
        if index_num[0] > 0:
            sum_num += spiral[(index_num[0]-1)][(index_num[1]+1)]
            #print('top right num', spiral[(index_num[0]-1)][(index_num[1]+1)])
        
    #find left num
    #direct left
    if index_num[1] > 0:
        sum_num += spiral[index_num[0]][(index_num[1]-1)]
        #bottom left corner
        if index_num[0] < (count_dimension-1):
            sum_num += spiral[(index_num[0]+1)][(index_num[1]-1)]
        #top left
        if index_num[0] > 0:
            sum_num += spiral[(index_num[0]-1)][(index_num[1]-1)]
        
    
    #print(sum_num)
    return sum_num


def main():    
### read the input file
    
    input_0 = sys.stdin.read()
    input_1 = input_0.split('\n')

    #print(input_1)
### create the spiral
    n = int(input_1[0])
    new_spiral = create_spiral(n)
### add the adjacent numbers
    for i in range(1,len(input_1)-1):
        a = int(input_1[i])
        sum_ = sum_adjacent_numbers(new_spiral, a)
        sum_ = int(sum_)
        print(sum_)
        
### print the result

if __name__ == "__main__":
    main()
