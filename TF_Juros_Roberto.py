#Programa para determinar o capital acumulado por juro simples e composto
while True:
    try:
        cinicial = float(input("Introduza o capital inicial: "))
        if  cinicial<=0:
            print("O capital inicial tem que ser um número maior do que zero.")
            continue
        break
    except ValueError:
        print("Por favor introduza um número.")
while True:
    try:
        tx=float(input("Introduza a taxa anual (para 1.5%, introduzir 1.5) : "))
        break
    except ValueError:
        print("Por favor introduza um número.")
while True:
    try:
        nper=int(input("Introduza o número de períodos de capitalização por ano: "))
        if  nper<1 or nper>12:
            print("O número de períodos tem que ser um número inteiro entre 1 e 12 inclusivé.")
            continue
        break
    except ValueError:
        print("Por favor introduza um número inteiro.")
while True:
    try:
        ncap=int(input("Introduza o número total de capitalizações: "))
        if  ncap<0:
            print("O número total de capitalizações tem que ser um número inteiro positivo.")
            continue
        break
    except ValueError:
        print("Por favor introduza um número inteiro.")

i=(tx/nper)/100
print("\n              CAPITAL ACUMULADO")
print("Período   juro simples    juro composto")

for n in range(ncap+1):
    capjs=cinicial*(1+i*n)
    capjc=cinicial*(1+i)**n
    print("   {:>3}      {:>10.2f}       {:>10.2f} ".format(n, round(capjs, 2), capjc, 2))
