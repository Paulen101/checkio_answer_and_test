n = input("Enter a number: ")
n = int(n)
def multiplication(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)
multiplication(n)