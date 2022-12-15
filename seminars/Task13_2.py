def sinoptik(N):
    days=[]
    for _ in range(N):
        days.append(round(random.uniform(-10,50),0))  
    print(days)
    maxPeriod = maxPeriodResult = 0
    i = 0
    while i<N-1:
        if days[i]>0:
            while days[i]>0 and i<N-1:
                maxPeriod+=1
                i+=1
            if maxPeriodResult<maxPeriod: maxPeriodResult=maxPeriod
        maxPeriod=0
        i+=1
    return maxPeriodResult