#Decimal to Hexadecimal
def DecToHex(num): 
    hexa = ""
    while num > 0:
        hexaval = num % 16
        hexa = hexchar(hexaval) + hexa
        num = num // 16
    return hexa

def hexchar(hexaval): 
    if hexaval < 10:
        return str(hexaval)
    else:
        return chr(hexaval + 55)
    
print(DecToHex(1234))

#Decimal to Binary
import math 
def DecToBin(value):
    value = int(value)
    result = 0
    i = 0
    while value > 0:
        result += (value % 2) * math.pow(10, i)
        value = value // 2
        i += 1
    return int(result)

print(DecToBin(1234))
    