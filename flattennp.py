import numpy as np

def flatten(array):
    shape = np.shape(array)
    a = array.copy()
    result = []
    while True:
        try: 
            for i in range(len(a)):
                result += a[i]
            a = result.copy()
            result = []
        except(TypeError):
            break
        
    return a , shape



array = [
[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]],[[[13,14,15],[16,17,18]],[[19,20,21],[22,23,24]]]]
result,shape = flatten(array)


print(result)
print(shape)
print(np.shape(result))