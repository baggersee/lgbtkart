from string import ascii_lowercase
alphabet = set(ascii_lowercase)


# function that given any element in the dictionary, returns its key
def finding_keys(item,dictio):
    
    for key_name, items_names in dictio.items():
        
        if item in items_names:
            return key_name
    
    return 0


# function to detect a keyword in an answer
def detection_function(answer, key_words):
    # answer -> string of an answer 
    # key words -> list with all possible names of a category
    
    answer = answer.lower() 
    answer = ' ' + answer + ' '
    extractions = []
    
    for key_word in key_words:
        
        key_word_length = len(key_word)
        finding = answer.find(key_word)
        
        if finding == -1:
            continue # the key word is not in the answer and we go to the next one
        
        else:
            # avoiding a case of self-content words:
            # e.g. : 'i am bilingual' could be counted wrongly as 'bi'
            # a case like: 'stright/Luigi' would be detected correctly
            if answer[finding-1] not in alphabet and answer[finding + key_word_length] not in alphabet:
                extraction = ''
                # we detect the keyword letter by letter
                for j in range(finding,finding + key_word_length):
                    extraction = extraction + answer[j]
                    
            else:
                continue
            
            extractions.append(extraction)
    
    # not counting the answers where more than an option is chosen
    # e.g.: 'straight, dry bones/koopa/ lemmy if i feel gay'
    if len(extractions) != 1:
        extractions = [0]
    return extractions