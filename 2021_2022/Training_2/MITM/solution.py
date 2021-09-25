from os import cpu_count
from datetime import datetime
from multiprocessing.pool import Pool
from multiprocessing import Manager
from feistel import GenericFeistel

manager_attributes = Manager()


PROCESSES_COUNT = cpu_count()
KEY_BIT_LENGTH = 24

knownPlaintext = b"See you in the middle"
knownCiphertext = bytes.fromhex("532638c679c5e39d690c66846828934969266683656b440808614ea508264650")
flagCiphertext = bytes.fromhex("6402137175a376e47bb1a2d362a7c550363bc7d53317f4676124a43632e72edf32ec023d379e581c37bd9076061f84f308614ea508264650")

encDict = manager_attributes.dict()


def doEncryption(processNumber):
	r = 2 ** KEY_BIT_LENGTH // PROCESSES_COUNT
	startI = r * processNumber
	endI = r * (processNumber + 1)
	localDict = {}
	for i in range(startI, endI):
		cipher = GenericFeistel(key = i)
		enc = cipher.encrypt(knownPlaintext)
		localDict[enc] = i
	encDict.update(localDict)
	print(f"Process {processNumber} ran from {startI} to {endI - 1}")


def doDecryption(processNumber):
	r = 2 ** KEY_BIT_LENGTH // PROCESSES_COUNT
	startI = r * processNumber
	endI = r * (processNumber + 1)
	for i in range(startI, endI):
		cipher = GenericFeistel(key = i)
		dec = cipher.decrypt(knownCiphertext)
		if dec in encDict:
			key1 = encDict[dec]
			key2 = i
			print(f"Found keys: {key1}, {key2}")
			cipher1 = GenericFeistel(key = key1)
			cipher2 = GenericFeistel(key = key2)
			dec2 = cipher2.decrypt(flagCiphertext)
			dec1 = cipher1.decrypt(dec2)
			print(dec1)
			return

	print(f"Process {processNumber} ran from {startI} to {endI - 1}")	


with Pool(PROCESSES_COUNT) as p:
	print("Running encryption phase...")
	start = datetime.now()
	p.map(doEncryption, range(PROCESSES_COUNT))
	end = datetime.now()
	print(end - start)
	print("Encryption phase finished\n")

	print("Running decryption phase...")
	start = datetime.now()
	p.map(doDecryption, range(PROCESSES_COUNT))
	end = datetime.now()
	print(end - start)
	print("Decryption phase finished\n")
