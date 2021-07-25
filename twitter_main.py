import pandas as pd
import matplotlib.pyplot as plt
import json
from twitter_functions import finding_keys, detection_function



# importing the answers from the file with the data
file_answers = open('data.txt','r', encoding="utf8" )
list_answers = [] # initializing the list where all the answers will be imported
N_col = 9527 # total number of replies

for j in range(N_col):
    
    answer = file_answers.readline().lower().strip()
    list_answers.append(answer)
        
file_answers.close()  


# importing the categories (characters and orientations) from JSON files to Python dictionaries
with open('characters.json','r') as file:
    characters_dict = json.load(file)

with open('orientations.json','r') as file:
    orientations_dict = json.load(file)
    

# building a list with all the possible names of all possible characters
characters_set = set()
characters_tuple = tuple(characters_dict.items())

for j in range(len(characters_dict)):
    characters_set.update(set(characters_tuple[j][1]))
    
characters_names_list = list(characters_set) 


# building a list with all the possible names of all possible orientations
orientations_set = set()
orientations_tuple = tuple(orientations_dict.items())

for j in range(len(orientations_dict)):
    orientations_set.update(set(orientations_tuple[j][1]))
    
orientations_names_list = list(orientations_set) 


# analyzing all the answers and finding out the character and orientation
results_orientations = [] # initialiing the list of the results in orientations
for item in list_answers:
    result_orientations = detection_function(item, orientations_names_list)
    final_result_orientations = finding_keys(result_orientations[0],orientations_dict) 
    results_orientations.append(final_result_orientations)
    

results_characters = [] # initialiing the list of the results in characters
for item in list_answers:
    result_characters = detection_function(item, characters_names_list)
    final_result_characters = finding_keys(result_characters[0],characters_dict) 
    results_characters.append(final_result_characters)
   

   
# building a DataFrame with the results
arrays_characters = pd.Series(results_characters)
arrays_orientations = pd.Series(results_orientations)
data_results = pd.DataFrame({'characters':arrays_characters, 'orientations':arrays_orientations})

# keeping the answers with data from both categories
data_results = data_results[data_results.characters!=0]
data_results = data_results[data_results.orientations!=0]



# Statistics
# for every orientations a graph with all the characters chosen is plotted

# contructing lists for the key names of both categories
orientations_keys_list = list(orientations_dict.keys()) # esto se supone que ya existe ¿no?
characters_keys_list = list(characters_dict.keys())

for ori in orientations_keys_list:
    
    # different characters for a fixed orientation
    data = data_results.loc[data_results.orientations == ori, 'characters']
    # computing the percentage of that fixed orientations
    ori_per = round(100*(len(data)/len(data_results)))
    
    frequencies = [ ]
    characters_list = [ ]
    
    for char in characters_keys_list:
        # computing the frequency of every character
        char_freq =  len(data[data==char])
        # computing its percentage
        char_freq_per = 100*(char_freq/len(data))
        
        # for the graph the characters with a percentage smaller than 5% wont be considered
        # considering all the characters gives a graph too chaotic
        if char_freq_per < 5:
            continue
        else:
            # building the lists with every character considered for the graph and its frequency (percentage)
            characters_list.append(char)
            frequencies.append(char_freq_per)
            
    # plotting the final results in a circular graph
    plt.pie(frequencies,labels=characters_list, autopct="%0.1f %%")
    plt.title(ori + ' (' + str(ori_per)+ '%' + ')')
    plt.show()