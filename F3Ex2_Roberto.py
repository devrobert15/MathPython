#Verifica se o candidato tem condições para obter vaga no emprego
idade=int(input("Introduza a idade:"))
anosExp=int(input("Introduza o número de anos de experiência:"))
if idade<55 or anosExp<5 or (idade>55 and anosExp>=10):
    print("\nCandidato habilitado à vaga.")
else:
    print("\nCandidato não habilitado à vaga")
