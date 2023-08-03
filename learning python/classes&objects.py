# create class...........
# class myclass:
#     x=5

# print(myclass)


# create a objects using class........

# class myclass:
#     x=5
# p1=myclass()
# print(p1.x)

# the __init__() function................

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# p1=person("hari",21)

# print(p1.name)
# print(p1.age)

# without the str function...........

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
# p1=person("hari",21)

# print(p1)


# with __str__() function 

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def __str__(self):
#         return f"{self.name}({self.age})"

# p1=person("hari",21)

# print(p1)

# object method in python.......

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def myfun(self):
#         print("hello my name is " + self.name ,self.age)



# p1=person("hari",21)

# p1.myfun()


# the self parameter...........

# class person:
#     def __init__(data,name,age):
#         data.name=name
#         data.age=age
    
#     def myfun(abc):
#         print("hello my name is "+ abc.name)
    
# p1=person("hari",21)
# p1.myfun()