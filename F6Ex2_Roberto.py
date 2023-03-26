#Imprime termos de uma progressão geométrica
soma=0
n_termos=5
u1 = int(input('Insira o primeiro termo: '))
razao = float(input('Insira a razão: '))
termo=u1
while n_termos!=0:
    for n in range(n_termos):
        soma += termo
        print(termo, end=' -> ')
        termo = termo * razao
    n_termos=int(input("\nQuantos termos quer mostrar de seguida? "))
print('A soma de todos os termos é ', soma)
