def SmallElement(matrix,k):
    flat=[e for sub in matrix for e in sub]
    flat.sort()
    return flat[k-1]

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(SmallElement(matrix,k))

