# n = int(input())

# #top half
# for i in range((n+1)//2):
#     for j in range(n):
#         print(j+n*i*2+1, end=" ")
#     print()


# #bottom half
# for i in range(n-((n+1)//2)):
#     print (((i*(n-1)//2)*n)-1)
#     for j in range(n):
#         print(j, end=" ")
#     print()
#     

# def nextP():
#     global n,m
#     i=j=0
#     while True:
#         for j in range(j,j+m):
#             yield i,j
#         for i in range(i+1,i+n):
#             yield i,j
#         for j in range(j-1,j-m,-1):
#             yield i,j
#         for i in range(i-1,i-n+1,-1):
#             yield i,j
#         n,m,j=n-2,m-2,j+1


# n,m=list(map(int,input().strip().split()))
# matrix=[input().strip().split() for i in range(n)]
# out = []

# pGen=nextP()
# for k in range(n*m):
#     i,j=next(pGen)
#     out.append(matrix[i][j])

# for i in out:
#   print(int(i), end=" ")

# import numpy as np 

# alldata = list(map(int, (input().strip().split())))

# if (len(alldata)==2):

#     m, n = alldata[0], alldata[1]

#     edata = list(map(int, (input().strip().split())))

#     matrix = np.array(edata).reshape(m,n)


# else:

#     m, n = alldata[0], alldata[1]

#     matrix = np.array(alldata[2:]).reshape(m,n)


# col_sum = np.sum(matrix, axis=0)

# row_sum = np.sum(matrix, axis=1)


# if(np.amax(col_sum)>np.amax(row_sum)):
#     print("column", col_sum.argmax(), np.amax(col_sum))
# else:
#     print("row", row_sum.argmax(), np.amax(row_sum))


# n = int(input())

# p = n

# for i in range(0,n,2):
#     k = (i-1)*n+1
#     for j in range(n-1):
#         print(k)
#         k+=1
#     

from firebase import firebase
from sys import argv

operation = argv[1]
name = argv[2]

# if (len(argv)>3):
#        m1 = argv[3]
#        m2 = argv[4]
#        m3 = argv[5]

# data = [name,m1,m2,m3]

firebase = firebase.FirebaseApplication("https://rnis-demo.firebaseio.com/")


if(operation=='add'):

    res = firebase.post('/', data)

    print 'Data added successfully'

elif(operation=='get'):

    res = firebase.get('/', None)

    for key in res:

        if (res[key][0]==name):
                    print((int(res[key][1])+int(res[key][2])+int(res[key][3]))/3)


else:
    print("invalid command")