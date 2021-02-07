

def twoSumBruteForce(nums, target):
    """
    Uses a brute force technique to solve the twosum problem
    TC: O(n^2)
    SC: O(1)
    """
    for i in range(len(nums)-1):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]

def twoSumEfficient(nums, target):
    """
    """
    pass



if __name__ == "__main__":
    print(twoSumBruteForce([2,7,11,15], 9))