# In A String All The Character Will Be At A Different index number
# The Space Will be  consider as a Character only and will be stored in a different index value

str = "Hi Adi"
print(str)

# We can also grab different pieces of string

selfish = "01234567"

# [start:stop:stepover]

print(selfish[0:8:2])

# If in this format [start:stop:stepover] we write only start with collen or end with collen the the default value of other attribute will be the start or the end

print(selfish[1::]) # Here as there is no end point given so the default will be the last index number

print(selfish[:5]) # As It does not have any start pont so the default will be the zeroth Index number



# In Python Negative index means start from the back
print(selfish[-1])

# For getting A Reverse of a string we can get in this way also

print(selfish[::-1])