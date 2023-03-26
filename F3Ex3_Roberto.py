#Verifica aprovação na disciplina
nota=int(input("Introduza a nota do aluno:"))
if nota>=10:
    print("\nAprovado.")
elif nota<10:
    notaEx=int(input("Introduza a nota do exame:"))
    if (nota+notaEx)/2<10:
        print("\nReprovado.")
    else:
        print("\nAprovado.")