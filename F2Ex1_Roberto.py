#Exemplifica a saida formatada
nomeCliente=input("Digite o nome do cliente: ")
diaVencimento=input("Digite o dia do vencimento: ")
mesVencimento=input("Digite o mês do vencimento: ")
valorFatura=input("Digite o valor da fatura: ")
print("Olá,",nomeCliente)
print("A sua factura com vencimento em {} de {} no valor de {} está fechada".format(diaVencimento,mesVencimento,valorFatura))
