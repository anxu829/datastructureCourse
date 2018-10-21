# 本题目对应着一种非常常见的递归方式：
# 递归维护的数组 dp[i]的计算需要考虑前面所有的 j < i 的dp[j] ，从而使得时间复杂度为 o(n^2)
# 类似的题目还有leetcode，最长递增子序列

# 思路： maxMul 记录着最大的乘积结果
# 
# maxMul[1] = 1
# maxMul[2] = 2
# maxMul[3] = 3
# def cut(N):

N = 8
maxMul  = [0] * (N+1)
# 0 位是用来占位置的
maxMul[0] = 1
maxMul[1] = 1
maxMul[2] = 2
maxMul[3] = 3
for n in range(4,N+1):
    # 需要解决f(n) 的问题：
    maxCut = 0
    for  i in range(1,n):
        maxCut = max(maxCut,maxMul[i] * maxMul[n-i])
    maxMul[n] = maxCut


