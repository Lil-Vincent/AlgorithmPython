
def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    j = 0
    for i in range(len(nums)):
        if (i > j):
            return False
        j = max(j, nums[i] + i)

    return True
