# Lists Methods

basket = [1,2,3,4,5]

#adding

basket.append(100) # Adds Element At The End Of The List
basket.insert(4,100) # Adds Element At Specific location of the list
basket.extend([20,30,40]) # Adds Multiple Items In the lists At One time.
print(basket)

# Removing

basket.pop() #It Removes The last Item Of the list if the bracket if empty or we can also remove item from a desired index number, It Also returns whatever We will Remove

basket.remove(20) # can directly Removes the data by writng in the bracket

# basket.clear() # Clears The whole list

# print(basket)

# lists more methods https://www.w3schools.com/python/python_ref_list.asp


# keywords for lists
print(1 in basket)
print(basket.count(1)) # How many times it is repeting
