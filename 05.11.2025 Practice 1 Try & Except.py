try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except IndexError:
    print("got an error but we caught it!")

print("continuing our program")
