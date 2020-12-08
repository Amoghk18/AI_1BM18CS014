noPred = 0
noArg = [None for i in range(10)]
nouse = ''
predicate = [None for i in range(10)]
argument = [[None for i in range(10)] for i in range(10)]


def main():
    global noPred
    char = 'y'
    while(char == 'y'):
        noPred = int(input("Enter Number of Predicates: "))
        for i in range(noPred):
            print("Enter the predicate ", (i+1), " :")
            predicate[i] = input()
            print("Enter No.of Arguments for thePredicate ", predicate[i], " :")
            noArg[i] = int(input())

            for j in range(noArg[i]):
                print("Enter argument ", j+1, " :")
                argument[i][j] = input()

        printPredicate()
        check_arg_pred()
        char = input("Do you want to continue(y/n):   ")


def printPredicate():

    print("*PREDICATES ARE*")
    for i in range(noPred):
        print(predicate[i], "(", end="")
        for j in range(noArg[i]):
            print(argument[i][j], end="")
            if(j != noArg[i]-1):
                print(",", end="")
        print(")")


def unify():
    flag = 0
    for i in range(noPred-1):
        for j in range(noArg[i]):
            if(argument[i][j] != argument[i+1][j]):
                flag = 0
                if(flag == 0):
                    print("The substitution is : ", end="")
                    print(argument[i+1][j], "/", argument[i][j])
                    flag += 1

        if(flag == 0):
            print("Arguments are Identical, so no substitution")
            flag += 1


def check_arg_pred():
    predflag = 0
    argflag = 0

   
    for i in range(noPred-1):
        if(predicate[i] != predicate[i+1]):
            print("Not same, Unification cannot be done")
            predflag = 1
            break


    if(predflag != 1):
        ind = 0
        key = noArg[ind]
        length = len(noArg)
        for i in range(0, key-1):
            if i >= key:
                continue
            if ind != length - 1:
                ind += 1
                key = noArg[ind]
            if(noArg[i] != noArg[i+1]):

                print("Number of arguments are not same")
                argflag = 1
                break

        if(argflag == 0 and predflag != 1):
            unify()


main()