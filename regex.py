# In this assignment you will read through and parse a file with text and numbers.
#  You will extract all the numbers in the file and compute the sum of the numbers

import re
nums = []


userinp = input ("enter file name: ")
hand = open(userinp)

for line in hand :
    line = line.strip()
# regex to find and extract all numbers 
    num = re.findall("[0-9]+",line)
#    print (num)
    for item in num :
        if len(item) >=1 :
#            print (item)
            nums.append(float(item))

print (sum(nums))
