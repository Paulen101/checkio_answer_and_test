vmonth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def number_to_short_month(number): 
    short_months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]
    if 1 <= number <= 12:
        return short_months[number - 1]
    else:
        return "Invalid month number"

def number_to_full_month(number):
    full_months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    if 1 <= number <= 12:
        return full_months[number - 1]
    else:
        return "Invalid month number"

# In case your teacher want it to print out 1 by 1 
print(number_to_short_month(1)) 

# In case your teacher want it to print out all at once
print([number_to_short_month(i) for i in vmonth]) # exercise 1 
print([number_to_full_month(i) for i in vmonth]) # exercise 2

