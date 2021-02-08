

def largestSumBruteForce(arr):
    """
    Algorithm
    1. find all subarrays
    2. find sum of all subarrays
    3. find largest/smallest from the sum of all subarrays
    TC: O(N^2)
    SC: O(1)
    """
    #step 1
    subarr = []
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            temp = []
            for x in range(i,j+1):
                temp.append(arr[x])
            subarr.append(temp)
    
    #step 2
    sums = [sum(x) for x in subarr]

    #step 3
    return max(sums)
            
    
    

def largestSumUsingDAC(arr, start, end):
    """
    TC: 
    SC:
    """
    pass

def largestSumUsingKadane(arr, size):
    """
    TC: 
    SC:
    """
    pass


if __name__ == "__main__":
    arr = [-2,-3,4,-1,-2,1,5,-3]
    print(largestSumBruteForce(arr))
   # print(largestSumBruteForce([1,2,3,4]))
    