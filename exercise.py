# 003111 # 3 = 1 + 1 + 1
# 813372 # 8 + 1 + 3 = 3 + 7 + 2
# 17935 # 1 + 7 = 3 + 5
# 56328116 # 5 + 6 + 3 + 2 = 8 + 1 + 1 + 6
#
# Your task is to write a method luckCheck(str), which returns true if argument is string
# decimal representation of a lucky ticket number, or false for all other numbers.
# It should handle errors for empty strings or strings which don't represent a decimal number.

def luckCheck(str):
    stringList = list(str)
    leftSum = 0
    rightSum = 0
    half = int(len(stringList) / 2)

    for i in range(0, half):
        leftSum += int(stringList[i])

    for j in range(half, len(stringList)):
        rightSum += int(stringList[j])


    if str == '':
        print("false")
    elif leftSum == rightSum:
        print("true")
    else:
        print("false")

    print(stringList)


luckCheck('')  # False
luckCheck('003111')  # True
luckCheck('813372')  # True
luckCheck('56328116')  # True
luckCheck('17935')  # True
luckCheck('12345678')  # False
