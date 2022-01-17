import numpy as np

def random_filter(start,end,shape):
    return np.random.randint(start,end,shape)

def conv2d(array,filr,st=1):
    #array = np.array(arr)
    filterr = np.array(filr)
    matr = [[0 for i in range(len(filterr))] for i in range(len(filterr[0]))]
    print(matr)
    cell = []
    res = []
    for i in range(0,len(array)-len(filterr)+1,st):
        cell = []
        for j in range(0,len(array[0])-len(filterr[0])+1,st):
            for k in range(len(filterr)):
                for d in range(0,len(filterr[0])):
                    print(k+d)
                    matr[k][d] = array[i+k][j+d]* filterr[k][d]
            cell.append(sum([sum(i) for i in matr]))
        res.append(cell)
    inp_shape = np.shape(array)
    filter_shape = np.shape(filterr)
    out_shape = np.shape(res)
            
                
    return res ,inp_shape, filter_shape, out_shape


array = [
    [3,3,2,1,0,7],
    [0,0,1,3,1,8],
    [3,1,2,2,3,6],
    [2,0,0,2,2,5],
    [2,0,0,0,1,3],
    [2,0,0,0,1,3]

    ]

filterr = [
    [0,1,2],
    [2,2,0],
    [0,1,2],
    ]

result,input_shape,filter_shape,output_shape = conv2d(array, filterr)
print(result,2)
print(input_shape)
print(filter_shape)
print(output_shape)
print(random_filter(0, 10, (3,3)))