def City(costs):
    costs=sorted(costs,key=lambda x:x[0]-x[1])
    c1=0
    c2=0
    n=len(costs)//2
    for i in range(n):
        c1+=costs[i][0]
    for i in range(n, len(costs)):
        c2+=costs[i][1]
    return c1+c2
costs = [[10,20],[30,200],[400,50],[30,20]]
total = City(costs)
print(total)

#TC = O(NlogN)
