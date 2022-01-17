import numpy as np
import math as m

def np_to_list2D(array):
    l = []
    for i in array:
        l.append(list(i))
    return l

def maxpool(arr,shape,st=1):
    array = np_to_list2D(arr)
    result = []
    node = []
    mat=[]

    for i in range(0,len(array)-shape[0]+1,st):
        node = []
        for j in range(0,len(array[0])-shape[1]+1,st):
            mat = []
            for d in array[i:i+shape[0]]:
                a = d[j:j+shape[0]]
                mat += a
            node.append(max(mat))
        result.append(node)
               

                
    return result

def minpool(array,shape,st=1):
   
    result = []
    node = []
    mat=[]

    for i in range(0,len(array)-shape[0]+1,st):
        node = []
        for j in range(0,len(array[0])-shape[1]+1,st):
            mat = []
            for d in array[i:i+shape[0]]:
                a = d[j:j+shape[0]]
                mat += a
            node.append(min(mat))
        result.append(node)
               

                
    return result


def avgpool(array,shape,st=1):
    result = []
    node = []
    mat=[]

    for i in range(0,len(array)-shape[0]+1,st):
        node = []
        for j in range(0,len(array[0])-shape[1]+1,st):
            mat = []
            for d in array[i:i+shape[0]]:
                a = d[j:j+shape[0]]
                mat += a
            node.append(sum(mat)/len(mat))
        result.append(node)
               

                
    return result


def avg_pool(array,shape):
    if(len(shape)==2):
        if(shape[0] != shape[1]):
            raise print('Area must be quadratic')
    selected_area=[]
    result = []
    res = []
    node_count=0
    for i in range(0,np.shape(array)[0],shape[0]):
        for j in range(0,np.shape(array)[1],shape[1]):
            for k in range(i,i+shape[1],1):
                selected_area += array[k][j:j+shape[1]]
            result.append(sum(selected_area)/len(selected_area))
            node_count +=1
            selected_area = []
    for i in range(0,len(result),int(m.sqrt(len(result)))):
        res.append(result[i:int(i+m.sqrt(len(result)))])
        
    return res

def min_pool(array,shape):
    if(len(shape)==2):
        if(shape[0] != shape[1]):
            raise print('Area must be quadratic')
    selected_area=[]
    result = []
    res = []
    node_count=0
    for i in range(0,np.shape(array)[0],shape[0]):
        for j in range(0,np.shape(array)[1],shape[1]):
            for k in range(i,i+shape[1],1):
                selected_area += array[k][j:j+shape[1]]
            result.append(min(selected_area))
            node_count +=1
            selected_area = []
    for i in range(0,len(result),int(m.sqrt(len(result)))):
        res.append(result[i:int(i+m.sqrt(len(result)))])
        
    return res

def max_pool(array,shape):
    if(len(shape)==2):
        if(shape[0] != shape[1]):
            raise print('Area must be quadratic')
    selected_area=[]
    result = []
    res = []
    node_count=0
    for i in range(0,np.shape(array)[0],shape[0]):
        for j in range(0,np.shape(array)[1],shape[1]):
            for k in range(i,i+shape[1],1):
                selected_area += array[k][j:j+shape[1]]
            result.append(max(selected_area))
            node_count +=1
            print(selected_area)
            selected_area = []
    for i in range(0,len(result),int(m.sqrt(len(result)))):
        res.append(result[i:int(i+m.sqrt(len(result)))])
        
    return res
            

array = np.array([
    [3,3,2,1,0,7],
    [0,0,1,3,1,8],
    [3,1,2,2,3,6],
    [2,0,0,2,2,5],
    [2,0,0,0,1,3],
    [2,0,0,0,1,3]
    ])

print(maxpool(array, (3,3),st=3))
