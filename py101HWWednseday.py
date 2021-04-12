#Question 1

# listOne = [2,4,5]
# listTwo = [2,3,6]
# #get the first digit of the first list and multiply by first and second digit
# totalList = []
# for i in listOne:
#     answer = i * listTwo[i]
#     totalList.append(answer)

# print(totalList)

#Question 2 & 3 Matrix of any size 

# matrixOne = [[1,3], [2,4]]
# matrixTwo = [[5,2], [1,0]]

# matrixSum = [[0,0], [0,0]]
# for i in range(len(matrixOne)):
#     for x in range(len(matrixOne[0])):
#         matrixSum[i][x]= matrixOne[i][x] + matrixTwo[i][x]
# for r in matrixSum:
#     print(r)

listOne = "e,d,e,w,c,s,f,g,h,p,p,d,e"
listTwo = ""
for i in range(len(listOne)):
    for x in range(len(listOne)):
        if i != x:
            i + listOne[i] = listTwo
print(listTwo)
        