import os
import random
from Crypto.Cipher import AES
from lib.types import IStdin, IStdout


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("To get the flag you need to encrypt or decrypt 100 blocks of data with AES using ECB mode\n")
    stdout.write("You will receive 3 lines for each round\n")
    stdout.write("First line will contain operation to perform: 1 - encrypt, 2 - decrypt\n")
    stdout.write("Second line will contain key as a hexadecimal string\n")
    stdout.write("Third line will contain hexadecimal string to perform operation on\n")
    stdout.write("Let's go!\n")

    for k in range(100):
        stdout.write(f"Round {k + 1}:\n")

        operation = random.randint(1, 2)
        stdout.write(f"{operation}\n")

        key = os.urandom(16)
        data = os.urandom(16)

        stdout.write(f"{key.hex()}\n")
        stdout.write(f"{data.hex()}\n")

        required = ""
        if operation == 1:
            required = AES.new(key, AES.MODE_ECB).encrypt(data).hex()
        elif operation == 2:
            required = AES.new(key, AES.MODE_ECB).decrypt(data).hex()

        try:
            stdout.write("Your answer >> ")
            stdout.flush()

            answer = stdin.readline().strip()

            if required == answer:
                stdout.write("Right\n")
            else:
                stdout.write("Wrooong. Your answer is incorrect\n")
                return

        except Exception as exception:
            print(exception)
            stdout.write("Wrooong. Exception occurred processing your answer\n")
            return

    stdout.write("Well done! Here's your flag:" + open("src/ctf_tasks/full_aes/flag.txt").read())
