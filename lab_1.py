def main(): 
    x = 1
    print(x)
    x = increment(x)
    print(x)

def increment(n):
    n += 1
    return n   

main()