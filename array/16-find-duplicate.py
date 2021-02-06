
def findDuplicate_floyd(arr):
    """
    
    Find duplicate number in array using floyd cycle detection algorithm.
    
    TC: O(n)
    SC: O(1)
    
    we will do floyd detection in two phases
    phase 1: detect the cycle
    phase 2: point slow to start and point fast to where it was when cycle was detected, 
    move them 1 by 1, whem they met, it was the cycle entry point
    """
    #phase 1
    slow, fast = 0, 0
    slow, fast = arr[slow], arr[arr[fast]]
    while True:
        if slow == fast:
            break
        slow, fast = arr[slow], arr[arr[fast]]
    
    #phase 2
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return arr[slow] # or fast 
    

def findDuplicateUsingSet(arr):
    """
    find duplicate using set
    TC: O(n)
    SC: O(n)
    """
    s = set([])
    for x in range(len(arr)):
        if arr[x] in s:
            return arr[x]
        s.add(arr[x])

    return -1


def findDuplicateUsingSorting(arr):
    """
    """
    pass


if __name__ == "__main__":
    arr = [1,3,4,2,2]
    print(findDuplicateUsingSet(arr))
    print(findDuplicate_floyd(arr))
    

