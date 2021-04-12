# def min(list):
#     current_min = list[0]  # Start by using the first number as the smallest
#     for num in list:       # Loop through each number in the list
#         if num < current_min:
#             current_min = num  
#     return current_min

# answer = min([1,2,3,-1])
# print(answer)

# def max(list):
#     currentMax = 0
#     for num in list:
#         if num > currentMax:
#             currentMax = num
#     return currentMax

# answer = max([1,2,3,6])
# print(answer)

# def shortest(list):
#     short = len(list[0])
#     for string in list:
#         if short > len(string):
#             return string






# answer = shortest([['i','d','t','v'], ['r','u'], ['u','y','o']])
# print(answer)

def longest(list):
    long = 0
    for string in list:
        if len(string) > long :
            return string






answer = longest([['i','d','t','v'], ['r','u'], ['u','y','o']])
print(answer)