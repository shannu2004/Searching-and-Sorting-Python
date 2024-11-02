def Ranks(score):
    score_sort=sorted(score,reverse=True)
    d={}
    answer=[]
    print(score_sort)
    for i in range(len(score_sort)):
        if i ==0:
            d[score_sort[i]]="Gold Medal"
        elif i==1:
            d[score_sort[i]]="Silver Medal"
        elif i==2:
            d[score_sort[i]]="Bronze Medal"
        else:
            d[score_sort[i]]=str(i+1)
    for i in range(len(score)):
        answer.append(d[score[i]])
    return answer

score = [5,4,3,2,1]
print(Ranks(score))
