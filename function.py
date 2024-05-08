def sumOfNaturalNum(n):
    if n == 1:
        return 1
    else:
        return n + sumOfNaturalNum(n - 1)

n = int(input('Enter up to how many variables you want to add: '))
result = sumOfNaturalNum(n)
print(f"The sum of natural numbers up to {n} is {result}.")
