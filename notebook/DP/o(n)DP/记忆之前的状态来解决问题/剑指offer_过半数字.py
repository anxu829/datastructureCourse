class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        state = numbers[0]
        count = 1
        for idx in range(1,len(numbers)):
            if numbers[idx] == state:
                count +=1
            else:
                if count == 1:
                    state = numbers[idx]
                else:
                    count -= 1
        if count > 1:
            return state
        else:
            return 0
            
if __name__ == "__main__":
    lis = [2,2,2,2,2,1,3,4,5]
    k = Solution().MoreThanHalfNum_Solution(lis)
    print(k)
