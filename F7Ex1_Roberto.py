#Construção de gráficos
import matplotlib.pyplot as plt
import numpy as np
lista=np.empty(8,dtype=int)
nota_maior=0
indice=0
for i in range(8):
    print("Introduza a nota ",i+1, " ",end="")
    lista[i]=int(input())
    if nota_maior<lista[i]:
        nota_maior=lista[i]
        indice=i
print ("O maior elemento da lista é ", nota_maior)
print ("O indíce do maior valor é ", indice)

plt.plot(lista, linestyle='-', marker='s')
plt.axis([0, 8, 0, 20])
plt.title("Notas a matemática")
plt.xlabel("Alunos")
plt.ylabel("Notas")
plt.show()