import random
from lib.types import IStdin, IStdout


def main(stdin: IStdin, stdout: IStdout):

    stdout.write("To get the flag you need to add 100 4x4 round key matrices to the 4x4 state matrix\n")
    stdout.write("Send answers as a 1x16 vectors\n")
    stdout.write("Initial state:\n")

    initial_state = [random.randint(1, 50) for _ in range(16)]
    for i in range(0, 16, 4):
        stdout.write(f"{initial_state[i]} {initial_state[i + 1]} {initial_state[i + 2]} {initial_state[i + 3]}\n")

    for k in range(100):
        stdout.write(f"Round key {k + 1}:\n")
        round_key = [random.randint(51, 99) for _ in range(16)]
        for i in range(0, 16, 4):
            stdout.write(f"{round_key[i]} {round_key[i + 1]} {round_key[i + 2]} {round_key[i + 3]}\n")

        initial_state = [initial_state[i] ^ round_key[i] for i in range(16)]

        try:
            stdout.write("Your array >> ")
            stdout.flush()

            answer = stdin.readline().strip()
            array = [int(i) for i in answer.split(" ")]
            if array == initial_state:
                stdout.write("Right\n")
            else:
                stdout.write("Wrooong. That's another array\n")
                return
        except Exception as exception:
            print(exception)
            stdout.write("Wrooong. That doesn't look like numbers -_-\n")
            return

    stdout.write("Well done! Here's your flag:" + open("src/ctf_tasks/add_round_key/flag.txt", 'r').read())
    stdout.flush()
