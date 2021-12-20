def printdisarium(lower,upper):
     l1=[]    
     def calclength(n):    
          length = 0;    
          while(n != 0):    
               length = length + 1;    
               n = n//10;    
          return length
     def adddigits(num):    
          rem = sum = 0;    
          len = calclength(num);    
        
          while(num > 0):    
               rem = num%10;    
               sum = sum + (rem**len);    
               num = num//10;    
               len = len - 1;    
          return sum;    
     result = 0
     for i in range(lower, upper):    
          result = adddigits(i);    
          if(result == i):    
               l1.append(i)
     return l1
llimit=int(input("Enter the lower limit : "))
ulimit=int(input("Enter the upper limit : "))
print(printdisarium(llimit,ulimit))
