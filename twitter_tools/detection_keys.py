 
#%%
"""
PROTOCOL 1

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

def keyword_detection(sentence,keyword1,keyword2):

    letters = string.ascii_lowercase
    
    n_keyword1 = len(list(keyword1)) 
    
    ind1 = sentence.find(keyword1)
    
    if ind1 == -1:
        
        detection1 = False
    
        
    elif ind1 == 0:
        
        
        
        if sentence[ind1 + n_keyword1 ] in letters:
            
            detection1 = False
            
                
                
        else:
                
            detection1 = True
            
          
        
    else:
        
        
    
        if sentence[ind1-1] in letters or sentence[ind1 + n_keyword1 ] in letters:
            
            detection1 = False
            
            
            
        else:
            
            detection1 = True
            
            
    
          
            
    n_keyword2 = len(list(keyword2)) 
    
    
    ind2 = sentence.find(keyword2)
    
    if ind2 == -1:
        
        detection2 = False
        
        
        
        
    elif ind2 == 0:
        
        
        
        if sentence[ind2 + n_keyword2 ] in letters:
            
            detection2 = False
            
           
                
                
        else:
                
            detection2 = True
            
            
        
        
    else:
        
        
    
        if sentence[ind2-1] in letters or sentence[ind2 + n_keyword2 ] in letters:
            
            detection2 = False
            
            
            
        else:
            
            detection2 = True
            
           
    
        
    
    
    if detection1 == True and detection2 == True:
        
        detection = True
        
    else:
        
        detection = False
    
    
    return detection
    



 
    
    
    











