insira_valor = int(input("Valor: "))

try:
    while(True):

        formas_pagamento = input("Selecione a forma de pagamento: \n Debito\n Credito")

        if formas_pagamento == "Debito":

            print(f" Insira ou aproxime o cartão.\n R$:{insira_valor},00")
            break

        elif formas_pagamento == "Credito":

            print("Forma de pagamento")

            pagamento_credito = input("Selecione\n A vista \n Parcelado\n")

            if pagamento_credito == "A vista":

                print(f"Insira ou aproxime o cartão:\n {insira_valor},00")

                break

            elif pagamento_credito == "Parcelado":

                print("Quantidade de parcelas\n")

                parcelas = int(input("Digite as parcelas\n"))

                if parcelas == 2:
                    
                    print(f"1° Parcela {insira_valor/2}")
                    print(f"2° Parcela {insira_valor/2}")
                    break
                elif parcelas == 3:
                    print(f"1° Parcela {int(insira_valor/3)}")
                    print(f"2° Parcela {int(insira_valor/3)}")
                    print(f"3° Parcela {int(insira_valor/3)}")
                    break
except:
    print("Não foi possivel efetuar a solicitação")