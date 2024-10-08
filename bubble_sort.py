import random
arr = [random.randint(1,100) for x in range(random.randint(1,10))]

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 ):
            if arr[j] > arr[j+1]:
               
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                
print("Unsorted List: ", arr)
bubble_sort(arr)
print("Sorted List: ", arr)
