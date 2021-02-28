

import matplotlib.pyplot as plt


#y = [95, 42, 69, 11, 49, 32, 74, 62, 25, 32]

y = ['Tipo 1','Tipo 2','Tipo 3','Tipo 4','Tipo 5','Tipo 1']

# Creating a histogram
plt.hist(y)
plt.xlabel('Bins')
plt.ylabel('Frequency')

plt.title('Histograma')
plt.show()