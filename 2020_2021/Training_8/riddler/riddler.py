from lib.types import IStdin, IStdout


questions = [
    "All right. Let's start with a simple one. What is an alternative name for AES cipher?",
    "A bit of a history. When did the first specification of AES was published? (Date format: dd.MM.YYYY)",
    "What is a name of an AES predecessor?",
    "There is a key-recovery attack that requires less operations to recover the key published by Andrey Bogdanov, Dmitry Khovarovich and Christian Rechberger in 2011. How much operations does it require? (Answer format 2^ddd.d)",
    "And how much terabytes of data do you need?"
]
answers = [
    "Rijndael",
    "26.10.2001",
    "DES",
    '2^126.2',
    '9002',
]


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("Hi! I am The Riddler! I have a flag for you, but you have to answer a few questions about AES to get it. So, should we start?\n")

    for i in range(5):
        stdout.write(questions[i] + "\n")
        stdout.write("Answer >> ")
        stdout.flush()
        answer = stdin.readline().strip()
        if answer != answers[i]:
            stdout.write("No it's not. See ya.\n")
            return

    stdout.write(f"Good job. Here's your flag: {open('./src/ctf_tasks/riddler/flag.txt', 'r').read().strip()}\n")
