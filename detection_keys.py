"""
The detection is valid when there are no alphabetic characters at the begining 
 or at the end of the hypothetical detection.
 
SENTENCES THT CAN GET WORNG DATA:
    
'I am not gay but straight'
'Straight and basically anyone in the second to last row'
'i’m bi (but also ????) and i main the pretty princess that wears orange idr her name'
'I'm hetro, and use toad': bad spelling!
'Bisexual and D R Y  B O N E S'
"""

import string

def keyword_detection(sentence,keyword):
    
    sentence = sentence + " " # avoids index out of range
    letters = string.ascii_lowercase # import the alphabet in lowercase    
    n_keyword = len(list(keyword)) # i think its not needed to convert it into a list    
    ind = sentence.find(keyword) # first index of a possible match
    
    if ind == -1:          
        detection = False
    
        
    elif ind == 0:  #possible match at the beggining
        
        if sentence[ind + n_keyword ] in letters: 
            detection = False # avoids false data like 'strightforward'
            
        else:                
            detection = True
            
    else:
    
        if sentence[ind-1] in letters or sentence[ind + n_keyword ] in letters:
            detection =  False # avoids false data like 'strightforward'
            
        else:          
            detection = True
            
    
    return detection    
    
    
    











