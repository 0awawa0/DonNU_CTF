from crypto_numbers import gcd


def decrypt(data):
    result = b""
    j = 3
    for i in range(len(data)):
        g = gcd(j, 256)
        while (g["reminder"] != 1):
            j += 1
            g = gcd(j, 256)
        result += bytes([(data[i] * g['a']) % 256])
        j += 1
    return result



if __name__ == "__main__":

    inp = open("output", 'rb').read()
    out = decrypt(inp)
    open("decrypted", 'wb').write(out)
