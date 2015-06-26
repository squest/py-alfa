import time

__author__ = 'questmac'


def is_prime(n):
    i = 3
    llim = n ** 1 / 2
    while i <= llim:
        if 0 == n % i:
            return False
        else:
            i += 2
    return True


def sum_sieve(lim):
    llim = lim**1/2
    prime = [True] * (lim+1)
    res = 2
    for i in range(3, lim, 2):
        if prime[i]:
            if i <= llim:
                for j in range(i*i, lim, 2*i):
                    prime[j] = False
            res += i
    return res


def timex(f, x):
    start_time = time.time()
    tmp = f(x)
    print("--- %s seconds ---" % (time.time() - start_time))
    return tmp

