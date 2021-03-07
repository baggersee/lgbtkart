

#%% STEP 1: Importing the answers and storing them in a list

file_answers = open('data.txt','r', encoding="utf8" )

list_answers = []

N_col = 944

for j in range(N_col):
    
    answer = file_answers.readline().lower()
    
    list_answers.append(answer)
        
print(list_answers)

file_answers.close()        


#%% STEP 2: Getting the data

from keywords import orientations_list, characters_list

from detection_keys import keyword_detection

n = len(list_answers)

list_data = []

for j in range(n):
    
    for orientation in orientations_list:
        
        for orientation_word in orientation:
            
            for character in characters_list:
                
                for character_word in character:
                
                    if keyword_detection(list_answers[j],orientation_word,character_word) == True:
                        
                        list_data.append([orientation_word,character_word])


n = len(list_data)

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













