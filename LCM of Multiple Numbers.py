from math import gcd
n=int(input("Enter the Number of Numbers you want to find the LCM for : "))
numlis=[]
for i in range(n) :
    num=int(input("Enter the Number : "))
    numlis.append(num)
lcm = numlis[0]
for i in numlis[1:]:
  lcm = int(lcm*(i/gcd(lcm, i)))
print("LCM of ",numlis,"is :", lcm)
