import os 
os.system("cls")

codigos = [1, 2, 3, 4, 5, 6, 7]
nomes = ["Hemograma Completo", "Raio-X", "Ultrassonografia", "Eletrocardiograma", "Tomografia", "Ressonancia Magnetica", "Exame de Glicose"]
precos = [150.0, 80.0, 110.0, 230.0, 250.0, 500.0, 15.0]

exames_escolhidos = []
nomes_escolhidos = []
subtotal = 0.0

while True:
    print("\n--- Exames ---")
    for i in range(7):
        print(codigos[i], "-", nomes[i], "- R$", precos[i])
    print("0 - Sair")

    escolha = int(input("\nDigite o codigo do exame: "))

    if escolha == 0:
        break
    elif escolha in codigos:
        indice = escolha - 1
        
        exames_escolhidos.append(codigos[indice])
        nomes_escolhidos.append(nomes[indice])
        subtotal = subtotal + precos[indice]
        
        print("Exame adicionado!")
        
        continuar = int(input("Quer adicionar outro? 1 pra Sim, 2 pra Nao: "))
        if continuar == 2:
            break
    else:
        print("Codigo invalido, tente de novo.")

if subtotal > 0:
    print("\n--- Pagamento ---")
    print("1 - Convenio (15% desconto)")
    print("2 - Particular (sem desconto)")
    print("3 - Cartao (8% acrescimo)")
    
    forma_pagamento = int(input("Escolha a forma (1, 2 ou 3): "))
    
    ajuste = 0.0
    nome_forma = ""

    if forma_pagamento == 1:
        nome_forma = "Convenio"
        ajuste = subtotal * -0.15
    elif forma_pagamento == 2:
        nome_forma = "Particular"
        ajuste = 0.0
    elif forma_pagamento == 3:
        nome_forma = "Cartao de Credito"
        ajuste = subtotal * 0.08
    else:
        print("Opcao invalida, vai ser particular.")
        nome_forma = "Particular"
        ajuste = 0.0

    total_final = subtotal + ajuste

    print("\n--- RESULTADO FINAL ---")
    print("Exames:")
    for i in range(len(exames_escolhidos)):
        print(exames_escolhidos[i], "-", nomes_escolhidos[i])
        
    print("Subtotal: R$", subtotal)
    print("Pagamento:", nome_forma)
    print("Ajuste: R$", ajuste)
    print("Total a pagar: R$", total_final)
else:
    print("Nenhum exame agendado.")