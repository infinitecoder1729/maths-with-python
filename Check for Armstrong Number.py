num = int(input("Enter a number: "))
length = len(str(num))
t = num
summation = 0
while t > 0:
   digit = t % 10
   summation += digit ** length
   t //= 10
if num != summation:
   print(num,"is not an Armstrong number")
else:
   print(num,"is an Armstrong number")
