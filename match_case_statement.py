x=int(input("Enter a value of x: "))

match x:
    case 0:
        print(x, "x is zero\n")
    case 1:
        print("x is one", x)

    case _ if x!=90:
        print(x, 'x is not 90')
    case _ if x!=80:
        print(x, 'is not 80')
    case _:
        print(x)
    
        