# Add a placeholder for the price variable:

# price = 59
# txt = f"The price is {price} dollars"
# print(txt)

#********************************************************************************************************************************

# A placeholder can also include a modifier to format the value.

# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

# Example
# Display the price with 2 decimals:


# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

#********************************************************************************************************************************

# Display the value 95 with 2 decimals:

# txt = f"The price is {95:.2f} dollars"
# print(txt)

# txt = f"the price is {20*10} dollars"
# print(txt)



# a=5
# b=3
# x=f"price is {a+b}"
# print(x)


# print(" ")




# price =15
# y=f"it is very {'expensive' if price>10 else 'cheap'}"
# print(y)

#********************************************************************************************************************************

# You can execute functions inside the placeholder:

# Example
# Use the string method upper()to convert a value into upper case letters:

# a="hello"
# x=a.upper()
# print(x)


# def converter(x):
#     return x*0.3048

# y=f"plane is flying at {converter(30000)} meters high"
# print(y)


#********************************************************************************************************************************


# String format()
# Before Python 3.6 we used the format() method to format strings.

# The format() method can still be used, but f-strings are faster and the preferred way to format strings.

# The next examples in this page demonstrates how to format strings with the format() method.

# The format() method also uses curly brackets as placeholders {}, but the syntax is slightly different:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

quantity =3
price =48
order ="i want {} rolls for {} rupees"
print(order.format(quantity,price))


age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
