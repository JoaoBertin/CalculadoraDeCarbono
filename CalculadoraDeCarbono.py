
#--------------------------------------------- Funções ------------------------------------------------------

def calcular_eletricidade():
# Estrutura de Seleção de Casos do Consumo de Eletricidade Residencial
    opcao_eletricidade = str(input("1 para calcular em kWh\n2 para calcular em R$\nDigite o valor desejado: "))
    match opcao_eletricidade:

        case "1":
# Calculo de emissões por kWh de Consumo Elétrico Residencial:
            consumo_eletricidade = float(input("Digite o valor de kWh consumidos em um mês: "))
# Atribuição da variável kwh para o futuro cálculo de Geração de Energia Elétrica
            kwh = consumo_eletricidade
# Quantidade de kWh consumidos * emissão em kg de CO² por kWh
            kg_carbono_eletricidade = kwh * 0.0385

        case "2":
# Calculo de emissões por R$ de Consumo Elétrico Residencial:
            consumo_eletricidade = float(input("Digite o valor em R$ do consumo de eletricidade mensal: "))
# Mesma coisa do último caso, atribuição da variável kwh para o futuro cálculo de Geração de Energia Elétrica
# (Valor total da conta de luz (R$) - (média de bandeira tarifária) - (COSSIP)) / pela taxa média de kWh
            kwh = (consumo_eletricidade - (consumo_eletricidade * 0.018) - (consumo_eletricidade * 0.03))/0.80
# Quantidade de kWh consumidos * emissão em kg de CO² por kWh
            kg_carbono_eletricidade = kwh * 0.0817 

        case _:
            print("Digite um número válido")

# Calculo de Geração de Energia Elétrica Residencial:
    opcao_geracao = str(input("\nUtiliza meios de Geração de Energia Elétrica? S/N"))
# Função que converte a string em maiúscula. O usuário pode secrever "n" ou "N" sem problemas
    opcao_geracao = opcao_geracao.upper()
# Encadeamento de IFs para as diferentes Opção de Geração
    if (opcao_geracao == "S") or (opcao_geracao == "SIM"):
        geracao_eletricidade = str(input("1 para Energia Solar\n2 para Energia Eólica\nDigite o valor desejado: "))
        if geracao_eletricidade == 1:
            gerador_eletricidade = float(input("Digite o valor em kWh mensal da geração de Energia Solar da sua residência: "))
        elif geracao_eletricidade == 2:
            gerador_eletricidade = float(input("Digite o valor em kWh mensal da geração de Energia Eólica da sua residência: "))
        else:
            print("Digite um número válido")
    elif (opcao_geracao == "N") or (opcao_geracao == "NAO") or (opcao_geracao == "NÃO"):
# Caso o usuário não tenha um meio de gereação de energia, define o número de kWh gerados como 0 para o cálculo de emissões totais
        gerador_eletricidade = 0
    else:
        print("Digite um número válido")
# Quantidade de kWh gerados * emissão em kg de CO² por kWh
    kg_carbono_evitado = gerador_eletricidade * 0.0817
    kg_carbono_eletricidade_total = kg_carbono_eletricidade - kg_carbono_evitado

    return (kg_carbono_evitado, kg_carbono_eletricidade_total)

def calcular_gas():
# Estrutura de Seleção de Casos do Consumo de Gás
    opcao_gas = str(input("1 para calcular em m³\n2 para calcular em quantidade de botijões\n3 para calcular em R$\nDigite o valor desejado: "))
    match opcao_gas:

        case "1":
# Calculo de emissões por m³ de Consumo de Gás Residencial:
            consumo_gas = float(input("Digite o valor de m³ de consumo de gás mensal: "))
# Quantidade de m³ consumidos * o peso (kg) do m³ de GLP * emissão em kg de CO² por kg de GLP queimado
            kg_carbono_gas = consumo_gas * 2.3 * 3.02

        case "2":
# Calculo de emissões por Quantidade de Botijões de Consumo de Gás Residencial:
            consumo_gas = int(input("Digite a Quantidade de Botijões de gás consumidos em um mês: "))
# Quantidade de botijões consumidos * o peso (kg) do botijão médio * emissão em kg de CO² por kg de GLP queimado
            kg_carbono_gas = consumo_gas * 13 * 3.02

        case "3":
# Calculo de emissões por R$ de Consumo de Gás Residencial:
            consumo_gas = float(input("Digite o valor em R$ de consumo de gás mensal: "))
# ((Valor da conta - (valor aproximado de impostos (25%))) / valor (R$) do m³ de GLP) * o peso (kg) que cada m³ tem * emissão em kg de CO² por kg de GLP queimado
            kg_carbono_gas = ((consumo_gas - (consumo_gas * 0.25))/ 7.785) * 2.3 * 3.02
            
        case _:
            print("Digite um número válido")

    return kg_carbono_gas

def calcular_transporte_individual():
    transporte_individual = []
# Início da Iteração do Transporte Individual
    while True:
        print("Adicione o meio de Transporte Indvidual utilizado:")
        opcao_transporte_individual = str(input("1 para Carro\n2 para Moto\n3 para Van\n4 para Caminhão\n5 para Bicicleta\n6 para Bicicleta Elétrica\n7 para Patinete Elétrico\n8 caso não tenha usado Transporte Indiviudal\n0 caso queira concluir\nDigite o valor desejado: "))
# Estrutura de Seleção de Casos do Transporte Individual
        match opcao_transporte_individual:

            case "1":
# Uso da variável "carro_total" para calcular a emissão de carros híbridos, fazendo ele entrar mas duas condições e somar as duas emissões, tanto a combustão como elétrica
                carro_total = 0
                print("\nQuantos Quilômetros percorridos de Carro?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
                print("\nQual o Tipo do seu carro?")
                tipo = int(input("1 para Combustão\n2 para Elétrico\n3 para Híbrido\nDigite o valor desejado: "))
# Encadeamento de IFs para os diferentes Tipos de Carros
                if (tipo == 1) or (tipo == 3):
                    print("\nQual o Combustível do seu Carro?")
                    combustivel = int(input("1 para Gasolina\n2 para Etanol\n3 para Diesel\n4 para GNV\nDigite o valor desejado: "))
                    print("\nQual o Rendimento do seu Carro?")
                    rendimento = int(input("Digite quantos km/l (quilômetros por litro) o seu carro faz com o combustível: "))
                    if combustivel == 1:
# Distância em km * (emissão em kg de CO² do combustível / rendimento)
                        carro = km * (2.28/rendimento)
                    elif combustivel == 2:
# *Pra descobrir a emissão do etanol, usei o link indicado que deu apenas a emissão do álcool etílico hidratado misturado em 23% de gasolina (0.389kg). Sendo assim, multipliquei esse valor por 4.348 (100%/23%) para conseguir a emissão por litro de etanol 
                        carro = km * (1.691/rendimento)
                    elif combustivel == 3:
                        carro = km * (2.6/rendimento)
                    elif combustivel == 4:
# *De acordo com nossa fonte, a emissão do GNV é 15% menor que a do etanol. Sendo assim, 1.691 - 15% de 1.691 dá 1.437kg de CO² 
                        carro = km * (1.437/rendimento)
                    carro_total = carro + carro_total
                    
                if (tipo == 2) or (tipo == 3):
                    print("\nQual a Autonomia do seu Carro?")
                    autonomia = float(input("Digite a autonomia da bateria do seu carro em km: "))
                    print("\nQual a Capacidade Total da Bateria do seu Carro?")
                    capacidade_bateria = float(input("Digite a quantidade em kWh da Capacidade Total da bateria: "))
# Distância em km * (consumo do carro em kWh por km) * emissão em kg de CO² por kWh
                    carro = km * (capacidade_bateria/autonomia) * 0.0385
                    carro_total = carro + carro_total
                transporte_individual.append(carro_total)

            case "2":
# Novamente, uso da variável "moto_total" para calcular a emissão de motos híbridas, fazendo ele entrar mas duas condições e somar as duas emissões, tanto a combustão como elétrica
                moto_total = 0
                print("\nQuantos Quilômetros percorridos de Moto?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
                print("\nQual o Tipo da sua Moto?")
                tipo = int(input("1 para Combustão\n2 para Elétrico\n3 para Híbrido\nDigite o valor desejado: "))
# Encadeamento de IFs para os diferentes Tipos de Motos
                if (tipo == 1) or (tipo == 3):
                    print("\nQual o Combustível da sua Moto?")
                    combustivel = int(input("1 para Gasolina\n2 para Etanol\n3 para Diesel\n4 para GNV\nDigite o valor desejado: "))
                    print("\nQual o Rendimento da sua Moto?")
                    rendimento = int(input("Digite quantos km/l (quilômetros por litro) a sua moto faz com o combustível: "))
                    if combustivel == 1:
# Distância em km *  (emissão em kg de CO² do combustível / rendimento)
                        moto = km * (2.28/rendimento)
                    elif combustivel == 2:
                        moto = km * (1.691/rendimento)
                    elif combustivel == 3:
                        moto = km * (2.6/rendimento)
                    elif combustivel == 4:
                        moto = km * (1.437/rendimento)
                    moto_total = moto + moto_total
                    
                if (tipo == 2) or (tipo == 3):
                    print("\nQual a Autonomia da sua Moto?")
                    autonomia = float(input("Digite a autonomia da bateria da sua moto em km: "))
                    print("\nQual a Capacidade Total da bateria da sua Moto?")
                    capacidade_bateria = float(input("Digite a quantidade em kWh da Capacidade Total da bateria: "))
# Distância em km * (consumo da moto em kWh por km) * emissão em kg de CO² por kWh
                    moto = km * (capacidade_bateria/autonomia) * 0.0385
                    moto_total = moto + moto_total
                transporte_individual.append(moto_total)

            case "3":
# Calculo de emissões por Van de Transporte Individual:
                print("\nQual a Categoria da sua Van (toneladas)?")
                categoria = int(input("1 se for de até 1.305t\n2 se for de 1.305t a 1.74t\n3 se for de 1.74t a 3.5t\nDigite o valor desejado: "))
                print("\nQual o Peso Transportado?")
                carga = float(input("Digite a Carga Transportada (toneladas) pela Van: "))
                print("\nQuantos Quilômetros percorridos de Van?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# Encadeamento de IFs para as diferentes Categorias de Vans
                if categoria == 1:
# Distância em km * emissão em kg de CO² da categoria de Van * carga transportada
                    van = km * 0.77 * carga
                elif categoria == 2:
                    van = km * 0.60 * carga
                elif categoria == 3:
                    van = km * 0.56 * carga
                transporte_individual.append(van)

            case "4":
# Calculo de emissões por Caminhão de Transporte Individual:
                print("\nQual o tipo do seu Caminhão?")
                tipo = int(input("1 para Rígido\n2 para Articulado\nDigite o valor desejado: "))
                print("\nQual a Categoria do seu Caminhão (toneladas)?")
# Encadeamento de IFs para os diferentes Tipos e Categorias de Caminhões
                if tipo == 1:
                    categoria = int(input("1 se for de 3.5t a 7.5t\n2 se for de 7.5t a 17t\n3 se for acima de 17t\nDigite o valor desejado: "))
                    print("\nQual o Peso Transportado?")
                    carga = float(input("Digite a Carga Transportada (toneladas) pelo Caminhão: "))
                    print("\nQuantos Quilômetros percorridos de Caminhão?")
                    km = float(input("Digite a quantidade de km rodados em um mês: "))
                    if categoria == 1:
# Distância em km * emissão em kg de CO² da categoria de Caminhão * carga transportada
                        caminhao = km * 0.46 * carga
                    elif categoria == 2:
                        caminhao = km * 0.32 * carga
                    elif categoria == 3:
                        caminhao = km * 0.17 * carga
                elif tipo == 2:
                    categoria = int(input("\n1 se for de 3.5t a 33t\n2 se for acima de 33t:\nDigite o valor desejado: "))
                    print("\nQual o Peso Transportado?")
                    carga = float(input("Digite a Carga Transportada (toneladas) pelo Caminhão: "))
                    print("\nQuantos Quilômetros percorridos de Caminhão?")
                    km = float(input("Digite a quantidade de km rodados em um mês: "))
                    if categoria == 1:
                        caminhao = km * 0.12 * carga
                    elif categoria == 2:
                        caminhao = km * 0.76 * carga
                transporte_individual.append(caminhao)  

            case "5":
# Calculo de emissões por Bicicleta de Transporte Individual:
                print("\nQuantos Quilômetros percorridos de Bicicleta?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# A ideia aqui é calcular a emissão evitada utilizando bicicleta. Os valores são de um carro a gasolina
                bike_evitada = km * (2.28/9.83)
                transporte_individual.append(bike)

            case "6":
# Calculo de emissões por Bicicleta Elétrica de Transporte Individual:
                print("\nQuantos Quilômetros percorridos de Bicicleta Elétrica?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# Distância em km * emissão em kg de CO² de Bicicleta Elétrica
                bicicleta_eletrica = km * 0.022
                transporte_individual.append(bicicleta_eletrica)

            case "7":
# Calculo de emissões por Patinete Elétrico de Transporte Individual:
                print("\nQuantos Quilômetros percorridos de Patinete Elétrico?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# Distância em km * emissão em kg de CO² de Patinete Elétrico
                patinete_eletrico = km * 0.125
                transporte_individual.append(patinete_eletrico)

# Fim da Iteração do Transporte Individual
            case "0":
                print(" * Transporte Individual Finalizado * ")
                break

            case _:
                print("Digite um número válido")
        
    soma_transporte_individual = sum(transporte_individual)
    return soma_transporte_individual

def calcular_transporte_coletivo():
    transporte_coletivo = []
# Início da Iteração do Transporte Coletivo
    while True:
        print("Adicione o meio de Transporte Coletivo utilizado:")
        opcao_transporte_coletivo = str(input("1 para Táxi\n2 para Metrô\n3 para Trem\n4 para Ônibus Municipal\n5 para Ônibus de Viagem\n6 caso não tenha usado Transporte Coletivo\n0 caso queira concluir\nDigite o valor desejado: "))
# Estrutura de Seleção de Casos do Transporte Coletivo
        match opcao_transporte_coletivo:

            case "1":
# Calculo de emissões por Táxi de Transporte Coletivo:
                print("\nQuantos Quilômetros percorridos de Táxi?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# Distância em km * emissão em kg de CO² de Táxi
                taxi = km * 0.19
                transporte_coletivo.append(taxi)

            case "2":
# Cálculo de emissões por Metrô de Transporte Coletivo:
                print("\nQuantos Quilômetros percorridos de Metrô?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# Distância em km * emissão em kg de CO² de Metrô
                metro = km * 0.006
                transporte_coletivo.append(metro)
                print(transporte_coletivo)

            case "3":
# Cálculo de emissões por Trêm de Transporte Coletivo:
                print("\nQuantos Quilômetros percorridos de Trêm?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# Distância em km * emissão em kg de CO² por Passageiro/km
                trem = km * 0.019
                transporte_coletivo.append(trem)

            case "4":
# Cálculo de emissões por Ônibus de Transporte Coletivo:
                print("\nQuantos Quilômetros percorridos de Ônibus Municipal?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# Distância em km * emissão em kg de CO² de Ônibus
                onibus = km * 0.080
                transporte_coletivo.append(onibus)

            case "5":
# Cálculo de emissões por Ônibus de Viagem de Transporte Coletivo:
                print("\nQuantos Quilômetros percorridos de Ônibus de Viagem?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# Distância em km * emissão em kg de CO² de Ônibus de Viagem
                onibus_viagem = km * 0.080
                transporte_coletivo.append(onibus_viagem)

# Fim da Iteração do Transporte Coletivo
            case "0":
                print(" * Transporte Coletivo Finalizado * ")
                break

            case _:
                print("Digite um número válido")
        
    soma_transporte_coletivo = sum(transporte_coletivo)
    return soma_transporte_coletivo

def calcular_transporte_viagem():
    transporte_viagem = []
# Início da Iteração do Transporte de Viagem
    while True:
        print("Adicione o meio de Transporte de Viagem utilizado:")
        opcao_transporte_viagem = str(input("1 para Avião\n2 para Barco\n3 para Návio\n4 caso não tenha usado Transporte de Viagem\n0 caso queira concluir\nDigite o valor desejado: "))
# Estrutura de Seleção de Casos do Transporte Coletivo
        match opcao_transporte_viagem:

            case "1":
# Calculo de emissões por Avião de Transporte de Viagem:
                print("\nQuantos Quilômetros percorridos de Avião?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# Distância em km * emissão em kg de CO² de avião por passageiro/km
                aviao = km * 0.123
                transporte_viagem.append(aviao)

            case "2":
# Calculo de emissões por Barco de Transporte de Viagem:
                print("\nQuantos Quilômetros percorridos de Barco?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# Distância em km * emissão em kg de CO² de barcos pequenos
# *Fiz uma conta maluca, usei o valor de emissão em libras de CO² por galão de diesel marinho (21.24) e converti em kg por litro (2.547). Depois fiz a média de rendimento milhas/l (0.91) para km/l (1.464). Então, peguei a emissão de CO² por litro de combustível e descobri quantos quilômetro rendem um litro, multiplicando os dois, temos a emissão a cada km (maluquice)
                barco = km * 3.977
                transporte_viagem.append(barco)

            case "3":
# Calculo de emissões por Návio de Transporte de Viagem:
                print("\nQual o tipo do Návio?")
                tipo = int(input("1 para Cruzeiro\n2 para Petroleiro\n3 para Container\n4 para Graneleiro\nDigite o valor desejado: "))
                print("\nQuantos Quilômetros percorridos de Návio?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
                if tipo == 1:
# Distância em km * emissão em kg de CO² de návio (Cruzeiro) por Passageiro/km
                    navio = km * 0.245
                elif tipo == 2:
# Distância em km * emissão em kg de CO² do tipo de návio
# *Usei a emissão de CO² em toneladas emitidas durante um ano (exemplo graneleiro: 6023248.78), dividi esse valor pelo número de návios do mesmo ano (145) e consegui a emissão por ano de cada návio (41539.647). Após isso, converti esse número de 1 ano para 1 hora (4.808) e tranformei em kg (4808). Por último, dividi pela velocidade do tipo em km/h (37.781), conseguindo assim a emissão por km (127.260) (usei o mesmo procedimento em cada um dos 3 tipos)
                    navio = km * 207.798
                elif tipo == 3:
                    navio = km * 418.236
                elif tipo == 4:
                    navio = km * 127.260
                transporte_viagem.append(navio)

# Fim da Iteração do Transporte de Viagem
            case "0":
                print(" * Transporte de Viagem Finalizado * ")
                break

            case _:
                print("Digite um número válido")
        
    soma_transporte_viagem = sum(transporte_viagem)
    return soma_transporte_viagem

# ---------------------------------------- Início da Execução ------------------------------------------

iniciar = str(input("Deseja iniciar a Calculadora de Carbono? S/N: "))
# Função que converte a string em maiúscula. O usuário pode secrever "n" ou "N" sem problemas
iniciar = iniciar.upper()
# Iniciando Iteração do Programa
while True:

    if (iniciar == "S") or (iniciar == "SIM"):
# Definindo as variáveis como 0 para que o usuário possa cálcular apenas a emissão que ele quer sem dar conflito cálculo final
        total_eletricidade = 0
        total_gas = 0
        total_transporte_individual = 0
        total_transporte_coletivo = 0
        total_transporte_viagem = 0
        print("\n------------------------ Iniciando Calculadora de Carbono ------------------------")
# Início da Iteração do Tipo de Emissão
        while True:
            print("\nQual Emissão você quer calcular?")
            tipo_emissao = str(input("1 para Eletricidade\n2 para Gás de Cozinha\n3 para Transporte Individual\n4 para Transporte Coletivo\n5 para Transporte de Viagem\n0 para ver o resultado das Emissões\nDigite o valor desejado: "))
# Estrutura de Seleção de Casos do Tipo de Emissão
            match tipo_emissao:

                case "1":
# Início do Cálculo de Consumo Elétrico
                    print("\n * Cálculo do Consumo de Eletricidade Residencial * ")
                    total_eletricidade = (calcular_eletricidade())/1000

                case "2":
# Início do Cálculo de Consumo de Gás
                    print("\n * Cálculo do Consumo de Gás Residencial * ")
                    total_gas = calcular_gas()/1000

                case "3":
# Início do Cálculo de Transporte Individual
                    print("\n * Cálculo do Consumo de Transporte Individual * ")
                    total_transporte_individual = calcular_transporte_individual()/1000

                case "4":
# Início do Cálculo de Transporte Coletivo
                    print("\n * Cálculo do Consumo de Transporte Coletivo * ")
                    total_transporte_coletivo = calcular_transporte_coletivo()/1000

                case "5":
# Início do Cálculo de Transporte de Viagem
                    print("\n * Cálculo do Consumo de Transporte de Viagem * ")
                    total_transporte_viagem = calcular_transporte_viagem()/1000
                
# Fim da Iteração do Tipo de Emissão
                case "0":
                    break

                case _:
                    print("Digite um número válido")

# Somatória de todas as emissões com uma função de arredondamento
        total_emissoes = round(total_eletricidade + total_gas + total_transporte_individual + total_transporte_coletivo + total_transporte_viagem, 3)
# Quantidade de árvores a serem plantadas = emissões em toneladas de CO² * quantidade de árvores necessárias para absorverem 1 tonelada de CO²
        arvores_reposicao = total_emissoes * 7.14
# Quantidade de m² de árvores a serem plantadas = quantidade de árvores a serem plantadas * quantidade de m² que cada árvore ocupa
        m2_reposicao = arvores_reposicao * 6
# 1 Crédito de Carbono = 1 tonelada de CO²
        creditos_carbono = total_emissoes
# R$ a serem doados = Créditos de Carbono * valor em R$ de cada crédito
        reais_doacao = creditos_carbono * 25
            
# Exibição dos Resultados dos Cálculos
        print("\n * Resultados dos Cálculos * ")
        print("Fonte                   Emissões(tCO²e)           %")
        print(f"Eletricidade                {total_eletricidade:.3f}               {total_eletricidade/total_emissoes:.2%}")
        print(f"Gás                         {total_gas:.3f}               {total_gas/total_emissoes:.2%}")
        print(f"Transporte Individual       {total_transporte_individual:.3f}               {total_transporte_individual/total_emissoes:.2%}")
        print(f"Transporte Coletivo         {total_transporte_coletivo:.3f}               {total_transporte_coletivo/total_emissoes:.2%}")
        print(f"Transporte de Viagem        {total_transporte_viagem:.3f}               {total_transporte_viagem/total_emissoes:.2%}")
        print(f"Total                       {total_emissoes}               {total_emissoes/total_emissoes:.2%}")
        print(f"\nPara compensar a quatidade de gases emitidos:\nÉ preciso restaurar {m2_reposicao:.2f}m² de árvores\nOu plantar {arvores_reposicao:.0f} árvore(s)")
        print(f"Doe R${reais_doacao:.2f} para ajudar a mitigar os impactos causados\nO enquivalente a {creditos_carbono:.0f} crédito(s) de carbono")
        print("Obrigado por dar um passo a diante e tentar se tornar uma pessoa mais consciente!")
        encerrar = int(input("\nDeseja Repetir ou Encerrar a Cálculadora de Carbono?\n1 para Repetir\n2 para Encerrar\nDigite o valor desejado: "))

# Se o usuário desejar, o programa repetirá todos os passos até ser encerrado
        if encerrar == 1:
            continue

# --------------------------------------Finalização da Execução ------------------------------------------

        if encerrar == 2:
            print("\n------------------------ Programa Encerrado ------------------------\n")
            break 

# Fim da Iteração do Programa
    elif (iniciar == "N") or (iniciar == "NÃO") or (iniciar == "NAO"):
        print("\n------------------------ Programa Encerrado ------------------------\n")
        break

    else:
        print("Digite um comando válido")
        break
