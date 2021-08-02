# recursion
# time c:   O(1)
# space = O(1)
def fact(n):
    if n <= 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)

# brut force
# time c:   O(N)
# space =  O(1)

def factbrut(n):
    fact = 1 
    for i in range(1,n + 1):
        fact = fact * i
    return fact

print(fact(5))
print(factbrut(5))


# 5
# 5*24 = 120
# 4*6 = 24
# 3*2 = 6
# 2*1 = 2
# 1

# print(fact)
