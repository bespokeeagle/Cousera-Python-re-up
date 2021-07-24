# Write code using find() and string slicing  to extract the number at the end of the line below.
#  Convert the extracted value to a floating point number and print it out.
 
text = "X-DSPAM-Confidence:    0.8475 "

# code to find the position/index of the semicolon in text and save to colonpos
colonpos  = text.find(":")
# code to slice text starting from the index after the colon
numpos = text[colonpos+1:]

#code to strip the whitespaces the number string to floating point
fnum = float( (numpos.strip()))
print (fnum)



