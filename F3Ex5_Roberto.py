#Exemplifica o uso de módulos para determinar a idade
from datetime import date

anoNasc=int(input("Introduza o ano de nascimento: "))
anoatual=float(date.today().year)
idade=anoatual-anoNasc
if idade<18:
    print("\nA pessoa é menor idade.")
else:
    print("\nA pessoa é maior de idade.")