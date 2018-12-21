#!/bin/python3

def nextMove(posr, posc, rn , cn , board):
    r = posr
    c = posc

    #find min dist from dirty cell to bot
    x = 100
    min = []
    for i in range(len(l)):
        if l[i] < x:
            x = l[i]
    #check how many cells have same min dist
    for i in range(len(l)):
        if l[i] == x:
            min.append(i)

    #if more than one cell has min dist ,then find agj cell of each dirty cell

    adj = []
    # flag = 1
    if(len(min) > 1):

        for i in min:
            count = 0;
            for j in dirty:

                x = dist(dirty[i][0],dirty[i][1],j[0],j[1])
                if(x == 1.0 or x == 1 or x == 1.4142135623730951 or (x > 1.4 and x < 1.42)):
                    count+=1
            adj.append(count)

            # find dirty cell with least adj cells
            x = 100
        for i in range(len(adj)):
            if adj[i] < x:
                x = adj[i]
                min_val = i

         # assign selected dirty cells position
        r1 = dirty[min[min_val]][0]
        c1 = dirty[min[min_val]][1]


        adj2 = []
        min2 = []
        for i in range(len(adj)):
            if adj[i] == x:
                min2.append(i)

        if (len(min2) > 1):
            for i in min2:
                count = 0
                for j in dirty:
                    x = dist(dirty[min[i]][0], dirty[min[i]][1], j[0], j[1])
                    if (x == 2.0 or x == 2.23606797749979 or (x > 2.1 and x < 2.3)):
                        count += 1

                adj2.append(count)
            x = 100
            for i in range(len(adj2)):
                if adj2[i] < x:
                    x = adj2[i]
                    min_val = i

            # assign selected dirty cells position
            r1 = dirty[min[min2[min_val]]][0]
            c1 = dirty[min[min2[min_val]]][1]








    else:
        # assign selected dirty cells position
        r1 = dirty[min[0]][0]
        c1 = dirty[min[0]][1]

    #assign selected dirty cells position



    #find the next move of bot
    if (r == r1 and c == c1):
        return 5

    if (r == r1):
        if (c1 < c):
            return 1
        else:
            return 2
    if c == c1:
        if r1 < r:
            return 3
        else:
            return 4

    if r == r1 + 1 or r == r1 - 1:
        if c1 < c:
            return 1
        else:
            return 2

    if r < r1:
        return 4
    else:
        return 3




from math import sqrt

def dist(a,b,c,d):
    res = sqrt(((c-a)**2)+((d-b)**2))
    return (res)

l = []


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    dirty = []


#find dirty cells
    for i in range(dim[0]):
        for j in range(dim[1]):
            if (board[i][j] == 'd'):
                temp = [i, j]
                dirty.append(temp)

#find dist of each dirty cell wrt to bot position
    for i in dirty:
        l.append(dist(pos[0],pos[1],i[0],i[1]))


    a = nextMove(pos[0], pos[1], dim[0], dim[1], board)
    # print(pos)
    # print(dim)
    # exit()


    if a == 1:
        print('LEFT')


    if a == 2:
        print('RIGHT')


    if a == 3:
        print('UP')


    if a == 4:
        print('DOWN')


    if a == 5:
        print('CLEAN')


