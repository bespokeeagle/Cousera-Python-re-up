#Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

k = []
#t = []
userinpt = input ("enter file name: ")
pyhandle = open (userinpt)
for line in pyhandle:
    line = line.strip()
    lines = line.split()
    for l in lines:
        if l not in k:
            k.append(l)
#    print (lines)
#    if lines not in k :
#        k. append (lines)
#print(k)
k.sort()
print (k)
     
