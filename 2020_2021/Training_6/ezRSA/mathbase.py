import random


SMALL_PRIMES = [
	2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,
    59,61,67,71,73,79,83,89,97,101,103,107,109,
    113,127,131,137,139,149,151,157,163,167,173,
    179,181,191,193,197,199,211,223,227,229,233,
    239,241,251,257,263,269,271,277,281,283,293,
    307,311,313,317,331,337,347,349,353,359,367,
    373,379,383,389,397,401,409,419,421,431,433,
    439,443,449,457,461,463,467,479,487,491,499,
    503,509,521,523,541,547,557,563,569,571,577,
    587,593,599,601,607,613,617,619,631,641,643,
    647,653,659,661,673,677,683,691,701,709,719,
    727,733,739,743,751,757,761,769,773,787,797,
    809,811,821,823,827,829,839,853,857,859,863,
    877,881,883,887,907,911,919,929,937,941,947,
    953,967,971,977,983,991,997,1009,1013,1019,
    1021,1031,1033,1039,1049,1051,1061,1063,1069,
    1087,1091,1093,1097,1103,1109,1117,1123,1129,
    1151,1153,1163,1171,1181,1187,1193,1201,1213,
    1217,1223,1229,1231,1237,1249,1259,1277,1279,
    1283,1289,1291,1297,1301,1303,1307,1319,1321,
    1327,1361,1367,1373,1381,1399,1409,1423,1427,
    1429,1433,1439,1447,1451,1453,1459,1471,1481,
    1483,1487,1489,1493,1499,1511,1523,1531,1543,
    1549,1553,1559,1567,1571,1579,1583,1597,1601,
    1607,1609,1613,1619,1621,1627,1637,1657,1663,
    1667,1669,1693,1697,1699,1709,1721,1723,1733,
    1741,1747,1753,1759,1777,1783,1787,1789,1801,
    1811,1823,1831,1847,1861,1867,1871,1873,1877,
    1879,1889,1901,1907,1913,1931,1933,1949,1951,
    1973,1979,1987,1993,1997,1999,2003,2011,2017,
    2027,2029,2039,2053,2063,2069,2081,2083,2087,
    2089,2099,2111,2113,2129,2131,2137,2141,2143,
    2153,2161,2179,2203,2207,2213,2221,2237,2239,
    2243,2251,2267,2269,2273,2281,2287,2293,2297,
    2309,2311,2333,2339,2341,2347,2351,2357,2371,
    2377,2381,2383,2389,2393,2399,2411,2417,2423
]


def gcd(n: int, m: int) -> int:
	"""Euklidean algorithm. Finds greatest common divisor of n and m

	Args:
		n -- first number
		m -- second number

	Return: greatest common divisor of n and m.
	"""

	if not n: return m
	if not m: return n

	while n:
		n, m = m % n, n
	return m


def egcd(n: int, m: int) -> dict:
    """Extended Euklidean algorithm. Finds greatest common divisor of n and m

     Args:
         n -- first number
         m -- second number

     Return: dictionary with specified keys:
         reminder -- greatest common divisor
         a, b -- answers to equation an + bm = reminder
     """

    a, a_ = 0, 1
    b, b_ = 1, 0
    
    c, d = n, m
    
    q = c // d
    r = c % d
    while r:
        c, d = d, r
        a_, a = a, a_ - q * a
        b_, b = b, b_ - q * b
        
        q = c // d
        r = c % d
        
    return {"reminder": d, "a": a, "b": b}


def is_prime(p: int, t: int) -> bool:
    """Miller-Rabin primality test. Error probability is (1/4)^t
    More about Miller-Rabin test:
    https://en.wikipedia.org/wiki/Miller–Rabin_primality_test

    Args:
        p -- number to be tested
        t -- count of tests

    Return: True if the number is prime, else - False
    """
    if p <= 0:
        return False

    if p == 2 or p == 1:
        return True

    if p in SMALL_PRIMES:
    	return True

    if True in [p % i == 0 for i in SMALL_PRIMES]:
    	return False

    temp = p - 1
    b = 0

    while temp % 2 == 0:
        temp = temp // 2
        b += 1

    m = (p - 1) // 2 ** b

    for i in range(t):

        a = random.randint(2, p-1)
        z = pow(a, m, p)

        if z == 1 or z == p - 1:
            continue

        for j in range(b - 1):
            z = pow(z, 2, p)

            if z == 1:
                return False

            elif z == p - 1:
                break

        if z == p - 1:
            continue

        else:
            return False

    return True


def get_prime(n: int) -> int:
    """Function generates random prime number with bit length equals n

    Args:
        n -- bit length of generated number

    Return: prime number
    """
    while True:

        # Here I use random.getrandbits to generate n random bits
        # Although higher bits might be 0, so actually this number may have
        # bit length less then n.
        # Moreover, lowest bit might be 0, so this number is not prime
        # To fix this I switch lowest bit to 1, and after that, while
        # the bit length of number less than n I complete it with 1 and 0.
        # For example, n = 4, but generated 0010, so it's 2. And actual bit
        # length is 2 (10). So I do this:
        # 1) Switch lowest bit to 1 and I get number 3 -> 11
        # 2) Complete number to 4 bits, so that highest bit is 1: 11 -> 1011
        if n <= 1:
            return

        num = random.getrandbits(n) | (2 ** (n - 1) + 1)

        # Now I has actual n bits number, but I cant say that it's prime
        # So I check it
        # First, I check if the number is divisible by any of prime numbers
        # from 2 to 200

        def check_small_primes(n):
            for p in SMALL_PRIMES:
                if n % p == 0 and n != p:
                    return False
            return True

        if not check_small_primes(num): continue

        # If it's not, I run Miller-Rabin test 10 times for this number
        # If number passes the test I return it. And it's prime with the
        # probability of 0.9999990463256836
        if is_prime(num, 10):
            return num


def prime_factors(n: int) -> list:
    """Function finds all prime divisors of the given number

    Args:
        n -- number to be factorized

    Return: list of factors
    """
    if is_prime(n, 10):
        return [n]

    import math
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    sq_root = round(math.sqrt(n))
    for i in range(3, sq_root, 2):
        while n % i == 0:
            n = n // i
            factors.append(i)
        if n == 1:
            break
    if n > 1:
        factors.append(n)
    return factors


def eulers_totient(n: int, factors: list = None) -> int:
    """Function counts the positive integers up to a given integer n that are
    relatively prime to n. More about Euler's function:
    https://en.wikipedia.org/wiki/Euler%27s_totient_function

    Args:
        n -- number to be processed

    Return: result of the Euler's function work
    """
    if is_prime(n, 10):
        return n - 1

    if factors:
        mul = 1
        for f in factors:
            mul *= f

        if mul != n: 
            n_factors = set(prime_factors(n))
        else:
            n_factors = set(factors)
    else:
        factors = prime_factors(n)
        n_factors = set(factors)

    count = {}
    for f in n_factors:
    	count[f] = factors.count(f)
    result = 1
    for i in n_factors:
        result *= (i ** (count[i] - 1)) * (i - 1)

    return result


def iroot(a, b):
    """Function to calculate a-th integer root from b. Example: iroot(2, 4) == 2
    """
    if b < 2:
        return b
    a1 = a - 1
    c = 1
    d = (a1 * c + b // (c ** a1)) // a
    e = (a1 * d + b // (d ** a1)) // a
    while c not in (d, e):
        c, d, e = d, e, (a1 * e + b // (e ** a1)) // a
    return min(d, e)


def int_to_bytes(n: int, byteorder: str = "big") -> bytes:
	"""Converts given integer number to bytes object
	"""
	return n.to_bytes((n.bit_length() + 7) // 8, "big")


def bytes_to_int(b: bytes, byteorder: str = "big") -> int:
	"""Converts given bytes object to integer number
	"""
	return int.from_bytes(b, byteorder)


def print_menu():
    print("Available commands:")
    print("1. Euklid algorithm")
    print("2. Extended Euklid algorithm")
    print("3. Primality check")
    print("4. Prime number generation")
    print("5. Integer factorization")
    print("6. Euler's totient")
    print()
    print("0. Exit")


if __name__ == "__main__":

	print("++++++++++Testing mathbase module++++++++++")
	while True:
		print_menu()
		command = int(input("Enter command number >> "))

		if command == 1:
			n, m = map(int, input("Enter two numbers separated by space >> ").split(' '))
			print(f"Result >> {gcd(n, m)}")

		elif command == 2:
			n, m = map(int, input("Enter two numbers separated by space >> ").split(' '))
			print(f"Result >> {egcd(n, m)}")

		elif command == 3:
			n = int(input("Enter the number to check >> "))
			t = int(input("How much tests to perform >> "))
			if is_prime(n, t):
				print(f"Number {n} is prime with probability of {1 - 1 / 4 ** t}")
			else:
				print(f"Number {n} is composite")

		elif command == 4:
			n = int(input("Enter required length >> "))
			print(f"Your number is >> {get_prime(n)}")

		elif command == 5:
			n = int(input("Enter the number to factorize >> "))
			print(f"Factors of {n}: {' '. join(list(map(str, prime_factors(n))))}")

		elif command == 6:
			n = int(input("Enter the number >> "))
			factors = input("Enter list of factors of the number (might be empty) >> ").strip()
			if len(factors) == 0:
				factors = None
			else:
				factors = list(map(int, factors.split(' ')))
				mul = 1
				for f in factors:
					mul *= f
				if mul != n:
					factors = None
					print(f"Multiplication of given factors not equals to {n}. Going to calculate factors by myself, it may take some time.")
			print(f"Euler's totient for {n} is: {eulers_totient(n, factors)}")

		elif command == 0:
			break

		else:
			print("No such command")
		print()



