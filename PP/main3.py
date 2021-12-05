# using *args
def calculateMean(*list):
    if len(list) == 0:
        return "NaN"
    else:
        sum = 0
        for i in list:
            sum += i
        mean = sum / len(list)

        return round(mean, 2)


# using **kwargs
def calculateMeanbyValue(**list):
    if (len(list) == 0):
        return "NaN"
    else:
        sum = 0
        for i in list.values():
            sum += i
        mean = sum / len(list)

        return round(mean, 2)


print(f"Mean of the list by using args:", calculateMean(1, 2, 3, 5, 8, 9))
print(f"Mean of the list by using kwargs:", calculateMeanbyValue(a=1, b=2, c=3, d=5, e=8, f=9))