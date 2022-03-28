a = [5, 6, 7]
b = [3, 6, 10]

def compareTriplets(a, b):
    score = [0,0]
    for an in a:
        i = a.index(an)
        if a[i] == b[i]:
            score[0] = score[0] + 0
            score[1] = score[1] + 0
        elif a[i] > b[i]:
            score[0] = score[0] + 1
        else:
            score[1] = score[1] + 1
    return score
        

print(compareTriplets(a, b))
