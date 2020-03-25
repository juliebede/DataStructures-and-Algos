def factorial(n):
  ## Input a number and calculate the factorial
  if (n <= 1):
    return 1
  else:
    return n * factorial(n - 1)


def fib_helper(n, current, next):
  if (n == 1):
    return next
  else:
    new_sum = current + next
    return fib_helper(n - 1, next, new_sum)


def fibonacci(n):
  return fib_helper(n, 0, 1)

print(factorial(4)) #should equal 24
print(fibonacci(10)) #should equal 55