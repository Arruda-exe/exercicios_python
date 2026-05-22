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


while True: 
    entrada = str (input("digite seu e-mail de acesso:"))
    senha = int (input("digite sua senha de acesso:"))

    if entrada == "professor@gmail.com" and senha == 1234:
        print("acesso permitido")
        break
    else:
        print("acesso negado")
calculo_das_notas()
