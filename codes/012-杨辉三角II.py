
def getRow(rowIndex):
    triangle = [1]
    for i in range(rowIndex):
        tmp = [1, 1]
        for j in range(1, i+1):
            tmp.insert(j, triangle[j-1] + triangle[j])
        triangle = tmp
    return triangle


print(getRow(3))
