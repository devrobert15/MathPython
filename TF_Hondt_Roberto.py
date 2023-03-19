# programa para aplicar o Método de Hondt até 6 candidatos
quocientes=[]
nvotos={}
candidato=["A", "B", "C", "D", "E", "F"]
mandatos={}

while True:
    try:
        nc=int(input("Digite um número de candidatos menor ou igual a 6: "))
        if  nc<=0 or nc>6:
            print("O número de candidatos tem que estar entre um e seis inclusivé.")
            continue
        break
    except ValueError:
        print("Por favor introduza um número inteiro.")

while True:
    try:
        nm=int(input("Digite o número de mandatos a atribuir: "))
        if  nm<=0:
            print("O número de mandatos tem que ser um número maior do que zero.")
            continue
        break
    except ValueError:
        print("Por favor introduza um número inteiro.")

for i in range(nc):
        nvotos[candidato[i]]=int(input(f"Introduza o número de votos do candidato {candidato[i]}: "))

# mostra o cabeçalho da tabela de quocientes
print("\n               Tabela de quocientes")
# primeira linha da tabela
print("Divisores", end='   ')
for i in range(nc):
    print("   {}".format(candidato[i]),end='       ')
print()

#cria lista de tuplos:(candidato, quociente) e mostra os quocientes
for j in range(1, nm+1):
    print("{:>5}".format(j), end='     ')
    for k in range(nc):
        q=float(nvotos[candidato[k]] / j)
        quocientes.append((candidato[k], round(q, 1)))
        print("{:>9}".format(round(q, 1)), end='  ')
    print()

#ordena por ordem decrescente a lista de tuplos pelo segundo elemento, neste caso, o quociente
quocientes.sort(key=lambda a: a[1], reverse=True)


#Atribuição dos mandatos até ao penúltimo.
for i in range(nm-1):
    if (quocientes[i])[0] in mandatos:
        mandatos[(quocientes[i])[0]] += 1
    else:
        mandatos[(quocientes[i])[0]] = 1

#Atribuição do último mandato para despistar o caso de empate
if (quocientes[nm-1])[1] == (quocientes[nm])[1]:
    if nvotos.get((quocientes[nm-1])[0]) < nvotos.get((quocientes[nm])[0]):
        if (quocientes[nm-1][0]) in mandatos:
            mandatos[(quocientes[nm-1])[0]] = +1
        else:
            mandatos[(quocientes[nm-1])[0]] = 1
    else:
        if (quocientes[nm][0]) in mandatos:
            mandatos[(quocientes[nm])[0]] = +1
        else:
            mandatos[(quocientes[nm])[0]] = 1
else:
    if (quocientes[nm-1])[0] in mandatos:
        mandatos[(quocientes[nm-1])[0]] += 1
    else:
        mandatos[(quocientes[nm-1])[0]] = 1

print("\nNúmero de mandatos: ")
for candidato,mandatos in mandatos.items():
    print("O candidato ",candidato, "obteve ", mandatos, " mandato(s).")
print()



