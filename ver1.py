# Program to check if a string is palindrome or not
import time
import math

s = time.time()

my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

palindrome = True
for i in range(math.floor(len(my_str)/2)):
    if my_str[i]==my_str[-(i+1)]:
        continue
    else:
        palindrome=False
        break

# check if the string is equal to its reverse
if palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

e = time.time()
print("time: %.5f" %(e-s))
    
