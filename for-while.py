# example of for cycle than iterates in string
vowels="AEIOU"
for iter in vowels:
    print("char:", iter)

# example of cycle that is using range
# from 10 to -2 with step 1
for it in range(10, -1, -2):
    print(it, end = ", ")

# example of cycle while
count = 0
    while count < 5 :
        num = int(input("Enter number between 0-100?"))
        if (num < 0) or (num > 100):
            print("Aborted while: You've entered an invalid number.")
            break
        count += 1
    else:
        print("While loop ended gracefully.")

