#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
#  Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

fname = input ("enter filename: ")
fhand = open (fname)
count = 0
summation = 0

for line in fhand :
    line = line.strip()

    if "X-DSPAM-Confidence:"  in line :
#        print (line)
        count = count + 1
        

        int = line.find(": ")

        intp = line[int+1:]
        print (intp)
        sintp = float(intp.strip())
        summation = sintp + summation

print (summation)
print (count)
avg = summation/count
print (avg)





    

