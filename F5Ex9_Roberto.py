#Determina a média de 10 números
soma=0
media=0
for contador in range(1,11):
    num=int(input("indique o número "))
    soma+=num
media=soma/contador
print("A média dos números é ",round(media,1))
print("A média dos números inseridos é {}".format(round(media,1)))
# no exemplo a seguir faz a truncatura
print(f"A média dos números é {media:.1f}")

