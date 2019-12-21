def math(log):

    if log == "add":
        def inner_func(n1,n2):
            res = n1 + n2
            return res
    elif log == "sub" :
        def inner_func(n1,n2):
            res = n1 - n2
            return res
    elif log == "mul" :
        def inner_func(n1,n2):
            res = n1 * n2
            return res
    elif log == "div" :
        def inner_func(n1,n2):
            res = n1 // n2
            return res

    return inner_func

def main():
    add = math("add")
    sub = math("sub")
    mul = math("mul")
    div = math("div")

    n1 = int(input("Enter 1. number : "))
    n2 = int(input("Enter 2. number : "))
        
    print (add(n1,n2))
    print (mul(n1,n2))

if __name__ == "__main__" :
    main()
