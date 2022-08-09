# Immutability of the string.

# in python the string are immutable i.e we cannot change the value of any specific index number if we have to do any change then we have to reassign the value of that string/variable.

name="01234567"

# name[7]="8" | we cannot change the string like this if we want to so we have to re-assign the value of that string.

name="01234568"

print(name)

# we can also change the string like this 
name="01234567" + "8" # but this will be a new string.

print(name)