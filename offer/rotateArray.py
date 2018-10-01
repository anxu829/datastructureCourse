nums = [3 , 4 , 5 , 1 ,2]
start = 0
end = len(nums) -1
value = -1
while(True ):
    mid = int((start + end )/2)
    
    mid_data = nums[mid]
    
    if mid_data == nums[start] and mid_data == nums[end]:
        value = min(nums[start:end])            
        break
    if mid_data > nums[start]:
        start = mid
    if mid_data < nums[end]:
        end = mid
    if end - start == 1:
        value = nums[end]
        break

    
