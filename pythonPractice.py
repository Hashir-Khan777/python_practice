# Assignment # 1
# print("Hashir Khan")

# Assignment 2
# eng = 70
# isl = 60
# maths = 100
# totalMarks = 300
# percentage = (eng + isl + maths) / totalMarks * 100
# if (round(percentage) >= 80):
#     print("Grade A")
# elif (round(percentage) >= 70):
#     print("Grade B")
# elif (round(percentage) >= 60):
#     print("Grade C")
# else:
#     print("Grade F")

# Assignment 3
# part 1

# print(
#     "Twinkle, twinkle, little star,\n         How I wonder what you are!\n                Up above the world so high,\n                Like a diamond in the sky.\nTwinkle, twinkle, little star\n         How I wonder what you are!"
# )

# part 2
# import sys

# print("My python version is: ", sys.version)

# part 3
# import datetime

# print("Today date and time is: ",
#       datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

# part 4
# radiusOfTheCircle = float(input("Enter radius of circle "))
# areaOfTheCircle = round(float(3.14) * radiusOfTheCircle * radiusOfTheCircle, 2)
# print("Area of the circle is: ", areaOfTheCircle)

# part 5
# firstName = input("Enter your first name: ")
# lastName = input("Enter your last name: ")
# print("Your reverse name is: " + lastName + " " + firstName)

# part 6
# value1 = int(input("Enter first number: "))
# value2 = int(input("Enter second number: "))
# print("Sum of two numbers is: ", value1 + value2)

# part 7
# eng = int(input("Enter your English marks: "))
# sci = int(input("Enter your Science marks: "))
# com = int(input("Enter your computer marks: "))
# isl = int(input("Enter your islamiat marks: "))
# urd = int(input("Enter your Urdu marks: "))
# percentage = (eng + sci + com + isl + urd) / 425 * 100
# mark_sheet = {
#     "English": eng,
#     "Science": sci,
#     "Computer": com,
#     "islamiat": isl,
#     "Urdu": urd,
#     "percecentage": str(round(percentage)) + "%"
# }
# print(mark_sheet)

# part 8
# num = int(input("Enter any number: "))
# if (num % 2 == 0):
#     print("Number is even")
# else:
#     print("Number is odd")

# part 9
# list = [1, 2, 3.53, "4", "Hashir", True, 7, 8, 9, 10]
# print("The length of list is: ", len(list))

# part 10
# list = [1, 2, 3.53, "4", "Hashir", True, 7, 8, 9, 10]
# numList = []
# total = 0
# for num in list:
#     if (type(num) == int or type(num) == float):
#         numList.append(num)
# if (len(numList) != 0):
#     for num in range(len(numList)):
#         total = total + numList[num]
# print("The sum of all numbers in list is: ", total)

# part 11
# list = [10, 20, 4, 45, 99]
# list.sort()
# print("The largest number in given list is: ", list[-1])

# part 12
# lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for num in lst:
#     if (num < 5):
#         print(num)

#  My practice

# table in python
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# for i in range(1, (num2 + 1)):
#     print(num1, "x", i, "=", num1 * i)

# List comprehension
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# lst = [num1 * i for i in range(1, (num2 + 1))]
# print(lst)

# print even numbers in using list comprehension
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# lst = [i for i in range(num1, (num2 + 1)) if i % 2 == 0]
# print(lst)

# transpose of matrix
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# transpose = []

# for i in range(len(matrix[0])):
#     row = []
#     for j in matrix:
#         row.append(j[i])
#     transpose.append(row)

# print(transpose)

# transpose of matrix using list comprehension
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# print(transpose)
