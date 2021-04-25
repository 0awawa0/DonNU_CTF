import random
from lib.types import IStdin, IStdout


def shuffle(array):
	arr = array[:]
	for i in range(len(array) // 2):
		if i % 2:
			arr[i] = array[len(array) // 2 + i]
		else:
			arr[i] = array[i]
	return arr


def main(stdin: IStdin, stdout: IStdout):

	stdout.write("You will be given 100 arrays of integers consisting 2 * n elements in the form [X1, X2, ..., Xn, Y1, Y2, ..., Yn].\n")
	stdout.write("Return the array in the form [X1, Y1, X2, Y2, ..., Xn, Yn]\n")

	for i in range(100):
		l = random.randint(20, 1000)
		if l % 2: l += 1
		arr = [str(random.randint(-1000, 1000)) for _ in range(l)]

		stdout.write(f"Array {i + 1}: {' '.join(arr)}\n")
		stdout.write(f"Answer >> ")
		stdout.flush()

		answer = stdin.readline().strip().split()
		if answer != shuffle(arr):
			stdout.write("Wroong.\n")
			return

	stdout.write("Good job! Your flag is: donnuCTF{c7761b034d20022d7fafb42e14096677}\n")