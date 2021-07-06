try:
    n = int(input("Enter the number of apples harry has: "))
    mn = int(input("Enter the minimum range: "))
    mx = int(input("Enter the maximum range: "))
except ValueError:
    print("Enter integer values only!")
    exit()
for i in range(mn, mx+1):
    res = n / i
    resint = int(res)
    if res == resint:
        print(f"{i} is a divisor of {n}")
    else:
        print(f"{i} is not a divisor of {n}")
