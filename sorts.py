'''This file is meant to act as a sort
of practice grounds for different key sorting
algorithms as well as providing supplemental
reasoning for why one would choose each algorithm
in the form of comments'''

# 05/09/20

#Insertion Sort - Good for small number of elements, lists that are almost sorted
'''Time complexity is O(n^2), Space complexity
is O(1). Insertion sort sorts in place, and is Stable'''


def insertionsort(arr):
    for i in range(1,len(arr)):

        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key


nums = [5, 2, 4, 8, 2, 4, 1, 8]
insertionsort(nums)
for i in range(len(nums)):
    print(nums[i])

tups = [(2, 9), (8, 5), (4, 3), (4, 2), (7, 1)]
insertionsort(tups)
for i in range(len(tups)):
    print(tups[i])

print("\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\n")


'''MergeSort - A divide and Conquer algorithm

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergesort(L)
        mergesort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
'''

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergesort(L)
        mergesort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1





def printlist(arr):
    print("List is as follows: ")
    for i in range(0, len(arr)):
        print(arr[i])


list1 = [5,4,3,1,2]
print(list1)
print("Performing mergesort...")
mergesort(list1)
printlist(list1)
