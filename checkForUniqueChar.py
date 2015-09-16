"""This program checks whether all characters in strings are unique """

def checkForUniqueChar(string):
	if len(list(string))==len(set(string)):
		print('All characters in String are unique')
	else:
		print('Characters in String are not unique')

