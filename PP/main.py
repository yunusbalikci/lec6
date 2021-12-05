def calculateAvgFromList(list):
    sum=0
    for elem in list:
        sum+=elem
    return round(sum/len(list),2)

a=[2,3,4,3,4,5,2,1,7,7,5]
avg=calculateAvgFromList(a)
print(f"mean value: {avg}")