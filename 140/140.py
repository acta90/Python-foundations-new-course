import time

# # Write a function which takes any number of parameters and returns their average.


def average(*args):
    return sum(args)/float(len(args))


print(average(1, 10, 4, 5, 8, 9))


# Write a function to calculate Lucas numbers using the naïve recursion.
# Lucas numbers are very similar to Fibonacci numbers and are defined by L(0)=2, L(1)=1 and L(n)=L(n-1)+L(n-2)


# Use a timing decorator to log how long each call.
# How long does it take to calculate L(35)? What about L(100)?


def timer(func):
    def time_decorator(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        endtime = time.perf_counter()
        run_time = endtime - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return time_decorator


def memoize(func):
    memory = {}

    def helper(x):
        if x not in memory:
            memory[x] = func(x)
        return memory[x]
    return helper


@memoize
@timer
def lucas(n: int) -> int:
    # Base cases: L(0)=2, L(1)=1

    if n == 0:
        return 2

    if n == 1:
        return 1

    # recurrence relation
    return lucas(n - 1) + lucas(n - 2)


print(lucas(100))


# # Write a function which does prime factorization of a number, e.g. 20633239 = 11*29*71*911.
# # Calculate the prime factorization of L(60) and L(61).


def prime_factors(n):
    n = lucas(n)
    i = 2
    factors = []

    if n < 0:
        factors.append(-1)
        n *= -1

    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)
    return factors


print(prime_factors(100))



