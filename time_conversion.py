# convert seconds to hours, minutes, seconds
import time
seconds = int(input("Please enter seconds: "))

hours = seconds // 3600 
minutes = (seconds % 3600) // 60
seconds = (seconds % 3600) % 60

print(f"{hours}h : {minutes}mn : {seconds}s")
