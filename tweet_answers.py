

#%% FASE 1

"""
We are going to work from a .txt file with all the answers to the tweet.

Aims: 

1) construct a list with all the answers: 'list_answers'

2) search for the key words (sexual orientation and mario kart character)
for each answer.

"""

# import the list with the specified keywords

from keywords import orientations, characters


# example of possible list with the answers
#(later we will have to extract it from a .txt file)

list_answers = ['i am hetero mario','i like potatoes','straight and browser','lesbian i like luigi','asexual or mario','bisexual and peach','bisexual nd luigi','gay browser ','homo peach','browser','mario hetero','hetero luigi','hetero mario','hetero mario fun','hetero peach','hetero browser']



# inicialize the dictionary

dictio_data = {} 

# obtenemos cuantas respuestas tenemos:



n = len(list_answers)


# vamos bucando en casa respuesta las palabras clave y filtrando las respuesas que 
# no sean validas

# ACHTUNG: esto puede fallar si hay plabras clave autocontenidas. P.ej:
# si una respuesta contiene la palabra 'HETEROgenous' se confundirá con 'hetero'

for j in range(n):
    
    dictio_data[f'dato {j}'] = ["",""]
    
    for orientacion in orientations:
        
        for palabra in orientacion:
        
            if palabra in list_answers[j]:
                
                 dictio_data[f'dato {j}'][0] = palabra
             
    
    for palabra in characters:
        
        if palabra in list_answers[j]:
            
            dictio_data[f'dato {j}'][1] = palabra
            
    
    """  
    esto borraría los elementos que solo contienen un tipo de info.
     pero de momento los voy a dejar

      
    if dictio[f'dato {j}'][0] == '' or dictio[f'dato {j}'][1] == '':
        
        del(dictio[f'dato {j}'])   """
        
        
        

#%% FASE 2: HISTOGRAMA DE LOS DATOS

"""
para cada orientacion, estudiamos cómo se distribuyen los personajes

para representarlo con un histograma, necesito transformarlo en una lista y 
 necesitaré filtrar aquellos elementos que solo tengan un tipo de info.

"""

# estamos considerando 5 orientaciones


lista_0  = []  # hetero

lista_1  = []  # homo

lista_2  = []  # lesbian

lista_3  = []  # bisexual

lista_4  = []  # asexual

lista_total = [lista_0, lista_1, lista_2, lista_3, lista_4]

for k in range(5):
    

    for j in range(n):
        
        
        if dictio_data[f'dato {j}'][0] in orientations[k]: 
            
            lista_total[k].insert( 0, dictio_data[f'dato {j}'][1] )
            
            
           
import matplotlib.pyplot as plt



oris = ['heteros','gays','lesbians','bisexuals','asexuals']


for j in range(5):
    

    plt.hist(lista_total[j])
    
    plt.xlabel('Personajes')
    
    plt.ylabel('Frequency')
    
    plt.title(f'HISTOGRAMA {oris[j]}')
    
    plt.show()
    
# igual todos los bucles 'for' se pueden meter juntos



        
        


    
    


    



   



            

            

