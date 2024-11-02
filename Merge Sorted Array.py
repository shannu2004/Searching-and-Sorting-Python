def MergeArray(nums1,nums2,m,n):
    for i in range(m,m+n):
        nums1[i]=nums2[i-n]
    nums1.sort()
nums1=[1,2,3,0,0,0]
m=3
nums2 = [2,5,6]
n = 3
MergeArray(nums1,nums2,m,n)
print(nums1)

