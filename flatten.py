import numpy as np

def shape(array):
    part_of_arr = array.copy()
    shape = []
    while True:
        try:
            shape.append(len(part_of_arr))
            part_of_arr = part_of_arr[0]
            
        except(TypeError):
            break
        except(AttributeError):
            break
    return tuple(shape)

def flatten(array):
    arr = array.copy()

    result = []
    
    
    
    while True:
        try:
            
            result = []
            for i in range(len(arr)):
                result += arr[i]
            arr = result.copy()
        except(TypeError):
            break
        

        
        
    return arr



array = [
[[
 [1,2,3],
 [4,5,6]
 ],[
 [7,8,9],
 [10,11,12]
 ]],[
    [
     [13,14,15],
     [16,17,18]
     ],[
     [19,20,21],
     [22,23,24]
     ]
        ]
    ]
result = flatten(array)

print(shape(array))
print(result)
print(shape(result))