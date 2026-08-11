# Create a Class
# To create a class, use the keyword class:

# class my_class:
#     x=5

# y=my_class()
# print(y.x)

#*******************************************************************************************************************************

# Delete Objects
# You can delete objects by using the del keyword:

# Delete the p1 object:

# del p1

#*******************************************************************************************************************************

# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content,
#  put in the pass statement to avoid getting an error.

# Example
# class Person:
#   pass

#*******************************************************************************************************************************

# The __init__() Method
# All classes have a built-in method called __init__(), which is always executed when the class is being initiated.

# The __init__() method is used to assign values to object properties, 
# or to perform operations that are necessary when the object is being created

# class student():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# x=student("jack",22)
# print(x.name)
# print(x.age)


# class dog:
#     def __init__(self,name,breed):
#         self.name=name
#         self.breed=breed

# d=dog("jacky","shepard")
# print("name is : ",d.name)
# print("breed is : ",d.breed)


#*******************************************************************************************************************************


# Default Values in __init__()
# You can also set default values for parameters in the __init__() method:

# class student:
#     def __init__(self,name,age=18):
#         self.name=name
#         self.age=age

# s1=student("fahmin",22)
# s2=student("finu")

# print(s1.name,s1.age)
# print(s2.name,s2.age)



# Multiple Parameters
# The __init__() method can have as many parameters as you need:

# class details:
#     def __init__(self,name,age,city,district):
#         self.name=name
#         self.age=age
#         self.city=city
#         self.district=district

# d1=details("finu",21,"balussery","calicut")
# d2=details("sanu",19,"thamarassery","calicut")

# print(d1.name,d1.age,d1.city,d1.district)
# print(d2.name,d2.age,d2.city,d2.district)


#*******************************************************************************************************************************

# The self Parameter
# The self parameter is a reference to the current instance of the class.

# It is used to access properties and methods that belong to the class.

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def greet(self):
#         print("hello",self.name)

# s1=student("fahmin",22)
# s1.greet()





# Without self, Python would not know which object's properties you want to access:

# The self parameter links the method to the specific object:

# class person:
#     def __init__(self,name):
#         self.name=name

#     def print_name(self):
#         print(self.name)

# p1=person("messi")
# p2=person("ronaldo")

# p1.print_name()
# p2.print_name()






# self Does Not Have to Be Named "self"
# It does not have to be named self, you can call it whatever you like, 
# but it has to be the first parameter of any method in the class:


# class students():
#     def __init__(obj,name,age):
#         obj.name=name
#         obj.age=age

#     def greet(obj):
#         print(obj.name,"'s age is",obj.age)

# s1=students("fahmin",22)
# s1.greet()





# Accessing Properties with self
# You can access any property of the class using self:

# Access multiple properties using self:

# class cars():
#     def __init__(self,brand,model,colour):
#         self.brand=brand
#         self.model=model
#         self.colour=colour

#     def details(self):
#         print(f"{self.colour} {self.brand} {self.model}")

# c1=cars("Nissan","GT","Green")
# c1.details()







# Calling Methods with self
# You can also call other methods within the class using self:

# Call one method from another method using self:

# class student:
#     def __init__(self,name):
#         self.name=name

#     def greet(self):
#         return "hello " + self.name

#     def welcome(self):
#         wel=self.greet()
#         print(wel , "welcome to our class")

# s1=student("fahmin")
# s1.welcome()




# Modify Properties
# You can modify the value of properties on objects:

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# s1=student("fahmin",22)
# print(s1.age)

# s1.age=23
# print(s1.age)




# Delete Properties
# You can delete properties from objects using the del keyword:

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# s1=student("fahmin",22)

# del s1.age

# print(s1.name)
# print(s1.age)           # CAUSE ERROR




# Class Properties vs Object Properties
# Properties defined inside __init__() belong to each object (instance properties).

# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:

# class student:
#     topper = "aaro"     #CLASS PROPERTY

#     def __init__(self,name,age):        # INSTANCE PROPERTY
#         self.name=name
#         self.age=age

# s1=student("finu",22)
# s2=student("sanu",19)

# print(s1.name)
# print(s1.topper)
        



# Modifying Class Properties
# When you modify a class property, it affects all objects:

# class student:
#     topper = "aaro"

#     def __init__(self,name):
#         self.name=name

# s1=student("fahmin")
# s2=student("sanu")

# student.topper = "topper njn thanne"

# print(s1.topper)
# print(s2.topper)
# print(s1.name)




# Add New Properties
# You can add new properties to existing objects:

# class student:
#     def __init__(self,name):
#         self.name=name

# s1=student("fahmin")

# s1.age=18
# s1.city="calicut"

# print(s1.name)
# print(s1.age)
# print(s1.city)


#*****************************************************************************************************************************


# Class Methods
# Methods are functions that belong to a class. They define the behavior of objects created from the class.

# class Person:
#   def __init__(self, name):
#     self.name = name

#   def greet(self):
#     print("Hello, my name is " + self.name)

# p1 = Person("Emil")
# p1.greet()




# Methods with Parameters
# Methods can accept parameters just like regular functions:

# class calculator:
#     def add(self,a,b):
#         return a+b

#     def multi(self,x,y):
#         return x*y

# cal=calculator()

# print(cal.add(5,3))
# print(cal.multi(5,3))



# Methods Accessing Properties
# Methods can access and modify object properties using self:

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def details(self):
#         return f"{self.name} is {self.age} years old"

# s1=student("fahmin",22)
# print(s1.details())




# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def birthday(self):
#         self.age=self.age+1
#         print(f"hpy bday ur age is {self.age}")

# s1=student("fahmin",22)

# print(s1.birthday())
# print(s1.birthday())




# Multiple Methods
# A class can have multiple methods that work together:

# class playlist:
#     def __init__(self,name):
#         self.name=name
#         self.songs = []

#     def add_song(self,song):
#         self.songs.append(song)
#         print(f"added : {song}")

#     def remove(self,song):
#         if song in self.songs:
#             self.songs.remove(song)
#         print(f"removed : {song}")

#     def show_song(self):
#         print(f"playlist : {self.name}")
#         for song in self.songs:
#             print(f"{self.songs}")

# my_playlist = playlist("fav")
# my_playlist.add_song("theerame")
# my_playlist.add_song("ilakozhiye")
# my_playlist.show_song()


#*****************************************************************************************************************************

                                                # Python Inheritance
                                        #____________________________________#

# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Create a Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class:

# class person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname

#     def print_name(self):
#         print(self.fname,self.lname)

# p1=person("muhammed","fahmin")

# p1.print_name()



# Create a Child Class
# To create a class that inherits the functionality from another class, 
# send the parent class as a parameter when creating the child class:


# class person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname

#     def print_name(self):
#         print(self.fname,self.lname)


# class student(person):
#     pass

# s1=student("muhammed","fahmin")

# s1.print_name()


# Add the __init__() Function
# So far we have created a child class that inherits the properties and methods from its parent.

# We want to add the __init__() function to the child class (instead of the pass keyword).


class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def print_name(self):
        print(self.fname,self.lname)


class student(person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.graduation_year =year

s1=student("muhammed","fahmin",2022)

print(s1.graduation_year)

