#Determina a soma de n números introduzidos
contador=0
resposta='S'
soma=0
while resposta=='S':
    numero=int(input('Digite um número '))
    contador+=1
    soma+=numero
    resposta=input(str('Quer continuar [S/N]? ')).upper().strip()[0]

print("Foram digitados ",contador, " números","e a média é ",soma/contador)

