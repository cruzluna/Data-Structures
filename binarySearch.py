# trying to code binary search without reference
# [ 1 2 3 4 5 6 7 8] length: 8 target: 7
def bisect(arr: list, target: int) -> int:
    '''
    assumes number is in list
    return the index of target number
    '''
    n = len(arr)
    beg = 0
    middle = (n-1)//2
    end = n-1
    if arr[middle] == target:
        #middle happens to be the number we want
        return middle
    
    while beg < end: #prevents points from intersecting
        if arr[beg] == target:
            break
        if arr[middle] < target:
            #concerned with right side of array
            #beginning becomes n+1/2
            beg = middle + 1
            middle = (beg + end  )//2
        elif arr[middle] > target:
            #left side of array
            end = middle -1
            middle = (beg + end)//2
    
    #index        
    return beg 

 
def bisect2(arr: list, target: int) -> int:  
    '''
    source: mCoding
    return index of target
    '''   
    low = 0
    high = len(arr)
    while low < high:
        #decrease pointers until they meet
        middle = (low + high)//2
        if arr[middle] < target:
            #concerned with right side 
            low = middle + 1
        else:
            high = middle
    return low #could also return high
    
arr1 = [1, 2, 3, 4, 5 ,6, 7, 8]
print(bisect(arr1,7))

#LEET CODE SOLUTION
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #BISECT LEFT
        low = 0
        high = len(nums)-1
        
        while low <= high:
            #decrease pointers until they meet
            middle = (low + high)//2
            if nums[middle] < target:
                #concerned with right side 
                low = middle + 1
            elif nums[middle] > target:
                #left side
                high = middle - 1
            else:
                return middle
        return -1 #could also return high