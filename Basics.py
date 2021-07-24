#using input to collect data
name = input ('what is your name ? ' )
print ("welcome " + name ) 

hours = input ("how many hours do you work:  ")
rate = input ("what do you earn per hour:  ")
pay = float(rate) * float (hours)

print ("your pay is " + str (pay))
