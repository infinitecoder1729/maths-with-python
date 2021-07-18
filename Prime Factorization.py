#Performs Prime Factorization of a Number
number=int(input("Input the Number which you want to Factorize into Prime Numbers : "))
while number % 2 == 0:
    print (2),
    number = number / 2 
for i in range(3,int(number**(1/2)+1),2):        
    while number % i== 0:
        print (i),
        number = number / i   
if number > 2:
    print (number)


    
