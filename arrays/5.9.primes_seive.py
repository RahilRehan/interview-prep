# time complexity is O(NloglogN), space: O(N)
# t.c => O(n/2 + n/3 + n/5 + n/7 + n/11 ..) => O(NloglogN)
def generate_primes(n: int) -> List[int]:
    isPrimes = [False, False] + [True]*(n-2+1)
    primes = []

    for p in range(2, n+1):
        if isPrimes[p]:
            primes.append(p)
            for i in range(p, n+1, p):
                isPrimes[i] = False
    return primes