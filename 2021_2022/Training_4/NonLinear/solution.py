
def generator(seed, mod):
	for i in range(100):
		yield((seed := -~seed) * seed + -~-seed) % mod

mod = 64019
enc = [54084, 27604, 3282, 26722, 61736, 1001, 62309, 37331, 34255, 14307, 62569, 59696, 51933, 33047, 31188, 5703, 6977, 44713, 54910, 9982, 55344, 23729, 13244, 18992, 23519, 43736, 32090, 38916, 22016, 2851, 20090, 28801, 39710, 17447, 59221, 10138, 51530, 63651, 60912, 38358, 42431, 57996]

seed = 35023
gamma = generator(seed, mod)
flag = ""
for i in range(len(enc)):
	flag += chr((enc[i] * pow(next(gamma), -1, mod)) % mod)

print(flag)