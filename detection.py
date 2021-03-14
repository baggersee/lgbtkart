def detection(sentence, keyword):
	sentence = " " + sentence + " "
	ind = sentence.find(keyword)

	if ind == -1 or 
	   sentence[ind-1] in string.ascii_lowercase or
	   sentence[ind + len(keyword)] in string.ascii_lowercase:
		return False
	
	return True
