floor1 = [[1, 0, 0, 0],
          [0, 1, 0, 1],
          [1, 0, 1, 1]]

floor2 = [[1, 1, 0, 0, 1, 0, 0],
          [0, 0, 0, 1, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 1],
          [0, 1, 0, 1, 0, 1, 0]]


def printFloor(floor, i, j):
    for i1 in range(len(floor)):
        for j1 in range(len(floor[i1])):
            if i == i1 and j == j1:
                print('X ', end="")
            else:
                print(str(floor[i1][j1]) + " ", end="")
        print()
    print()



def clean(floor, i, j):
    floor[i][j] = 0
    return floor

def startCleaning(floor):
    
    for i in range(len(floor)):
        if i % 2 == 0:
            for j in range(len(floor[i])):
                if floor[i][j] == 1:
                    floor = clean(floor, i, j)
                printFloor(floor, i, j)
        else:
            for j in range(len(floor[i])-1, -1, -1):
                if floor[i][j] == 1:
                    floor = clean(floor, i, j)
                printFloor(floor, i, j)
        

def start():
    newFloor = []
    r = int(input("Enter number of rows : "))
    for i in range(r):
        temp = list(map(int, input().split(" ")))
        newFloor.append(temp) 
    print("**************** Your Floor *****************")
    printFloor(newFloor, -1, -1)
    print("*********************************************")
    startCleaning(newFloor)
        
start()