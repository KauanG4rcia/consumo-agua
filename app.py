##Entrada
opcao = input("Qual seu tipo de Imóvel (Comercial - Casa - Apartamento): ")
consumo_agua = float(input("Qual seu consumo mensal de água em metros cúbicos (m3): "))

##Condicional caso o usuário digite uma opção inválida
if opcao not in ("Comercial", "Casa", "Apartamento"):
    print("Opção inválida. Por favor, escolha entre Comercial, Casa ou Apartamento.")
##Condicional para verificar o tipo de imóvel e o consumo de água
elif opcao in "Comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo")
elif opcao in "Apartamento" and consumo_agua <= 10: 
    print("Consumo econômico – excelente controle de água!")
elif opcao in ("Apartamento", "Casa") and consumo_agua <= 25:
    print ("Consumo moderado – dentro do padrão residencial")
else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
