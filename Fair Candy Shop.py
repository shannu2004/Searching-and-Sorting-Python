def candy(alice,bob):
    sumA,sumB=sum(alice),sum(bob)
    setB=set(bob)
    target=(sumA+sumB)/2
    for c in alice:
        diff=target-(sumA-c)
        if diff in setB:
            return [c,diff]
    return []
alice=[1,1]
bob=[2,2]
print(candy(alice,bob))
