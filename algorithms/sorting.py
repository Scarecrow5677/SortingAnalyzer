import random

#Standard in-place Insertionsort that uses the swap method to swap elements in the list

def Insertionsort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        ptr = i-1

        #Swap element with its left neighbor until the right place is found

        while ptr >= 0 and nums[ptr] > key:
            swap(nums, ptr, ptr+1)
            ptr -= 1

#Wrapper method for the Mergesort implementation

def Mergesort(nums):
    
    mergeSortAux(nums, 0, len(nums)- 1)

#Auxiliary method for recursive mergesort

def mergeSortAux(nums, start, end):

    #Base case

    if(start >= end):
        return

    mid = (start + end) // 2

    #recursive call on left and right half of the list

    mergeSortAux(nums, start, mid)
    mergeSortAux(nums, mid + 1, end)

    #Merge the two halves by comparing the next element in both lists

    leftP = 0
    rightP = 0
    numsP = start

    left = nums[start:mid + 1]
    right = nums[mid+1:end + 1]

    while leftP < len(left) and rightP < len(right):
        if left[leftP] <= right[rightP]:
            nums[numsP] = left[leftP]
            leftP += 1
        else:
            nums[numsP] = right[rightP]
            rightP += 1
        numsP += 1
    
    while leftP < len(left):
        nums[numsP] = left[leftP]
        numsP += 1
        leftP += 1

    while rightP < len(right):
        nums[numsP] = right[rightP]
        rightP += 1
        numsP += 1

def Countingsort(nums, k):
    counts = [0] * (k + 1)

    #count occurences of all integers from 0 to k

    for i in nums:
        counts[i] += 1

    #Calculate cumulative sums

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1] 

    out = [0] * len(nums)

    #place the numbers from the original list by looking at the index in the cumulative sums

    for i in range(len(nums) - 1, -1, -1):
        out[counts[nums[i]] - 1] = nums[i]
        counts[nums[i]] -= 1

    nums[:] = out

def Bucketsort(nums, sort):

    #find maximum of the list

    max_val = nums[0]

    for i in nums:
        if i > max_val:
            max_val = i

    if max_val == 0:
        return
    
    #create 11 buckets

    buckets = []

    for _ in range(11):
        new_list = []
        buckets.append(new_list)

    arr = nums.copy()

    #divide every element by max to get values between 0 and 1, then multiply by 10 and round down to get the index of the bucket

    for i in range(len(arr)):
        arr[i] /= max_val
        arr[i] = int(arr[i] * 10)
        buckets[arr[i]].append(nums[i])

    #sort the buckets and merge them

    out = []

    for b in buckets:
        globals()[sort](b)
        for i in b:
            out.append(i)

    nums[:] = out

#Wrapper method for Quicksort

def Quicksort(nums):

    quickSortAux(nums, 0, len(nums) - 1)

#Auxiliary method for recursive quicksort implementation

def quickSortAux(nums, start, end):

    #Base-case

    if(start >= end):
        return
    
    #get a randomized pivot

    pivot = random.randint(start, end)

    swap(nums, pivot, end)

    pivot = end

    swapP = start

    #divide elements into two sublists of smaller and bigger (or equal) ints

    for i in range(start, end):
        if nums[i] < nums[pivot]:
            swap(nums, swapP, i)
            swapP += 1
    

    swap(nums, swapP, pivot)

    #recursive call on the two sublists

    quickSortAux(nums, start, swapP-1)
    quickSortAux(nums, swapP + 1, end)

#Heapsort with a simple heap implementation as a list

def Heapsort(nums):

    #returns the index of the parent in the heap
    
    def getParent(nums, n):
        return (n-1)//2
    
    #returns the index of the left child in the heap
    
    def getLeftChild(nums, n):
        return (2*n) + 1
    
    #returns the index of the right child in the heap
    
    def getRightChild(nums, n):
        return (2*n)+2
    
    #makes sure that the maxheap condition is fulfilled for a node by making recursive swaps if necessary

    def maxHeapifyNode(nums, n, size):
        left = getLeftChild(nums, n)
        right = getRightChild(nums, n)

        #check whether there is a child with a greater value than the parent

        max = n

        if left <= size and nums[left] > nums[max]:
            max = left
        if right <= size and nums[right] > nums[max]:
            max = right
        
        if max != n:
            swap(nums, max, n)
            maxHeapifyNode(nums, max, size)

    #builds the heap by making sure the maxheap condition holds for every node

    def maxHeapify(nums, size):
        n = getParent(nums, len(nums) - 1)

        for i in range(n, -1, -1):
            maxHeapifyNode(nums, i, size)

    #sorting starts by creating the heap

    maxHeapify(nums, len(nums) - 1)

    out = []

    length = len(nums) - 1

    #sort by "removing" the root (biggest element) until every element is "removed"

    for _ in range(len(nums)):
        out.append(nums[0])
        swap(nums, 0, length)
        length -= 1
        maxHeapifyNode(nums, 0, length)

    #as we take the biggest element first, the list is sorted in descending order, so we reverse it

    out.reverse()
        
    nums[:] = out

def Selectionsort(nums):

    #search the smallest element in the unsorted sublist and swap it to the start

    for i in range(len(nums)):
        min = i
        for j in range(i + 1, len(nums)):
           if nums[j] < nums[min]:
               min= j
        swap(nums, i, min)

def Bubblesort(nums):

    #swaps an element with its right neighbor if it is bigger until the list is sorted

    while(True):
        finished = True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                swap(nums, i, i+1)
                finished = False
        if finished:
            break

#function used to swap two elements in a list

def swap(nums, x, y):

    #if the list is a visualizerlist (from sorting_visualizer), then we call the built-in swap function for visualization

    if hasattr(nums, "swap"):
        nums.swap(x, y)

    #otherwise we just do a regualr swap

    else:
        temp = nums[x]
        nums[x] = nums[y]
        nums[y] = temp