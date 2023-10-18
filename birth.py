import datetime 

birthyear = int(input ("Enter your birth year:"))
age = datetime.datetime.now().year - birthyear
print("Your age is", age, "years old")
