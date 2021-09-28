def fibonacci_series(a, b, n):
    c = a+b
    print(c, end=" ")
    if c < n:
        fibonacci_series(b, c, n)
    else:
        return None


# fibonacci_series(0, 1, 15)


def fibonacci_series_m2(n):
    if n <= 1:
        return n
    else:
        return fibonacci_series_m2(n-1) + fibonacci_series_m2(n-2)


for k in range(int(input("Enter the number to print fibonacci series\n"))):
    print(fibonacci_series_m2(k), end=" ")

print(fibonacci_series_m2(int(input("\nNth element of fibonacci\n"))-1))
