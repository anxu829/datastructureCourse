class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 第一个元素，比他小的数为 0 
        if not nums  :
            return 0
        status = [1]
        max_ = 1
        for i in range(1,len(nums)):
            temp = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    temp = status[j] + 1  if status[j] + 1 > temp else temp
            if temp > max_:
                max_ = temp
            status.append(temp)
        return max_
