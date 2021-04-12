#sudo code for hw problem 1 & 2
#the total bill amount/level of service 
# make input for bill amount 
# make input for level of service 
# if elif else check for making 

# bill = float(input('Your bill is >>  '))
# service = input('This service was >>  ')
# numOfGroup = int(input('Number in group >>  '))
# if service == "good":
#     totalbill = bill * .20 + bill
#     print(f'Your bill is {totalbill}')
# elif service == "fair":
#     totalbill = bill * .15 + bill
#     print(f'Your bill is {totalbill}')
# elif service == "bad":
#     totalbill = bill * .10 + bill 
#     print(f'your bill is {totalbill}')
# print(totalbill/numOfGroup)

# number 3 of homework
# 0 coins
# ask if you want a coin 
# yes ... add a coin
# no ... break 

# coins = 0
# question = (input('Would you like a coin? >>  '))

# while question == "yes":
#     coins += 1
#     print(f'You now have {coins} coins')
#     question = (input('Would you like a coin? >>  '))
#     print(f'You now have {coins} coins')
# print("Bye have a nice day")

#Question 4 sudo code
# add place for width and height 
# take number of width and height and add ** correlating to number

# count = 0

# height = int(input('the height you want is  >> '))
# width = int(input('the width you want is >> '))
# space = '  ' * width 
# print('*  ' * width)
# while count <= height - 3:
    
#     count += 1 
#     print(f'*{space} *')
# print('*  ' * width)
# 
# 
# print a triangle    
# s = 7
# count = 1

# while count <= s :
#     print('*' * count)
#     count += 2

#number 6 multiply numbers up to 10 * 10
# grab number 1 and multiply it by one
# after the multiplication we need to increment number by 1
#after number reaches 10 we need to increment first number by 1

# first = 1 
# second = 1 

# while first <= 10:
#     total = first * second
#     print(f'{first} * {second} = {total}')
#     second += 1
#     if second == 11:
#         first+= 1 
#         second = 1

    




# arr = [4,2,5,7,23,6,5]
# # sum = 0
# # for i in arr:
# #     if sum < i:
# #         sum = i
    
# # print(sum)
# # sum = arr[0]
# # for i in arr:
# #     if i < sum:
# #         sum = i
# # print(sum)

# # for i in arr:
# #     if i%2 == 0:
# #         print(i)
# m = 4 
# sum = []
# for i in arr:
#     p = m * i
#     sum.append(p)
# print(sum)

#reverse the string 
name = "Veronica"
backwards = ""

print(name)
for i in name:
    backwards = i + backwards

print(backwards)

# 1 number
# sign -1 1
# abs 9854
# cast int => string 
# reverse string  4589
# cast str => int 
# int * sign
# num = -9854 #4589-
# sign = 1
# if num < 0:
#     sign = -1
# absNum = abs(num) # 9854 -> 4589
# numStr = str(absNum) # "9854"
# rev_num_str = ""
# for c in numStr:
#     rev_num_str = c + rev_num_str  # 4589
# result = sign  * int(rev_num_str)
# print(result)
for firstNumber in range (1,11):
        for secondNumber in range (1,11): 
            total = firstNumber * secondNumber
            print(f'{firstNumber} * {secondNumber} = {total}')
            
