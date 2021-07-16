t=int(input("Enter the Number of Terms : "))
if t>2:
    first=0
    second=1
    print("\nFibonacci Sequence is : ")
    for i in range(2,t):
        ne=first+second
        print (ne , end = " ")
        first=second
        second=ne

else :
    print("Invalid Input")
