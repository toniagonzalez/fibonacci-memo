def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print("I'ts fibonacci time!")
print("Give me a number and I'll return the fibonacci sequence number at that spot!")
try:
    number = int(input("Enter a number greater than or equal to 0: "))
    print("The fibonacci number in that spot is " + str(fib(number)) + "!")
except ValueError:
    print("Invalid input. Please try again using a positive integer.")
