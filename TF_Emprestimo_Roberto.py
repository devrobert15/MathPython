#Programa para determinar o plano de pagamentos de um empréstimo à habitação
while True:
    try:
        valor_inicial=float(input("Digite o valor do empréstimo: "))
        if  valor_inicial<=0:
            print("O capital inicial tem que ser um número maior do que zero.")
            continue
        break
    except ValueError:
        print("Por favor introduza um número.")
while True:
    try:
        tx=float(input("Digite o valor da taxa anual(para 1.5%, introduzir 1.5): "))
        if  tx<=0:
            print("A taxa tem que maior do que zero.")
            continue
        break
    except ValueError:
        print("Por favor introduza um número.")

while True:
    try:
        nper=int(input("Digite o número total de meses do empréstimo: "))
        if  nper<=0:
            print("A taxa tem que maior do que zero.")
            continue
        break
    except ValueError:
        print("Por favor introduza um número.")

i=tx/12/100
va=valor_inicial
prestacao=va*(i/(1-(1+i)**(-nper)))
print("\n                       PLANO DE PAGAMENTOS")
print("Prestação  amortização       juros      prestação    capital em dívida")
for n in range(1,nper+1):
    juros=va*i
    amortizacao=prestacao-juros
    va=va-amortizacao
    print("{:>4}        {:>10.2f}  {:>10.2f}     {:>10.2f}       {:>10.2f}".format(n, round(amortizacao,2), round(juros,2), round(prestacao,2), round(va,2)))
    montante_total=n*round(prestacao,2)
print("\nVALOR DO EMPRÉSTIMO: ", round(valor_inicial,2))
print("MONTANTE TOTAL PAGO: ", round(montante_total,2))



