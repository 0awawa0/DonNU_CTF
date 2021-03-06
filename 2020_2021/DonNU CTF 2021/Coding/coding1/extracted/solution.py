import os
import random
import pyminizip
from parse_pwd import parsePwd



for i in range(100	, 0, -1):
	password = parsePwd(f"pwd{i}.png")
	nextZip = f"{i}.zip"

	print(password)

	pyminizip.uncompress(nextZip, password, ".", True)
	os.remove(nextZip)
	os.remove(f"pwd{i}.png")

flagZip = "flag.zip"
flagPwd = f"pwd{0}.png"

password = parsePwd(flagPwd)
pyminizip.uncompress(flagZip, password, ".", True)

os.remove(flagZip)
os.remove(flagPwd)