def checker(a):
    if type(a) != str:
        raise TypeError(f"Sory, i can't work with {type (a)} , i need class str")
    else:
        print("Good")


b = 10
checker(b)
