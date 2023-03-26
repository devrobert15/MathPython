#Determina percentagem de dos alunos por sexo
numTotAlunos=int(input("Introduza o total de alunos da escola: "))
numAlunoMasc=int(input("Introduza o total de alunos do sexo masculino: "))
percentAlunosMasc=numAlunoMasc/numTotAlunos*100
percentAlunosFem=(numTotAlunos-numAlunoMasc)/numTotAlunos*100
print("Percentagem de alunos do sexo masculino: {0}\nPercentagem de alunos do sexo feminino: {1}".format(percentAlunosMasc,percentAlunosFem))
