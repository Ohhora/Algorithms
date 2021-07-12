## source : https://www.daleseo.com/sort-insertion/


def insert_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j-1] >= arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr
            
