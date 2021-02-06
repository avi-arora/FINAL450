

def largestSumBruteForce(arr):
    """
    TC: O(N^2)
    SC: O(1)
    """
    largest = arr[0]
    for i in range(0, len(arr)):
        j = i+1
        temp = arr[i] 
        while j < len(arr):
            temp += arr[j]
            j+=1
        if temp > largest:
            largest = temp
    
    return largest

def largestSumUsingDAC(arr, start, end):
    """
    TC: 
    SC:
    """
    def maxCrossingSum(arr, start,mid, end):
        right_sum = arr[mid+1]
        


    if start == end:
        return arr[start]
    else:
        mid_index = (start + end)//2
        crossMax = maxCrossingSum(arr,start, min_index, end)
        leftMax = largestSumUsingDAC(arr, start, mid_index)
        rightMax = largestSumUsingDAC(arr, mid_index+1, end)

        return max(midelem, leftMax, rightMax)

def largestSumUsingKadane(arr, size):
    """
    TC: 
    SC:
    """
    pass


if __name__ == "__main__":
    arr = [-1,-2,-3,-4]
    print(largestSumBruteForce(arr))
    print(largestSumUsingDAC(arr, 0, len(arr)-1))