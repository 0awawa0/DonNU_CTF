from .mathbase import *


class PublicKey:

    @classmethod
    def fromRawParams(cls, e: int, primes: list):
        n = 1

        for p in primes:
            n *= p

        return cls(e, n)

    @classmethod
    def fromPrimesOnly(cls, primes: list):
        n = 1

        for p in primes:
            n *= p

        e = 65537 % (2 ** (n.bit_length() + 1) - 1)
        fn = eulers_totient(n, primes)

        while gcd(e, fn) != 1:
            e = (e + 1) % (2 ** (n.bit_length() + 1) - 1)

        return cls(e, n)

    def __init__(self, e: int, n: int):
        self.e = e
        self.n = n


class PrivateKey:

    @classmethod
    def fromRawParams(cls, e: int, primes: list):

        n = 1
        for p in primes:
            n *= p

        fn = eulers_totient(n, primes)
        d = egcd(e, fn)['a'] % fn

        return cls(d, n)

    @classmethod
    def fromPrimesOnly(cls, primes: list):

        n = 1
        for p in primes:
            n *= p

        e = 65537 % (2 ** (n.bit_length() + 1) - 1)
        fn = eulers_totient(n, primes)

        while gcd(e, fn) != 1:
            e = (e + 1) % (2 ** (n.bit_length() + 1) - 1)
            
        d = egcd(e, fn)['a'] % fn
        return cls(d, n)

    def __init__(self, d: int, n: int):

        self.d = d
        self.n = n


class RSA:

    @classmethod
    def fromBitLength(cls, n: int = 1024):
        p = get_prime(n)
        q = get_prime(n)

        fn = eulers_totient(p * q, [p, q])
        e = 65537 % (2 ** (n + 1) - 1)
        while gcd(e, fn) != 1:
            e = (e + 1) % (2 ** (n + 1) - 1)

        public_key = PublicKey.fromRawParams(e, [p, q])
        private_key = PrivateKey.fromRawParams(e, [p, q])

        return cls(public_key, private_key)

    @classmethod
    def fromRawParams(cls, e: int, primes: list):
        return cls(PublicKey.fromRawParams(e, primes), 
            PrivateKey.fromRawParams(e, primes))

    @classmethod
    def fromPrimesOnly(cls, primes: list):
        return cls(PublicKey.fromPrimesOnly(primes),
         PrivateKey.fromPrimesOnly(primes))

    def __init__(self, public_key: PublicKey, private_key: PrivateKey):

        if public_key.n != private_key.n:
            raise Exception("Given keys are incompatibale. public_key.n != private_key.n")

        self.public_key = public_key
        self.private_key = private_key

    def encrypt(self, n: int):
        if n.bit_length() > self.public_key.n.bit_length():
            raise Exception("Given n is too large to be encrypted with this RSA instance")

        return pow(n, self.public_key.e, self.public_key.n)

    def decrypt(self, n: int):
        return pow(n, self.private_key.d, self.private_key.n)

