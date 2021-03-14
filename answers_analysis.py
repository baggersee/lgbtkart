import pandas as pd
import string
from detection_keys import keyword_detection
from keywords import characters,orientations

#%% STEP 1: Importing the answers and storing them in a list

with open('data.txt','r', encoding="utf8" ) as file_answers:
    list_answers = file_answers.read().split("\n")
    
file_answers.close()



#%% STEP 2: Getting the data

# initializing the table with all entries equal to zero
data = pd.DataFrame(0, index=list(characters), columns=list(orientations))

for answer in list_answers:
    
    for ori_key , ori_keyword in orientations.items():
        
        if any(keyword_detection(answer,ori) for ori in ori_keyword):
            ori_detected = ori_key
            
            for char_key , char_keyword in characters.items():
                
                if any(keyword_detection(answer,char) for char in char_keyword):
                    char_detected = char_key
                    data.at[char_detected,ori_detected] = data.at[char_detected,ori_detected] + 1

#%% STEP 3: Histogram


list_0  = []  # hetero

list_1  = []  # homo

list_2  = []  # lesbian

list_3  = []  # bisexual

list_4  = []  # asexual

list_total = [list_0, list_1, list_2, list_3, list_4]

for k in range(5):
    

    for j in range(n):
        
        
        if  list_data[j][0] in orientations_list[k]: 
            
            list_total[k].append( list_data[j][1] )
            
            
           
import matplotlib.pyplot as plt



oris = ['heteros','gays','lesbians','bisexuals','asexuals']


for j in range(5):
    

    plt.hist(list_total[j])
    
    plt.xlabel('Personajes')
    
    plt.ylabel('Frequency')
    
    plt.title(f'HISTOGRAMA {oris[j]}')
    
    plt.show()
    
# igual todos los bucles 'for' se pueden meter juntos













