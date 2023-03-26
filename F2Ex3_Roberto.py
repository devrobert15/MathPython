#Revebe número e imprime o digito das dezenas
num=int(input("Insira um número inteiro: "))
centenas = num//100
num -= centenas*100
res = num//10
print("O dígito das dezenas é",res)


