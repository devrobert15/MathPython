#Calcular descontos
nprod=int(input("Introduza o número de produtos comprados:"))
valorTot=float(input("Indroduza o valor total:"))
desconto=0
if nprod==2:
    desconto=2
elif nprod>2 and nprod<=5:
    desconto=5
elif nprod>5 and nprod<10:
    desconto=10
elif nprod>=10:
    desconto=15

valorDesc=valorTot*desconto/100
valorComDesc=valorTot-valorDesc

print("\nValor total da compra sem desconto: ", valorTot)
print("Valor total da compra com desconto: ", valorComDesc)
print("Valor do desconto obtido: ",valorDesc)
