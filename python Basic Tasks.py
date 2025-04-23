
# Task 3
terms = int(input("Enter the number of terms for the Fibonacci series: "))
a, b = 0, 1
print("Fibonacci series:", end="")
for _ in range(terms):
  print(a, end=" ")
  a, b = b, a + b

# Task 1
# def calculateGrade(num):
#     if(num<=100 and num>=91):
#         print('Grade is A!')
#     elif(num<=90 and num>=81):
#         print('Grade is B!')
#     elif(num<=80 and num>=71):
#         print('Grade is C!')
#     elif(num<=70 and num>=61):
#         print('Grade is D!')
#     elif(num<=60 and num>=51):
#         print('Grade is E!')
#     else:
#         print('Grade is F!')

# marks = eval(input('Enter your marks : '))
# calculateGrade(marks)

# Question 22
# n = int(input("Enter the value of n: "))
# sum_series = 0

# for i in range(1, n + 1):
#     sum_series += 1 / i

# print(f'The sum of the series up to 1/{n} is: ', sum_series)

# Question 21
# def printTable(num):
#     for i in range(1,11):
#         print(num, ' x ', i, ' = ', num*i)
        
# printTable(10)

# Question 20
# def factorial(num):
#     fact = 1 
#     for i in range(1,num+1):
#         fact *= i
#     return fact

# num = eval(input('Enter a number: '))
# print('The factorial of ', num, ' is : ', factorial(num))

# Question 19
# income = float(input("Enter your income: "))

# if income <= 10000:
#     tax = income * 0.05
# elif 10001 <= income <= 50000:
#     tax = income * 0.10
# else:
#     tax = income * 0.15

# print("Your tax is:", tax)

# Question 18
# n = 1
# while True:
#     if n * (n + 1) / 2 > 1000:
#         break
#     n += 1
# print("The smallest positive integer n is:", n)

# Question 17
# def determiningDayOfWeek(num):
#     match num:
#         case 1:
#             print('Monday!')
#         case 2:
#             print('Tuesday!')
#         case 3:
#             print('Wednesday!')
#         case 4:
#             print('Thursday!')
#         case 5:
#             print('Friday!')
#         case 6:
#             print('Saturday!')
#         case 7:
#             print('Sunday!')
#         case _:
#             print('Enter a valid number (1-7)!')

# num = eval(input('Enter day number : '))
# determiningDayOfWeek(num)

# Question 16
# def calculateGrade(num):
#     if(num>=90):
#         print('Grade is A!')
#     elif(num<=89 and num>=80):
#         print('Grade is B!')
#     elif(num<=79 and num>=70):
#         print('Grade is C!')
#     elif(num<=69 and num>=60):
#         print('Grade is C!')
#     else:
#         print('Fail!')

# marks = eval(input('Enter your marks : '))
# calculateGrade(marks)

# Question 15
# number = eval(input('Enter a number: '))

# if(number > 0):
#     print('The number is positive!')
# elif(number < 0):
#     print('The number is negative!')
# else:
#     print('The number is zero!')

# Question 14
# number = eval(input('Enter a number: '))

# if(number>10):
#     print('The number is greater than 10')
# else:
#     print('The number is less than or equal to 10')

# Question 13
# import math

# num1 = eval(input('Enter 1st number : '))
# num2 = eval(input('Enter 2nd number : '))

# if(math.pow(num1,2) == num2):
#     print(num2,' is the square of ',num1)
# else:
#     print(num2,' is not the square of ',num1)

# Question 12
# def check_marks(marks):
#     if marks >= 90:
#         print("Congratulations! You have 90 percent or more marks.")
#     else:
#         print("Keep trying! You need to score 90 percent or more.")

# marks = float(input("Enter your marks: "))
# if 0 <= marks <= 100:
#     check_marks(marks)
# else:
#     print("Please enter marks between 0 and 100.")
    
# Question 11
# currentElectricityRate = eval(input('Enter the current rate of electricity : '))
# g = eval(input('Enter g : '))
# petrolPerLiter = eval(input('Enter petrol per liter : '))
# print('After 10% price hike : ')
# currentElectricityRate += (currentElectricityRate/10)
# g += (g/10)
# petrolPerLiter += (petrolPerLiter/10)

# print('Rate of electricity : ',currentElectricityRate)
# print('g : ',g)
# print('Petrol per liter : ',petrolPerLiter)

# Question 7
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")    

# Question 6
# distance = float(input("Enter distance (km): "))
# speed = float(input("Enter speed (km/h): "))
# time = distance / speed
# print("Time to reach destination (hours): ", time)
 
# Question 5
# var1 = 33
# var2 = 15
# print("Before swap: ")
# print("Var1: ",var1)
# print("Var2: ",var2)
# # Swapping
# var1 = var1 + var2  
# var2 = var1 - var2 
# var1 = var1 - var2 

# print("After swap: ")
# print("Var1: ",var1)
# print("Var2: ",var2)

# Question 4
# var1 = 25
# var2 = 91
# print("Before swap: ")
# print("Var1: ",var1)
# print("Var2: ",var2)
# # Swapping
# var3=var1
# var1=var2
# var2=var3

# print("After swap: ")
# print("Var1: ",var1)
# print("Var2: ",var2)


#  ******Question 3**********
# height = 6
# width = 7
# Area = height * width
# print("Area of Square: ", Area)

#  ******Question 2**********
# number = 10
# print("Initial value:", number)
# print("Compound assignment using +=")
# number += 5 
# print("After += 5:", number)
# print("Compound assignment using -=")
# number -= 3
# print("After -= 3:", number)
# print("Compound assignment using *=")
# number *= 2  
# print("After *= 2:", number)

#  ******Question 1**********
# import math
# radius = float(input("Enter radius of circle: "))
# circumference = 2 * math.pi * radius
# print("Circumference of circle: ", circumference)

#  ******Question 10**********
# number = 123
# reverse_number = []
# print("Actual Number: ",number)
# while(number>=1):
#     reverse = int(number % 10)
#     reverse_number.append(reverse)
#     number = int(number / 10)
# print("Reversed Number: ",reverse_number)

#  ******Question 9**********
# temperature_in_celsius = 25.6
# temperature_in_fahrenheit = 9/5 * temperature_in_celsius + 32
# print("Temperature in Fahrenheit: ",temperature_in_fahrenheit)

#  ******Question 8********** 
# base = float(input("Enter base: "))
# height = float(input("Enter height: "))
# Area = 1/2 * base * height
# print("Area: ", Area)
