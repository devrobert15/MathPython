#Ordenar lista
resposta='S'
lista=[]
while resposta=='S':
    numero=int(input('Digite um número '))
    lista.append(numero)
    resposta=input(str('Quer continuar [S/N]? ')).upper().strip()[0]

print("Inseriu ",len(lista)," números")
lista.sort()
print("Os números inseridos por ordem crescente são ",lista)
lista.sort(reverse=True)
print("Os números insridos por  ordem descrescente são ",lista)

