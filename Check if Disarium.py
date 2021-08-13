def disarium(number):
     rem = sum = 0   
     length = len(str(number))        
     n = number    
     while(number > 0):    
         remainder = number%10  
         sum = sum + int(remainder**length)    
         number = number//10  
         length = length - 1       
     if(sum == n):    
         return True    
     else:    
         return False    
num=int(input("Enter a Number : "))
print(disarium(num))