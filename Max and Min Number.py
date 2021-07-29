'''Finding the Smallest and the Largest Number out of the Numbers given by the user (Doesn't Use inbuilt functions'''
n=int(input("Enter number of Numbers you want to compare : "))
if n > 1 :
    p=eval(input("Enter a Number : "))
    mn,mx=p,p
    for a in range (1,n):
        p=eval(input("Enter a Number : "))
        if p>mx:
            mx=p
        elif p<mn:
            mn=p
        else :
            mn=mn
            mx=mx
    print("Greater Number is : ",mx)
    print("Smallest Number is : ",mn)
else :
    print("Number of terms should be greater than 1 ")
