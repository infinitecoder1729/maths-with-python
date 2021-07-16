number = int(input("Enter a number: "))  
if number > 1:  
   for count in range(2,number):  
       if (number % count) == 0:  
           print(number,"is not a prime number as",number//count,"*",count,"is",number)  
           break  
   else:  
       print(number,"is a prime number")  
else:  
   print("Invalid Input")
