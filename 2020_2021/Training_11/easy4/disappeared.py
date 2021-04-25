import random
from lib.types import IStdin, IStdout


def findDisappeared(arr):
	result = []

	for i in range(len(arr)):
		k = abs(arr[i]) - 1
		if (arr[k] > 0): arr[k] = -arr[k]

	for i in range(len(arr)):
		if (arr[i] > 0): result.append(i + 1)

	return result


def main(stdin: IStdin, stdout: IStdout):

	stdout.write("You will be given 1000 arrays of integers. Each array will consist of N numbers from range (1, N). Numbers in array may duplicate.\n")
	stdout.write("Find numbers from range (1, N) that don't appear in the given array. Return result in an ascending order\n")
	stdout.write("Example: for array [4,3,2,7,8,2,3,1] result will be [5, 6].\n")

	for i in range(1000):
		size = random.randint(10000, 20000)
		arr = [random.randint(1, size) for _ in range(size)]

		stdout.write(f"Array {i + 1}: {' '.join(map(str, arr))}\n")
		stdout.write(f"Answer >> ")
		stdout.flush()

		answer = list(map(int, stdin.readline().strip().split()))
		if answer != findDisappeared(arr):
			stdout.write("Wroong.\n")
			return

	stdout.write("Good job! Your flag is: donnuCTF{0182fb6b445cbe9cea0658c48ac8e5d5}\n")