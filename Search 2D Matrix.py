def searchMatrix(matrix,target):
    if not matrix or not matrix[0]:
        return False
    row=0
    for r in range(len(matrix)):
        if target==matrix[r][0] or matrix[r][-1]==target:
            return True
        elif matrix[r][0]<target and matrix[r][-1]>target:
            row=r
            break
    l,r=0,len(matrix[row])-1
    while l<=r:
        mid=(l+r)//2
        if target==matrix[row][mid]:
            return True
        elif target > matrix[row][mid]:
            l=mid+1
        else:
            r=mid-1
    return False
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3
print(searchMatrix(matrix,target))
