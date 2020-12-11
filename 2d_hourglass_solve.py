def solve_hourglass (array):
    s =  str("indices:")
    for i in range(0, len(array[0])):
        s += " " + str(i)
    print (s)
    blocks = list()
    for y in range (0,4):
        for x in range (0,4):
            if y < 3:
                block = getTopQuadrants(array[y:y+3], x)
            else:
                block = getBottomQuadrant( makeList(array[y:], array[0:y-2]), x)
            print('block-->', block , "\n")
            blocks.append(block)
    sums = list()
    for block in blocks:
        sum = 0
        x = 0
        topRow = block[0][0] + block[0][1] + block[0][2]
        d = block[1][1]
        bottomRow = block[2][0] + block[2][1] + block[2][2]
        sum = topRow + d + bottomRow
        sums.append(sum)
    print("Total blocks->",len(blocks))
    print("Total sums->",len(sums))
    print(sums)
    sums.sort()

    print("Greatest sum=>", sums[len(sums)-1])
    return sums[len(sums)-1]
    
def getTopQuadrants(rows, x):

    line1 = rows[0]
    line2 = rows[1]
    line3 = rows[2]
    if x < 3:
        column1 = line1[x:x+3] 
        column2 = line2[x:x+3]
        column3 = line3[x:x+3]
    else:
        column1= makeList(line1[x:],line1[:x-3])
        column2= makeList(line2[x:],line2[:x-3])
        column3= makeList(line3[x:],line3[:x-3])
    
    return list([column1, column2, column3])

def getBottomQuadrant(rows, x):
    line1 = rows[0]
    line2 = rows[1]
    line3 = rows[2]
    if x < 3:
        column1 = line1[x:x+3] 
        column2 = line2[x:x+3]
        column3 = line3[x:x+3]
    else:
        column1= makeList(line1[x:], line1[:x-3])
        column2= makeList(line2[x:], line2[:x-3])
        column3= makeList(line3[x:], line3[:x-3])
    
    return list([column1, column2, column3])

def makeList(l1, l2):
    newList = list()
    for i in range(len(l1)):
        newList.append(l1[i])
    for j in range(len(l2)):
        newList.append(l2[j])
    return newList


if __name__ == "__main__": 
    array = []
    y = 0
    txtFile = open("hourglass_test.txt").readlines()
    for _ in range(6):
        array.append(list(map(int, txtFile[_].rstrip().split())))
    print(array)
    solve_hourglass(array)