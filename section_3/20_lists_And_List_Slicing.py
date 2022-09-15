# Lists Are one type of data structure
# Lists Are Mutable(Can be changed)

# List slicing
amazon_cart = [
'notebooks',
'sunglasses',
'toys',
'grapes'
]
amazon_cart [0] = ' laptop'
# It will Generate A Copyof amazon cart.
new_cart = amazon_cart[:]
# It says that the new cart and amazon cart will be equal.
# new_cart = amazon_cart
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)