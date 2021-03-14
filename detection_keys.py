 
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

#palabra_clave1 = 'hetero'

#palabra_clave2 = 'browser'

#answer = 'I am hetero and i like browser '

import string

def keyword_detection(sentence,keyword1,keyword2):

    #vaccum = ' '

    letters = string.ascii_lowercase
    
    #palabra_clave = "ola"
    
    n_keyword1 = len(list(keyword1)) 
    
    #frase = "!ola!!!! and i’m bi....." 
    
    ind1 = sentence.find(keyword1)
    
    if ind1 == -1:
        
        detection1 = False
        
        #return vaccum
    
        #print("NOT DETECTED FOR SURE")
        
        
    
    # la palabra clave puede estar al principio
        
    elif ind1 == 0:
        
        
        
        if sentence[ind1 + n_keyword1 ] in letters:
            
            detection1 = False
            
            #return vaccum
                
            #print("not detected")
                
                
        else:
                
            detection1 = True
            
            #return keyword
                
            #print('detected')
        
        
    else:
        
        
    
        if sentence[ind1-1] in letters or sentence[ind1 + n_keyword1 ] in letters:
            
            detection1 = False
            
            #return vaccum
            
            #print("not detected")
            
        else:
            
            detection1 = True
            
            #return keyword
            
            #print("detected")
    
    
    # second category keyword        
            
    n_keyword2 = len(list(keyword2)) 
    
    #frase = "!ola!!!! and i’m bi....." 
    
    ind2 = sentence.find(keyword2)
    
    if ind2 == -1:
        
        detection2 = False
        
        #return vaccum
    
        #print("NOT DETECTED FOR SURE")
        
        
    
    # la palabra clave puede estar al principio
        
    elif ind2 == 0:
        
        
        
        if sentence[ind2 + n_keyword2 ] in letters:
            
            detection2 = False
            
            #return vaccum
                
            #print("not detected")
                
                
        else:
                
            detection2 = True
            
            #return keyword
                
            #print('detected')
        
        
    else:
        
        
    
        if sentence[ind2-1] in letters or sentence[ind2 + n_keyword2 ] in letters:
            
            detection2 = False
            
            #return vaccum
            
            #print("not detected")
            
        else:
            
            detection2 = True
            
            #return keyword
            
            #print("detected")
    
        
    
    
    if detection1 == True and detection2 == True:
        
        detection = True
        
    else:
        
        detection = False
    
    
    return detection
    
#a = keyword_detection(answer,palabra_clave)

#print(a)


#%% PROTOCOL 2 : USING'regular expressions'    
    
    
    











