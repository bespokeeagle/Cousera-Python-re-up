#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#  The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#  After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

userinp = input ("enter filename : ")
fhand = open(userinp)
counts = {}
lines = []

for line in fhand:
    if line.startswith("From "):
        line = line.split()
# code to add the second word of each line to the list lines
        lines.append(line[1])

#print (lines)
#code to add each word in lines to the dic as key and update a counter as it's value
for l in lines:
    counts[l] = counts.get(l,0)+1
#print (counts)

words = None
bigcount = None
# code to loop through the keys and values in dic counts and identify the key with the highest count
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        words = word
print (bigcount,words)
