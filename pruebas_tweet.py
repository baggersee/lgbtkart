"""
SCRIPT PARA TODAS LAS PRUEBAS DEL PROYECTO TWITTER

"""

#%% CREAR UN dictionary DE FORMA ITERATIVA


dictio = {} # inicializamos el diccionario vacio



keys = ['key1','key2','key1','key4']

elements = ['ingles','castellano','aleman','frances']


n = len(keys) # numero de elementos en las listas

for j in range(n):
    

    dictio[keys[j]] = elements[j]
    
    
#%% VER SI UN string TIENE UNA PALABRA CLAVE QUE NOS INTERESA

palabra_clave = 'pene'

frase = 'Hola soy alvaropene'

frase = frase.lower()

if palabra_clave in frase:
    
    deteccion = palabra_clave
    
else:
    
    deteccion = 'no está'
    
print(deteccion)


#%% 

heteros = ['straight','hetero']

gays = ['gay','homo']

lesbians = ['lesbian']

bisexuals = ['bisexual','pansexual']

asexuals = ['asexual']

orientations = [heteros,gays,lesbians,bisexuals,asexuals]

characters = ['mario','luigi','browser','peach']

lista_respuestas = ['hetero mario','straight browser','lesbian luigi','asexual mario','bi peach','bi luigi','gay browser ','homo peach','lesbian browser']
  
respuesta = lista_respuestas[0]


for respuesta in lista_respuestas:


    for lista in orientations:
        
        for item1 in lista:
        
            if item1  in respuesta:
                
                print(f"\nesta {item1} en {respuesta}")
                
    
    for personaje in characters:
        
        for item2 in personaje:
            
            if item2 in respuesta:
                

#%% remove non valid elements

lista_respuestas = ['hetero mario','straight browser','lesbian luigi','asexual mario','bi peach','bi luigi','gay browser ','homo peach','lesbian browser']
        

#%%

dictio = {}

dictio['dato1'] = ['orientacion1']

dictio['dato1'].insert(1,'personaje1')

#%% crear un diccionario de n entradas iguales

n = len(lista_respuestas)

dictio =  {}

for j in range(n):
    
    dictio[f'dato {j}'] = ["",""]
    
print(dictio)



    
    


           
        
            
            

