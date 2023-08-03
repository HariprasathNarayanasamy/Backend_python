# create a parent class...........


# class person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname

#     def printname(self):
#         print(self.fname, self.lname)
    
# p1=person("hari","prasath")

# p1.printname()


# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname

#     def printname(self):
#         print(self.firstname,self.lastname)
    

# p1=person("hari","prasath")

# p1.printname()


# to create a child class...............

# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname

#     def printname(self):
#         print(self.firstname,self.lastname)

# class student(person):
#     pass

# x=student("you","prasath")

# x.printname()

# Add the __init__() in function...............

# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname

#     def printname(self):
#         print(self.firstname,self.lastname)
    
# class student(person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)

# x=student("H","P")
# x.printname()

# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname

#     def printname(self):
#         print(self.firstname,self.lastname)
    
# class student(person):
#     def __init__(self, fname, lname,year):
#         super().__init__(fname, lname)
#         self.graduationyear=year

# x=student("hari","prasath",2022)
# print(x.graduationyear,x.firstname,x.lastname)

# add method ...................

# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
    
#     def printname(self):
#         print(self.firstname,self.lastname)
    
# class student(person):
#     def __init__(self,fname,lname,year):
#         super().__init__(fname,lname)
#         self.graduation=year

#     def welcome(self):
#         print("welcome ",self.firstname,self.lastname,"to the class of ",self.graduation)

# x=student("hari","prasath",2022)
# x.welcome()


# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
    
#     def printname(self):
#         print(self.firstname,self.lastname)

# class student(person):
#     def __init__(self,fname,lname):
#         person.__init__(self,fname,lname)

# p1=student("hari","prasath")
# p1.printname()

