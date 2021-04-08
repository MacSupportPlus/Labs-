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

first = 1 
second = 1 

while first <= 10:
    total = first * second
    print(f'{first} * {second} = {total}')
    second += 1
    if second == 11:
        first+= 1 
        second = 1

    




