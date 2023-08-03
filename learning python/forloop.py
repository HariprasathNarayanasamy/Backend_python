# x=["a","b","c","d"]
# for i in x:
#     print(i)

# break statement...............



# x=["apple","banana","cherry"]
# for i in x:
#     print(i)
#     if i=="banana":
#         break

# x=["apple","banana","cherry"]
# for i in x:
#     if i == "banana":
#         break
#     print(i)


# continue statement.................

# for i in range(1,20):
#     if i==10:
#         continue
#     print(i)


# x=["a","b","c"]
# for i in x:
#     if i=="b":
#         continue
#     print(i)

# increment the sequence with 3..................

# for i in range(3,30,3):
#     print(i)

# for i in range(12,121,12):
#     print(i)


# Else in for loop...................

# for i in range(0,6):
#     print(i)
# else:
#     print("finally loop ended")


# Break before else..............

# for i in range(6):
#     if i==3:
#         break
#     print(i)
# else:
#     print("Finally loop ended")



# Nested loop............

# adj=["red","yellow","green"]
# fruits=["cherry","banana","apple"]
# for x in adj:
#     for y in fruits:
#         print(x,y)





################  Assingments ######################

'''
Calculate the sum of all numbers from 1 to a given number

Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
'''

# user=int(input("enter a num: "))
# j=0
# for i in range(1,user):
#     j+=i
# print(j)


'''
 Write a program to print multiplication table of a given number
'''

# user=int(input("enter the number: "))


# for i in range(1,11):
#     s=i*user
#     print(s)


'''
Write a program to display only those numbers from a list that satisfy the following conditions

    The number must be divisible by five
    If the number is greater than 150, then skip it and move to the next number
    If the number is greater than 500, then stop the loop
'''

# list1=[12, 75, 150, 180, 145, 525, 50]

# for i in list1:
#     if i>150:
#         continue
#     elif i>500:
#         break
#     if i%5==0:
#         print(i)


'''
count the total number of digits in a number

Write a program to count the total number of digits in a number using a while loop.
'''

# user=str(input("enter your number to count the digits: "))
# counter=0
# for i in user:
#     counter+=1
# print(counter)


'''
Print the following pattern

Write a program to use for loop to print the following reverse number pattern

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
'''
# n=5
# k=5
# for i in range(0,n+1):
#     for j in range(k-i,0,-1):
#         print(j,end=" ")    
#     print()

'''
1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
'''

# for i in range(1500,2701):
#     if i%7==0 and i%5==0:
#         print(i,end=", ")


'''
2. Write a Python program to convert temperatures to and from celsius, fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius 
'''

