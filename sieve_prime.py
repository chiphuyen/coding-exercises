'''
Using Sieve of Eratosthenes algorithm to return a generator of
all primes under a threshold.
'''


def _test_div(n):
    '''
    Check if in the input m is divisible by n
    '''
    def _divisible_by_n(m):
        return m % n == 0
    return _divisible_by_n


def prime_under(threshold):
    div_tests = []

    for n in range(2, threshold):
        if not any(map(lambda test: test(n), div_tests)):
            div_tests.append(_test_div(n))
            yield n


primes = prime_under(1000)
for prime in primes:
    print(prime)
