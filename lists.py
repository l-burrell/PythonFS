
cart = [
    'notebooks', 
    'bags', 
    'pencils', 
    'laptop'
    ]

# print specific index from lists
print(cart[0:3])

# lists are mutable
cart[2] = 'pens'
print(cart)

# create a copy of a list, then modify it
items = cart[:]
items[0] = "binders"
print("items: ",items)

# notice the copy doesn't reference the original
print("cart: ",cart)

# matrix = nested list
matrix = [
    [1,0,1],
    [0,1,0],
    [1,0,1]
]
print(matrix)
