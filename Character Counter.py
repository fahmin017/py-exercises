
# 10. Character Counter
# Count uppercase, lowercase, digits and special characters.

a=input("enter the character : ")
upper_c =0
lower_c =0
digits_c =0
special_c =0

for i in a:
    if i.isupper():
        upper_c=upper_c+1

    elif i.islower():
        lower_c=lower_c+1

    elif i.isdigit():
        digits_c=digits_c+1

    else:
        special_c=special_c+1

print(f"upper case : {upper_c}\nlowercse : {lower_c}\ndigits : {digits_c}\nspecial : {special_c}")
