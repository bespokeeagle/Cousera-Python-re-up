#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#  You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

counts = dict()
b = []
tmp = []
userinp = input ("enter filename: ")
# defaults the userinput to mbox-short.txt if nothing is entered
if len(userinp) < 1 :
    userinp = "mbox-short.txt"

fhand = open(userinp)
#splits line and extracts contents at index 5 and spllts that further and finally extracts contents at index 0 and appends to list b
for line in fhand:
    if line.startswith("From "):
        line = line.split()
        line = line [5]
        line = line.split(':')
        line = line[0]
        b.append(line)
#print(b)
#creates a dictionary of the contents in b and counts the frequency
for l in b:
    counts[l] = counts.get(l,0) + 1

#print (counts)
#
# creates a tuple of the k,v in dictionary counts
for k,v in counts.items():
    newtup = (k,v)
#    print (newtup)
# appends tuple to list tmp
    tmp.append(newtup)
# sorts list tmp
    tmp = sorted(tmp)
print (tmp)





