# balance = 1000 
# while True: 
#     if balance < 9: 
#         break
#     balance = balance -9 

# print("balance is ", balance)

# number = 0
# sum = 0
# for count in range(5):
#      number = eval(input("Enter an integer: "))
#      sum += number
# print("sum is", sum)
# print("count is", count)


def sum(i1, i2):
    result = 0
    for i in range(i1, i2 + 1):
        result += i
    return result

def main():
    print("Sum from 1 to 10 is", sum(1, 10))
    print("Sum from 20 to 37 is", sum(20, 37))
    print("Sum from 35 to 49 is", sum(35, 49))

main() # Call the main function