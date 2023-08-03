# if statement...............

# a=20
# b=200
# if b>a:
#     print("b is greater than a")

# elif statement..............

# a=200
# b=200
# if b>a:
#     print("b is greater than a")
# elif a==b:
#     print("a and b are equal")

# else statement..............

# a=200
# b=33
# if b>a:
#     print("b is greater than a")
# elif a==b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")

# without elif...................

# a=200
# b=20
# if b>a:
#     print("b is greater than a")
# else:
#     print("a is greater than b")

# short hand if...............

# a=200
# b=20
# if a>b: print("a is greater than b")

# short hand if...else......

# a=200
# b=400
# print("a") if a>b else print("b")

# multiple else statement.........

# a=200
# b=200
# print('A') if a>b else print("=") if a==b else print("B")

# And keyword ...........

# a=300
# b=200
# c=400
# if a>b and c>a:
#     print("both condition are true ")


# nested if..............

# x=40
# if x>10:
#     print("above ten,")
#     if x>20:
#         print("and also above 20!")
#     else:
#         print("but not above 20")


############### assingments ####################

'''
# 1.A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.
'''
# salary=int(input("Enter your salary: "))
# years=int(input("Enter your experience: "))
# if years>5:
#     print(f"you got 5% increment on your salary {salary}")
# else:
#     print(" your year of service is low ")

'''
# 2.Take values of length and breadth of a rectangle from user and check if it is square or not.
'''
# length=int(input("Enter the length of the rectangle you have: "))
# breadth=int(input("Enter the breadth of the rectangle you have: "))
# if length == breadth :
#     print("It is a square")
# else:
#     print("It is not a square")

'''
# 3.Take two int values from user and print greatest among them.
'''
# x=int(input("Enter a number: "))
# y=int(input("Enter another number: "))
# if x>y :
#     print("x is greater than y")
# else:
#     print("y is greater x")

'''
4.
A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
# Judge and print total cost for user.
'''

# x=int(input("Enter quantity that you have purchased: "))

# y=x*100

# if y > 1000:
#     z=y/10
#     y-=z
#     print(f"you have to pay{y}")
# else:
#     print("no discount for you ")

'''
5.
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
'''

# subject_x=int(input("Enter your subject mark: "))
# if subject_x>=80:
#     print("grade- 'A'")
# elif subject_x<80 and subject_x>=60:
#     print("grade-'B'")
# elif subject_x<60 and subject_x>=50:
#     print("grade-'C'")
# elif subject_x<50 and subject_x>=40:
#     print("grade - 'D'")
# elif subject_x<40 and subject_x>=30:
#     print("grade - 'E'")
# else:
#     print("grade -'F'")





# a=50
# if a>10:
#     print("above ten")
#     if a>20:
#         print("and also above 20")
#         if a>40:
#             print("and also above 40")
# else:
#     print("but not above 50")
