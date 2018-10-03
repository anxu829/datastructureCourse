nums = [4 ,1 , 7 , 6 , 9 ,2 , 8 , 0 , 3 , 5]

def quikSort(nums, start , end):
    # print(start,end)
    if start == end:
        return
    if end - start == 1:
        a = max(nums[start],nums[end])
        b = min(nums[end],nums[start])
        nums[start] = b 
        nums[end] = a
    else:
        left = start
        right = end
        key = end
        while(left < right):
            while(left < right and nums[left] < nums[key]):
                left += 1
            while(left < right and nums[right] >= nums[key]):
                right -=1
            nums[left] , nums[right] = nums[right] , nums[left]
        nums[right] , nums[key] = nums[key] , nums[right]
        print(nums,start,right)
        
        if start <= right -1:
            quikSort(nums,start,right - 1)
        if right +1 <= end:
            quikSort(nums,right+1,end)

quikSort(nums,0,len(nums)-1)
