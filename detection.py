from string import ascii_lowercase as letters

def detection(sentence, keyword):
	sentence = " " + sentence + " "
	ind = sentence.find(keyword)

	if ind == -1 or 
	   sentence[ind-1] in letters or
	   sentence[ind + len(keyword)] in letters:
		return False
	
	return True
