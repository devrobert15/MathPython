#Determina a soma dos termos de uma progressão aritmética
termo1=int(input("Introduza o primeiro termo da progressão: "))
razao=float(input("Introduza a razão da progressão: "))
n_termos=int(input("Introduza o número de termos a mostrar: "))
soma=0
for contador in range(1,n_termos+1):
    termo_atual=termo1+(contador-1)*razao
    print(termo_atual, end=',')
    soma+=termo_atual
print("\n\nA soma dos termos é ", soma)


