import qrcode

def maquininha():
    insira_valor = float(input("Valor: "))

    try:
        while(True):

            formas_pagamento = input("Selecione a forma de pagamento: \n (1) Debito \n (2) Credito \n (3) Pix \n ")

            if formas_pagamento == "Debito" or formas_pagamento == "1":

                print(f" Insira ou aproxime o cartão.\n R$:{insira_valor},00")
                break

            elif formas_pagamento == "Credito" or formas_pagamento == "2":


                pagamento_credito = input("Selecione\n (1) A vista \n (2) Parcelado\n ")

                if pagamento_credito == "A vista" or pagamento_credito == "1":

                    print(f"Insira ou aproxime o cartão:\n {insira_valor},00")

                    break

                elif pagamento_credito == "Parcelado" or pagamento_credito == "2":
                    parcelas = int(input("Digite as parcelas\n"))

                if parcelas >= 2 and parcelas <= 5:
                    print("Insira ou aproxime o cartão")
                    valor_parcela = insira_valor / parcelas 
                    for i in range(parcelas):
                        print(f"{i+1}° Parcela: R${valor_parcela:.2f}")
                    break
                else:
                    print("Número de parcelas inválido. Por favor, escolha um número de parcelas entre 2 e 5.")
            elif formas_pagamento == "Pix" or formas_pagamento == "3":
                pagamento_pix = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=1)
                pagamento_pix.add_data(str(insira_valor))
                pagamento_pix.make(fit=True)

                img_pix = pagamento_pix.make_image(fill_color="black", back_color="white")
                img_pix.show()
                break

    except:
        print("Não foi possivel efetuar a solicitação")



maquininha()