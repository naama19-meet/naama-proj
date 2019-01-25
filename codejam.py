import python
b=1
d = 0
#generates a list of numbers.
while b<15:
    b=b+1
    x = 0.0
    a = 0
    #generates a list of numbers less than b. 
    while x<b:
        x=x+1
        #this will check for divisors. 
        if (b/x)-int(b/x) == 0.0:
            a=a+1
    if a==2:
        #if it finds a prime it will add it.
        d=d+b
print d 