#! /usr/bin/python3

from hashlib import md5, sha1, sha224, sha256, sha384, sha512
from sys import argv, exit

hash_types = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]
what_line = 0
found_words = []
thread_list = []
exit_code = False


def l(n, s="-"):
	"""
	prints a line
	:param n: number of chars
	:param s: symbol
	:return: None
	"""
	print(n * s)


def header(msg):
	"""
	prints an header
	:param msg: str
	:return: None
	"""
	l(50)
	print(f"{msg:^50}")
	l(50)


def readStr(msg):
	"""
	handle input exceptions
	:param msg: str
	:return: str
	"""
	while True:
		try:
			n = str(input(msg)).strip()
		except KeyboardInterrupt:
			print("\nType 'exit' to exit the program")
		except:
			print("ERROR")
		else:
			return n
			break


def compareHash(h, word_text):
	"""
	compare the hash with the word
	:param word_bytes: word file content
	:param hash_text: hash file content
	:return: None
	"""
	if type_of_crypto == "md5":
		for word in word_text:
			if md5(word.encode("utf8")).hexdigest() == h:
				print("Found: " + word + " - " + h)
				found_words.append(word)
				break
	elif type_of_crypto == "sha1":
		for word in word_text:
			if sha1(word.encode("utf8")).hexdigest() == h:
				print("Found " + word + " - " + h)
				found_words.append(word)
				break
	elif type_of_crypto == "sha224":
		for word in word_text:
			if sha224(word.encode("utf8")).hexdigest() == h:
				print("Found " + word + " - " + h)
				found_words.append(word)
				break
	elif type_of_crypto == "sha256":
		for word in word_text:
			if sha256(word.encode("utf8")).hexdigest() == h:
				print("Found " + word + " - " + h)
				found_words.append(word)
				break
	elif type_of_crypto == "sha384":
		for word in word_text:
			if sha384(word.encode("utf8")).hexdigest() == h:
				print("Found " + word + " - " + h)
				found_words.append(word)
				break
	elif type_of_crypto == "sha512":
		for word in word_text:
			if sha512(word.encode("utf8")).hexdigest() == h:
				print("Found " + word + " - " + h)
				found_words.append(word)
				break
        

def fileExist(filename):
	"""
	verify if file exist
	:param filename: filename
	:return: bool
	"""
	try:
		a = open(filename, "rt")
	except:
		return False
	else:
		return True


def createFile(filename):
	"""
	creates a file
	:param filename: filename
	:return: None
	"""
	try:
		a = open(filename, "wt+")
	except:
		print("ERROR CREATING THE FILE")
	else:
		print(f"{filename} created!")


def writeFile(filename, word):
	"""
	write in the file
	:param filename: filename
	:param word: str
	:return: None
	"""
	try:
		a = open(filename, "at")
	except:
		print("ERROR OPENING THE FILE")
	else:
		a.write(f"{word}\n")


def readHash():
	"""
	calls compare Hash
	:return: None
	"""
	global what_line
	try:
		compareHash(list_of_hashes[what_line], word_file_text)
		what_line += 1
	except:
		exit_code = True


def readFile(word):
	"""
	read file content
	:param word: filename
	:return: None
	"""
	no_spaces = []
	try:
		a = open(word, "rt").readlines()
	except:
		print("Error opening the file")
	else:
		for line in a:
			no_spaces.append(line.replace("\n", ""))
		return no_spaces


# CHECK IF THE WORDLIST WAS PASSED AND IF IT EXIST

while True:
	try:
		wordlist = argv[1]
		if fileExist(wordlist):
			break
		else:
			raise Exception
	except:
		wordlist = readStr("Wordlist: ")
		if wordlist.lower() == "exit":
			exit()
		if fileExist(wordlist):
			break
		else:
			print("File does not exist!")

# CHECK IF THE HASHLIST WAS PASSED AND IF IT EXIST

while True:
	try:
		hashlist = argv[2]
		if fileExist(hashlist):
			break
		else:
			raise Exception
	except:
		hashlist = readStr("Hashlist: ")
		if hashlist.lower() == "exit":
			exit()
		if fileExist(hashlist):
			break
		else:
			print("File does not exist!")

# CHECK IF TYPE OF CRYPTO WAS PASSED AND IF IT EXIST
while True:
	try:
		type_of_crypto = argv[3]
		if type_of_crypto.strip() in hash_types:
			break
		else:
			raise Exception
	except:
		type_of_crypto = readStr("Encryption type: ")
		if type_of_crypto.lower() == "exit":
			exit()
		if type_of_crypto.strip() in hash_types:
			break
		else:
			print("Invalid type of encryption!")


# CALL'S FUNCTIONS
header("Checking Hashes")

word_file_text = readFile(wordlist)
list_of_hashes = readFile(hashlist)

while True:
	if not exit_code:
		if what_line != len(list_of_hashes):
			readHash()
		else:
			break
	else:
		break

# SAVE THE FOUND THINGS IN A FILE
if len(found_words) != 0:
	l(50)
	if not fileExist("creds.txt"):
		createFile("creds.txt")
		filename = "creds.txt"
	else:
		number = 1
		while fileExist("creds" + f"{number}" + ".txt"):
			number += 1
		createFile("creds" + f"{number}" + ".txt")
		filename = "creds" + f"{number}" + ".txt"

	for words in found_words:
		writeFile(filename, words)
else:
	print("Nothing match")
