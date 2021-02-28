

#%% FASE 1

"""
Asumo que vamos a recibir un archivo .txt con todas las respuestas

Asumo que es posible hacer una lista con todas las respuestas
A esa hipotetica lista la llamo 'lista_respuestas'


Objetivo: buscar las palabras clave (sexualidad y personaje) en cada respuesta
          y meterlas en un diccionario.
          
          filtrar las respuestas no validas.
          una respuesta es no valida si no tiene las dos infos.


"""

# importamos las listas con las palabras clave que vamos a buscar

from keywords import orientations, characters


# ejemplo de posibles respuestas

lista_respuestas = ['i am hetero mario','straight and browser','lesbian i like luigi','asexual or mario','bisexual and peach','bisexual nd luigi','gay browser ','homo peach','browser','mario hetero','hetero luigi','hetero mario','hetero mario fun','hetero peach','hetero browser']



# inicializamos el diccionario

dictio = {} 

# obtenemos cuantas respuestas tenemos:

    
from pruebas2_tweet import list_respuestas

lista_respuestas = list_respuestas

n = len(lista_respuestas)


# vamos bucando en casa respuesta las palabras clave y filtrando las respuesas que 
# no sean validas

# ACHTUNG: esto puede fallar si hay plabras clave autocontenidas. P.ej:
# si una respuesta contiene la palabra 'HETEROgenous' se confundirá con 'hetero'

for j in range(n):
    
    dictio[f'dato {j}'] = ["",""]
    
    for orientacion in orientations:
        
        for palabra in orientacion:
        
            if palabra in lista_respuestas[j]:
                
                 dictio[f'dato {j}'][0] = palabra
             
    
    for palabra in characters:
        
        if palabra in lista_respuestas[j]:
            
            dictio[f'dato {j}'][1] = palabra
            
    
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
        
        
        if dictio[f'dato {j}'][0] in orientations[k]: 
            
            lista_total[k].insert( 0, dictio[f'dato {j}'][1] )
            
            
           
import matplotlib.pyplot as plt



oris = ['heteros','gays','lesbians','bisexuals','asexuals']


for j in range(5):
    

    plt.hist(lista_total[j])
    
    plt.xlabel('Personajes')
    
    plt.ylabel('Frequency')
    
    plt.title(f'HISTOGRAMA {oris[j]}')
    
    plt.show()
    
# igual todos los bucles 'for' se pueden meter juntos



        
        


    
    


    



   



            

            

