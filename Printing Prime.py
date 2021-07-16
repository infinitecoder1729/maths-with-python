lb = int(input("Enter lower bound: "))  
ub = int(input("Enter upper bound: "))  
for n in range(lb,ub + 1):  
     if n > 1:
          for i in range(2,n):  
               if (n% i) == 0:  
                    break  
          else:  
               print(n)
#Print Prime numbers between two numbers
