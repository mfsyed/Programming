def getRow(rowIndex):
    rowI = [1]
    memo = {0:[1],1:[1,1]}

    if rowIndex in memo:
        return memo[rowIndex]

    prev = getRow(rowIndex-1)


    for i in range(len(prev)-1):
        rowI.append(prev[i]+prev[i+1])


    rowI.append(1)

    memo[rowIndex] = rowI

    return rowI


print(getRow(9))
