import random
import base64
from lib.types import IStdin, IStdout
from Crypto.Util.number import getPrime


MAX_ENTRIES = 10

users = {}
adminSecret = 0xdeadbeef

users[adminSecret] = [open("src/ctf_tasks/rsa/flag").read().strip()]

e = 0x10001
n = 0x88947242ed41dc41ddbc6402717ab9b6d829d38f026fe5790a65e3300223b9fbeaf9b6a1c3ab0386b2c915cbe2caf3c417bfb0d75737845888e37c2745cb1814bf6e76aadf6a64e98037465f7608f57cd55ca3f355d234bca0ed71d8a37584d65aa99fddba64e38035d78dca83453543a92d1eedc153573bc13245c2601ac1e01ea54cbb1be6259883a77e8b01aea24672356a07b852dafb8a181e612504aa7e8024f005bdb570fd2a8b1026eae9d819cc494643806b7105bac3f69c2a1db7e177540b005f00ecb94aebfdfe0c6a35bba5a250e8843013fca75b4d98fcb947f9b970b505672168a3c5870fa02277bcc1ee023916b3653063cf0efa63c8fe9363
d = int(open("src/ctf_tasks/rsa/secret_exp").read().strip(), 16)

verifyParam = getPrime(56)
invertVerifyParam = pow(verifyParam, -1, n)


def checkToken(token):

    decoded = base64.b64decode(token).decode().split("\n")
    secret = int(decoded[0], 16)

    encryptedVerification = int(decoded[1], 16)
    decryptedVerification = pow(encryptedVerification, d, n)
    verificationValue = (decryptedVerification * invertVerifyParam) % n

    return (secret == verificationValue, secret)


def generateToken():

    secret = getPrime(56)
    while secret in users:
        secret = getPrime(56)

    users[secret] = []
    verificationValue = (secret * verifyParam) % n
    encryptedVerification = pow(verificationValue, e, n)
    tokenVerification = hex(encryptedVerification)[2:]
    token = base64.b64encode((hex(secret)[2:] + "\n" + tokenVerification).encode()).decode()
    return token


def addNote(token, note):

    try:
        check = checkToken(token)
        if not check[0]: return False
        secret = check[1]
        if secret == adminSecret: return False
        if secret not in users: return False
        else:
            if len(users[secret]) >= MAX_ENTRIES: return False
            users[secret].append(note)
            return True
    except Exception as ex:
        print(ex)
        return False


def getNotes(token):

    try:
        check = checkToken(token)
        if not check[0]: return []
        secret = check[1]
        if secret not in users: return []
        else: return users[secret]
    except Exception as ex:
        print(ex)
        return []
 

def main(stdin: IStdin, stdout: IStdout):

    stdout.write("Welcome to note taker. Here you can save and read up to 10 your notes\n\n")

    while True:
        stdout.write("Choose the option to perform:\n")
        stdout.write("\t1. Get new token\n")
        stdout.write("\t2. Add the note\n")
        stdout.write("\t3. Get my notes\n")
        stdout.write("\t4. Exit\n")
        stdout.write(">> ")

        option = stdin.readline().strip()
        if option == '1':
            token = generateToken()
            stdout.write(f"Your token: {token}\n\n")
        if option == '2':
            stdout.write(f"Enter your token >> ")

            try:
                token = stdin.readline().strip()
            except Exception:
                stdout.write("Token has wrong format!\n")
                continue

            stdout.write(f"Enter your note >> ")
            note = stdin.readline().strip()
            if addNote(token, note):
                stdout.write("Your note successfully saved!\n\n")
            else:
                stdout.write("Failed to save your note, token is wrong!\n\n")

        if option == '3':
            stdout.write(f"Enter your token >> ")

            try:
                token = stdin.readline().strip()
            except Exception:
                stdout.write("Token has wrong format!\n")
                continue

            stdout.write("\nNotes for given token: \n")
            for i, note in enumerate(getNotes(token)):
                stdout.write(f"{i}: {note}\n\n")
        if option == '4':
            break
