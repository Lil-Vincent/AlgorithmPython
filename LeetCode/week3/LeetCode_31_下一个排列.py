import self as self


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        k = n
        while k > 0 and nums[k - 1] >= nums[k]:
            k -= 1
        if k == 0:
            nums.reverse()
        else:
            t = k
            while t < len(nums) and nums[t] > nums[k - 1]:
                t += 1
            nums[t - 1], nums[k - 1] = nums[k - 1], nums[t - 1]
            nums[k:] = sorted(nums[k:])


if __name__ == '__main__':
    Solution.nextPermutation(self,nums=[1, 3, 2])










