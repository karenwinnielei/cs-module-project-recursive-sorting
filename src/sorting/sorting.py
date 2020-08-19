# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    indexA = 0
    indexB = 0

    while indexA < len(arrA) or indexB <len(arrB):
        if indexA >= len(arrA):
            while indexB <= len(arrB) - 1:
                merged_arr[len(arrA) + indexB] = arrB[indexB]
                indexB += 1
            return merged_arr
        elif indexB >= len(arrB):
            while indexA <= len(arrA) - 1:
                merged_arr[len(arrB) + indexA] = arrA[indexA]
                indexA += 1
            return merged_arr
        else:
            if arrA[indexA] <= arrB[indexB]:
                merged_arr[indexA + indexB] = arrA[indexA]
                indexA += 1
            else:
                merged_arr[indexA + indexB] = arrB[indexB]
                indexB += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

