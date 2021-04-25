import random
from lib.types import IStdin, IStdout


def main(stdin: IStdin, stdout: IStdout):

	stdout.write("You will be given 100 integers N. For each N return array containing N unique integers such that they add up to 0.\n")

	for i in range(100):
		l = random.randint(1, 100)

		stdout.write(f"Number {i + 1}: {l}\n")
		stdout.write(f"Answer >> ")
		stdout.flush()

		answer = sum(list(map(int, stdin.readline().strip().split())))
		if answer:
			stdout.write("Wroong.\n")
			return

	stdout.write("Good job! Your flag is: donnuCTF{495818deb0ac365473fd51033e3fa8fb}\n")