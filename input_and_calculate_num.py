
positive_num = []
negative_num = []   

while True:
    num = eval(input("Enter a number (0: for end of input): "))
    if num == 0: 
        break 
    elif num > 0:
        positive_num.append(num)
    elif num < 0: 
        negative_num.append(num)

print("The number of positive numbers is", len(positive_num))
print("The number of negative numbers is", len(negative_num))

def total_num():
    total = 0
    for i in positive_num:
        total += i
    for i in negative_num:
        total += i
    return total

def average_num():
    average = total_num() / (len(positive_num) + len(negative_num))
    return round(average, 2)

print(total_num())
print(average_num())