def calculo_das_notas():
    notas = []

    for i in range(5):
        nota = float(input("digite a nota dos alunos: "))
        notas.append(nota) 


    media = sum(notas) / len(notas)
    maior = max(notas)
    menor = min(notas)

    aprovados = 0 
    for nota in notas:
        if nota >= 7:
            aprovados += 1 
    print(f"{aprovados } de 5 alunos foram aprovados")

    if media >= 7:
        print("A turma foi aprovada, media da tumra:",media )
    else:    
        print("A turma foi reprovada, media da tumra:",media )

calculo_das_notas()