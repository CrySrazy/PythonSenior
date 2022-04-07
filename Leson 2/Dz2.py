a = input("Ведіть перше число")
b = input('Ведіть друге число')
c = input('Ведіть дію')
if c == '+':
    print('a + b =' ,str(int(a) + int(b)))
elif c == '-':
    print('a - b =' ,str(int(a) - int(b)))
elif c == '*':
    print('a * b =' ,str(int(a) * int(b)))
elif c == '/':
    if b == '0':
        print("ERROR")
    else: 
        print('a / b =' ,str(int(a) / int(b)))

    
