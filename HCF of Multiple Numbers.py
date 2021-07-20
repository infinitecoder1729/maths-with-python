n=int(input("Enter the Number of Numbers you want to find the HCF for : "))
def hcf(num1,num2):
    if(num1==0):
        return num2
    else:
        return hcf(num2%num1,num1)
if n==2:
    num1=int(input("Enter the Number : "))
    num=int(input("Enter the Number : "))
    hcf_calc=hcf(num,num1)
else:
    num1=int(input("Enter the Number : "))
    num=int(input("Enter the Number : "))
    hcf_calc=hcf(num,num1)
    for i in range(n-2) :
        num=int(input("Enter the Number : "))
        hcf_calc=hcf(num,hcf_calc)
print("HCF of given numbers is:",hcf_calc)
