import time
import gui.Gui as Gui
from algorithms import sorting

#Function that calls one of the sorting algorithms and measures the time it takes to finish sorting

def measure(alg, nums, counting_sort_limit = -1, bucket_sort_alg = ""):
    start = 0
    end = 0

    #specific call for Countingsort (needs extra argument)

    if counting_sort_limit != -1:
        start = time.time_ns()

        getattr(sorting, alg)(nums, counting_sort_limit)

        end = (time.time_ns() - start) / 1000000

        if not checkSorted(nums):
            raise RuntimeError("An unknown error occured while sorting")

    #specific call for Bucketsort (needs extra argument)

    elif bucket_sort_alg != "":
        start = time.time_ns()

        getattr(sorting, alg)(nums, bucket_sort_alg)

        end = (time.time_ns() - start) / 1000000

        if not checkSorted(nums):
            raise RuntimeError("An unknown error occured while sorting")

    else:
        start = time.time_ns()

        getattr(sorting, alg)(nums)

        end = (time.time_ns() - start) / 1000000

        if not checkSorted(nums):
            raise RuntimeError("An unknown error occured while sorting")

    return end

#used for assertions, checks whether a list is sorted in ascending order

def checkSorted(nums):
    for i in range(1, len(nums)):

        #if the previous element was larger than the current, the list is not sorted correctly

        if nums[i-1] > nums[i]:
            return False
    return True

#Starts the program by creating the Gui

if __name__ == "__main__":

    #Initialize window

    gui = Gui.Gui()
   
    
