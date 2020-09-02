#function for implementation of Bubble Sort 
def bubbleSort(arr):
    n=len(arr)

    #loop for all elements of array
    for i in range(n-1): 
    #we use range(n-1) because last loop is unnecessary
   
        for j in range(n-1): 

            #if next element of array smaller then previous
            #function swap their values
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  

def simpleSort(arr):
    n=len(arr)
    
    #loop for all elements of array
    for j in range(n-1):
    #we use range(n-1) because last loop is unnecessary

        for i in range(j, n):

            #we search for the smallest elemnent of array
            #when the smallest element at the right position
            #we find the next smallest element
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]


#example of array
arr1 = [1, 123, 1234, 4, 2, 42, 55] 
arr2 = [1, 7, 15, 14, 33, 45, 3] 

bubbleSort(arr1)
simpleSort(arr2)

print('Sorted arr1:', arr1)
print('Sorted arr2:', arr2)