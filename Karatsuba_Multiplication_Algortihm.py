# Karatsuba's algorithm
# Step 1: Divide both the numbers into two halves (String wise) to form A,B,C,D
# Step 2: Compute AxC and BxD (Recursive Multiplication)
# Step 3: Compute (A+B)x(C+D) (Again Recursive Multiplication)
# Step 4: Compute (A+B)x(C+D) - AxC - BxD
# Step 5: The answer to the problem is 10^n(AxC) + 10^(n/2)(AxD+BxC)+BxD {This is a recursive approach}

def KMul(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        nby2 = n // 2
        a = x // 10**nby2
        b = x % 10**nby2
        c = y // 10**nby2
        d = y % 10**nby2
        ac = KMul(a, c)
        bd = KMul(b, d)
        ad_plus_bc = KMul(a + b, c + d) - ac - bd
        prod = ac * 10**(2 * nby2) + (ad_plus_bc * 10**nby2) + bd
        return prod

# Input
x = int(input("Enter Number x: "))
y = int(input("Enter Number y: "))

# Output
result = KMul(x, y)
print("Product:", result)
