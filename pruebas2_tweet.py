

import random

orientations = ['hetero','gay','lesbian','bisexual','asexual']

characters = ['mario','luigi','browser','peach']

N = 1000 # vamos a modelizar 100 respuestas


list_respuestas = []

for j in range(N):
    
    list_respuestas.insert(0,random.choice(orientations) +" " + random.choice(characters) )
    

