# creating a function................

# def greetings():
#     print("Hello good morning")



# greetings()

# Arguments............

# def my_name(name):
#     print(name+" "+"working in telestratum")

# my_name("hariprasath")
# my_name("hari")


# Number of arguments............

# def user_id(fname,lname):
#     print("Good morning" +" "+ fname +" "+ lname )

# user_id("hari","prasath")


# def add(x,y):
#     c=x+y
#     return c

# values=add(10,90)


# def age(b,c):
#     age=c-b
#     return age

# birth_year=int(input("enter your birth year: "))
# current_year=int(input("enter your current year: "))
# age1=age(birth_year,current_year)
# print(age1)



# Arbitary Arguments.................

# def my_function(*kids):
#     print("The youngest child is " + kids[1])

# my_function("hari","lakshith","ashwin")


# keyword arguments.......

# def youngest_child(child1,child2,child3):
#     print("the youngest child is "+ child3)


# youngest_child("hari","ashwin","lakshith")



# Arbitrary keywords arguments...................

# def childlname(**kids):
#     print("His first name is "+ kids["fname"] +","+"his last name is "+kids["lname"])

# childlname(fname="hari",lname="prasath")




# def myfun(child1,child2,child3):
#     print("the youngest child is " + child2)


# myfun(child1="hari",child2='lakshith',child3="ashwin")


# default parameter................

# def my_function(country="India"):
#     print("I am from " + country)

# my_function()
# my_function("sweden")
# my_function("brazil")


# passing a list as an arguments................

# def myfun(food):
#     for i in food:
#         print(i)
# fruits=["apple","banana","cherry"]
# myfun(fruits)

# Returns values.............

# def my_fun(x):
#     return 5*x

# print(my_fun(3))
# print(my_fun(5))
# print(my_fun(6))

# def my_fun(a,b,):
#     x=a*b
#     return x

# print(my_fun(2,3))


# Recursion.................

# def tri_recursion(k):
#     if(k>0):
#         result=k + tri_recursion(k-1)
#         print(result)
#     else:
#         result=0
#     return result
# print("recursion example result")
# tri_recursion(6)


# def student_mark(a,b,c,d,e):
#     t=a+b+c+d+e
#     return t

# x=int(input("english mark:"))
# y=int(input("maths mark:"))
# z=int(input("tamil mark:"))
# w=int(input("science mark:"))
# f=int(input("social mark:"))


# total_mark=student_mark(x,y,z,w,f)
# print(total_mark)

