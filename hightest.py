#the code find the biggest number
biggest = None
print("Before")
for value in [16, 85, 4, 59, 78, 12, 0, 1, 98] :
    if biggest is None :
        biggest = value
    elif value > biggest :
        biggest = value
    print(biggest, value)
print("After", biggest)