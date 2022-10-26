"""Calculte Compound Interest Interest"""
def ci(principle, rate, time):
    Amount = principle * (pow((1 + rate / 100), time))
    Amount - principle
    print("Compound Interest is",Amount - principle)
p=float(input("Enter the Principle Amount : "))
r=float(input("Enter the Rate of Interest : "))
t=float(input("Enter the time in years : "))
ci(p,r,t)
