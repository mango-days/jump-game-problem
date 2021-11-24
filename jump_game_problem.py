# Jump Game problem

# Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index.

# Input: [ 2 , 3 , 1 , 1 , 4 ]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Input: [ 3 , 2 , 1 , 0 , 4 ]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

array = [ 2 , 3 , 1 , 1 , 4 ]
index = 0
flag = False
max_jump_length = array [ index ]

while ( index < len ( array ) or flag == False ) :
    if array [ index ] == 0 : 
        flag = True
        break
    elif index + array [ index ] > len ( array ) - 1 : break
    else : index += array [ index ]
    
if flag == True : print (" false ")
else : print ( " true ")