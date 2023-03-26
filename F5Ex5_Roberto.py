# Escrever números pares entre dois números dados
n_menor=int(input("Introduza o número inicial (menor): "))
n_maior=int(input("Introduza o número final (maior): "))
for contador in range(n_menor,n_maior+1,2):
    print(contador)
