fact = lambda n: 1 if n == 0 else n * fact(n - 1)

# Test case
number = 7
result = fact(number)
print(result)
