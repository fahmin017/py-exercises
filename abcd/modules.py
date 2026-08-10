# Create a Module
# To create a module just save the code you want in a file with the file extension .py:


# import my_module

# a=my_module.employees["name"]
# print(a)

#******************************************************************************************************************************

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:

# Example
# Create an alias for mymodule called mx:


# import my_module as mx

# a=mx.employees["name"]
# print(a)

#******************************************************************************************************************************

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.

# import platform

# x=platform.system()
# print(x)

#******************************************************************************************************************************

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

# import platform

# x=dir(platform)
# print(x)

# import my_module

# x=dir(my_module)
# print(x)


#******************************************************************************************************************************

# from my_module import employees

# x=employees["age"]
# print(x)

#******************************************************************************************************************************

# import tuples

# a=tuples.tup1[1]
# print(a)

#******************************************************************************************************************************


# Python Dates
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

                                # ***********************************************

# import datetime
# x=datetime.datetime.now()
# print(x)

# print(x.year)
# print(x.strftime("%A"))


# Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime module.

# The datetime() class requires three parameters to create a date: year, month, day.


# import datetime

# x=datetime.datetime(2020,12,21,12)
# print(x)

#******************************************************************************************************************************

                                                    # Python Math

                                                # ********************

# Python has a set of built-in math functions, including an extensive math module, 
# that allows you to perform mathematical tasks on numbers.

# The min() and max() functions can be used to find the lowest or highest value in an iterable:


# x=min(5,8,4,9,7,2,5)
# y=max(5,8,4,9,7,2,5)

# print("min number : ",x)
# print("max number : ",y)

#******************************************************************************************************************************

# # The abs() function returns the absolute (positive) value of the specified number:

# x=abs(-89.34)
# print(x)

# print(" ")

# # The pow(x, y) function returns the value of x to the power of y (xy

# y=pow(5,2)
# print(y)

#******************************************************************************************************************************

# The Math Module
# Python has also a built-in module called math, which extends the list of mathematical functions.

# To use it, you must import the math module:

# The math.sqrt() method for example, returns the square root of a number

# import math

# x=math.sqrt(49)
# print(x)

# # The math.ceil() method rounds a number upwards to its nearest integer, 
# #  the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

# y=math.ceil(1.5)
# z=math.floor(1.5)
# print(y)
# print(z)

# # The math.pi constant, returns the value of PI (3.14...):

# a=math.pi
# print(a)

#******************************************************************************************************************************
#******************************************************************************************************************************

# Python JSON
# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.

# JSON in Python
# Python has a built-in package called json, which can be used to work with JSON data.

# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.

# import json

# x='{"name":"fahmin","age":22,"city":"calicut"}'

# y=json.loads(x)

# print(y["age"])


# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# a={
#     "name":"finu",
#     "age":21,
#     "city":"balussery"
# }

# b=json.dumps(a)
# print(b)

#******************************************************************************************************************************

# Convert Python objects into JSON strings, and print the values:

# import json

# print(json.dumps({"name":"sanu","age":19}))
# print(json.dumps(["apple","grapes","mango"]))
# print(json.dumps(("messi","rono")))

# Convert a Python object containing all the legal data types:

# import json
# x = {
#   "name": "messi",
#   "age": 39,
#   "married": True,
#   "divorced": False,
#   "children": ("mateo","diego"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "colour": "white"},
#     {"model": "Ferrari classic", "colour": "black"}
#   ]
# }
# print(json.dumps(x,indent=5))   #Use the indent parameter to define the numbers of indents:


#******************************************************************************************************************************


# Order the Result
# The json.dumps() method has parameters to order the keys in the result:


# import json
# x = {
#   "name": "messi",
#   "age": 39,
#   "married": True,
#   "divorced": False,
#   "children": ("mateo","diego"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "colour": "white"},
#     {"model": "Ferrari classic", "colour": "black"}
#   ]
# }
# print(json.dumps(x,sort_keys=True,indent=4,separators=".""="))

# You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, 
# and a colon and a space to separate keys from values:

# Use the separators parameter to change the default separator:


#******************************************************************************************************************************
#******************************************************************************************************************************


                                                # Python RegEx
                                        #*******************************#

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

# RegEx can be used to check if a string contains the specified search pattern.

# Python has a built-in package called re, which can be used to work with Regular Expressions.

# Import the re module:

# Search the string to see if it starts with "The" and ends with "Spain":

# import re
# x="the la liga is played in spain"
# y=re.search("^the.*$spain",x)

# if x:
#     print("yes")
# else:
#     print("no")


# RegEx Functions


# findall	    Returns a list containing all matches
# search	    Returns a Match object if there is a match anywhere in the string
# split	        Returns a list where the string has been split at each match
# sub	        Replaces one or many matches with a string



# []	A set of characters	"[a-m]"	
# \	    Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	    Any character (except newline character)	"he..o"	
# ^	    Starts with	"^hello"	
# $	    Ends with	"planet$"	
# *	    Zero or more occurrences	"he.*o"	
# +	    One or more occurrences	"he.+o"	
# ?	    Zero or one occurrences	"he.?o"	
# {}	Exactly the specified number of occurrences	"he.{2}o"	
# |	    Either or	"falls|stays"	
# ()	Capture and group



# Flags
# You can add flags to the pattern when using regular expressions.

# re.ASCII	re.A	            Returns only ASCII matches	
# re.DEBUG		                Returns debug information	
# re.DOTALL	re.S	            Makes the . character match all characters (including newline character)	
# re.IGNORECASE	re.I	        Case-insensitive matching	
# re.MULTILINE	re.M	        Returns matches at the start/end of each line	
# re.NOFLAG		                Specifies that no flag is set for this pattern	
# re.UNICODE	re.U	        Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches	
# re.VERBOSE	re.X	        Allows whitespaces and comments inside patterns. Makes the pattern more readable







# The findall() Function
# The findall() function returns a list containing all matches.

# import re
# x="my name is muhammed fahmin"

# y=re.findall("me",x)
# print(y)

#******************************************************************************************************************************

# import re

# txt = "The rain in Spain"
# x = re.search("\s", txt)

# print("The first white-space character is located in position:",x.start())

#******************************************************************************************************************************

# The split() Function
# The split() function returns a list where the string has been split at each match:

# plit at each white-space character:

# import re

# x= "my name is muhammed fahmin"

# y=re.split("\s",x)

# print("splitted string is : ",y)

# print(" ")


# # Split the string only at the first occurrence:

# z=re.split("\s",x,1)

# print("splitted string is : ",z)

#******************************************************************************************************************************

# The sub() Function
# The sub() function replaces the matches with the text of your choice:

# Example
# Replace every white-space character with the number 9:



# import re
# x="my name is muhammed fahmin"

# y=re.sub("fahmin","finu",x)
# print(y)


#******************************************************************************************************************************


# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

# Example
# Print the position (start- and end-position) of the first match occurrence.

# The regular expression looks for any words that starts with an upper case "S":

# import re
# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.span())


# import re
# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.string)


import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
