def arrayPairSum(nums):
    nums.sort()
    m_sum=sum(nums[i] for i in range(0,len(nums),2))
    return m_sum
nums=[1,2,3,4]
print(arrayPairSum(nums))
