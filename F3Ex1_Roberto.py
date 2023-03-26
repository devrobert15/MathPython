#Exemplifica o uso do if
idade=int(input("Introduza a idade: "))
notaEx=int(input("Introduza a nota do exame de matemática em pontos: "))
terminou=bool(input("Terminou o secundário?(1 para sim, 0 para não): "))
if (idade<25 and notaEx>=140 and terminou):
    print("Candidato aprovado.")
else:
    print("Candidato não aprovado")