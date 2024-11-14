
#--------------------------------------------- Funções ------------------------------------------------------

# Função Emissão de Carbono de Eletricidade
def calcular_eletricidade():
# Estrutura de Seleção de Casos do Consumo de Eletricidade Residencial
    print("Como deseja calcular o Consumo de Eletricidade?")
    opcao_eletricidade = str(input("1 para calcular em kWh\n2 para calcular em R$\nDigite o valor desejado: "))
    match opcao_eletricidade:

        case "1":
# Calculo de emissões por kWh de Consumo Elétrico Residencial
            consumo_eletricidade = float(input("Digite o valor de kWh consumidos em um mês: "))
# Atribuição da variável kwh para o futuro cálculo de Geração de Energia Elétrica
            kwh = consumo_eletricidade
# Quantidade de kWh consumidos * emissão em kg de CO² por kWh
            kg_carbono_eletricidade = kwh * 0.0385

        case "2":
# Calculo de emissões por R$ de Consumo Elétrico Residencial
            consumo_eletricidade = float(input("Digite o valor em R$ do consumo de eletricidade mensal: "))
# Mesma coisa do último caso, atribuição da variável kwh para o futuro cálculo de Geração de Energia Elétrica
# Valor total da conta de luz (R$) * 112.3%, que seria, de acordo com os cálculos efetuados, a porcentagem de R$ da conta para kWh
            kwh = consumo_eletricidade * 1.123
# Quantidade de kWh consumidos * emissão em kg de CO² por kWh
            kg_carbono_eletricidade = kwh * 0.0385 

        case _:
            print("Digite um número válido")

# Calculo de Geração de Energia Elétrica Residencial
    gerador_eletricidade = 0
    opcao_geracao = str(input("\nUtiliza meios de Geração de Energia Elétrica? S/N: "))
# Função que converte a string em maiúscula. O usuário pode escrever "n" ou "N" sem problemas
    opcao_geracao = opcao_geracao.upper()
# Encadeamento de IFs para as diferentes Opção de Geração
    if (opcao_geracao == "S") or (opcao_geracao == "SIM"):
        geracao_eletricidade = str(input("1 para Energia Solar\n2 para Energia Eólica\nDigite o valor desejado: "))
        if geracao_eletricidade == "1":
            gerador_eletricidade = float(input("Digite o valor em kWh mensal da geração de Energia Solar da sua residência: "))
        elif geracao_eletricidade == "2":
            gerador_eletricidade = float(input("Digite o valor em kWh mensal da geração de Energia Eólica da sua residência: "))
        else:
            print("Digite um número válido")
    elif (opcao_geracao == "N") or (opcao_geracao == "NAO") or (opcao_geracao == "NÃO"):
# Caso o usuário não tenha um meio de geração de energia, mantém o número de kWh gerados como 0 para o cálculo de emissões totais 
        geracao_eletricidade = 0
    else:
        print("Digite um número válido")
# Quantidade de kWh gerados * emissão em kg de CO² por kWh
    kg_carbono_eletricidade_evitado = gerador_eletricidade * 0.0385
# kg de CO² de eletricidade consumida - kg de CO² de eletricidade evitados 
    kg_carbono_eletricidade_total = kg_carbono_eletricidade - kg_carbono_eletricidade_evitado

    return (kg_carbono_eletricidade_total, kg_carbono_eletricidade_evitado)

# Função Emissão de Carbono de Gás
def calcular_gas():
    kg_carbono_gas = 0
    print("Qual o Gás de Cozinha utilizado?")
    tipo_gas = int(input("1 para GLP (Gás Liquefeito de Petróleo)\n2 para GN (Gás Natural)\nDigite o valor desejado: "))
    if tipo_gas == 1:
# Estrutura de Seleção de Casos do Consumo de Gás
        print("\nComo deseja calcular o Consumo de Gás de Cozinha?")
        opcao_gas = str(input("1 para calcular em m³\n2 para calcular em quantidade de botijões\nDigite o valor desejado: "))
        match opcao_gas:

            case "1":
# Calculo de emissões por m³ de Consumo de GLP
                consumo_gas = float(input("Digite o valor de m³ de consumo de gás mensal: "))
# Quantidade de m³ consumidos * o peso (kg) do m³ de GLP * emissão em kg de CO² por kg de GLP queimado
                kg_carbono_gas = consumo_gas * 2.3 * 3.02

            case "2":
# Calculo de emissões por Quantidade de Botijões de Consumo de Gás Residencial
                consumo_gas = float(input("Digite a Quantidade de Botijões de gás consumidos em um mês: "))
                peso_botijao = int(input("Digite o peso em kg de cada botijão (Ex: P13 tem 13kg, P45 tem 45kg): "))
# Quantidade de botijões consumidos * o peso (kg) do botijão médio * emissão em kg de CO² por kg de GLP queimado
                kg_carbono_gas = consumo_gas * peso_botijao * 3.02
            
            case _:
                print("Digite um número válido")
                
    elif tipo_gas == 2:
        print("\nComo deseja calcular o Consumo de Gás de Cozinha?")
        opcao_gas = str(input("1 para calcular em m³\n2 para calcular em R$ (conta)\nDigite o valor desejado: "))
        match opcao_gas:

            case "1":
# Calculo de emissões por m³ de Consumo de GN
                consumo_gas = float(input("Digite o valor de m³ de consumo de gás mensal: "))
# Quantidade de m³ consumidos * o peso (kg) do m³ de GN * emissão em kg de CO² por kg de GN queimado
                kg_carbono_gas = consumo_gas * 0.78 * 2.747

            case "2":
# Calculo de emissões por R$ de Consumo de Gás Residencial
                consumo_gas = float(input("Digite o valor em R$ de consumo de gás mensal: "))
# (Valor da conta - (ICMS de 15%)) - Termo Fixo médio (imposto)
                conta_gas = (consumo_gas - (consumo_gas * 0.15)) - 15.02
# (Valor da conta sem impostos / valor (R$) do m³ de GN) * o peso (kg) que cada m³ tem * emissão em kg de CO² por kg de GN queimado
                kg_carbono_gas = (conta_gas/ 7.785) * 0.78 * 2.747
            
            case _:
                print("Digite um número válido")

    return kg_carbono_gas

# Função Emissão de Carbono de Transporte Individual
def calcular_transporte_individual():
    transporte_individual = []
    transporte_individual_evitado = []
# Início da Iteração do Transporte Individual
    while True:
        print("Adicione o(s) meio(s) de Transporte Individual utilizado(s):")
        opcao_transporte_individual = str(input("1 para Carro\n2 para Moto\n3 para Van\n4 para Caminhão\n5 para Bicicleta\n6 para Bicicleta Elétrica\n7 para Patinete Elétrico\n0 caso queira concluir\nDigite o valor desejado: "))
# Estrutura de Seleção de Casos do Transporte Individual
        match opcao_transporte_individual:

            case "1":
# Definindo as variáveis como 0 para poder calcular a emissão de carros híbridos sem problemas, fazendo ele entrar nas duas condições e somar as duas emissões, tanto a combustão como elétrica
                carro_total = 0
                carro_evitado = 0
                carro_evitado_total = 0
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
# Distância em km * (emissão em kg de CO² do combustível por km)
                        carro = km * (1.68/rendimento)
                    elif combustivel == 2:
                        carro = km * (0.014/rendimento)
# Cálculo da emissão evitada ao utilizar o etanol ao invés de um carro a gasolina. A conta se utiliza da quantidade percorrida em km * (emissão de kg de CO² da gasolina em um carro por km) subtraído pela emissão do veículo comparado (nesse caso o carro a etanol)
# A conta se sucede a mesma em todos os cálculos de emissões evitadas por transportes
                        carro_evitado = km * (1.68/rendimento) - carro
                    elif combustivel == 3:
                        carro = km * (2.38/rendimento)
                    elif combustivel == 4:
                        carro = km * (2.12/rendimento)
                    carro_total = carro_total + carro
                    carro_evitado_total = carro_evitado_total + carro_evitado
                    
                if (tipo == 2) or (tipo == 3):
                    print("\nQual a Autonomia do seu Carro?")
                    autonomia = float(input("Digite a autonomia da bateria do seu carro em km: "))
                    print("\nQual a Capacidade Total da Bateria do seu Carro?")
                    capacidade_bateria = float(input("Digite a quantidade em kWh da Capacidade Total da bateria: "))
# Distância em km * (consumo do carro em kWh por km) * emissão em kg de CO² por kWh
                    carro = km * (capacidade_bateria/autonomia) * 0.0385
# Cálculo da emissão evitada ao utilizar o carro/motor elétrico ao invés de um carro a gasolina
                    carro_evitado = km * (1.68/9.83) - carro
                    carro_total = carro + carro_total
                    carro_evitado_total = carro_evitado_total + carro_evitado
                transporte_individual.append(carro_total)
                transporte_individual_evitado.append(carro_evitado_total)

            case "2":
# Novamente, uso da variável "moto_total" para calcular a emissão de motos híbridas, fazendo ele entrar nas duas condições e somar as duas emissões, tanto a combustão como elétrica
                moto_total = 0
                moto_evitado = 0
                moto_evitado_total = 0
                print("\nQuantos Quilômetros percorridos de Moto?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
                print("\nQual o Tipo da sua Moto?")
                tipo = int(input("1 para Combustão\n2 para Elétrico\n3 para Híbrido\nDigite o valor desejado: "))
# Encadeamento de IFs para os diferentes Tipos de Motos
                if (tipo == 1) or (tipo == 3):
                    print("\nQual o Combustível da sua Moto?")
                    combustivel = int(input("1 para Gasolina\n2 para Etanol\nDigite o valor desejado: "))
                    print("\nQual o Rendimento da sua Moto?")
                    rendimento = int(input("Digite quantos km/l (quilômetros por litro) a sua moto faz com o combustível: "))
                    if combustivel == 1:
# Distância em km * (emissão em kg de CO² do combustível / rendimento)
                        moto = km * (1.68/rendimento)
                    elif combustivel == 2:
                        moto = km * (0.014/rendimento)
# Cálculo da emissão evitada ao utilizar o etanol ao invés de uma moto a gasolina. Para uma comparação justa, no cálculo da moto a emissão de kg de CO² da gasolina é da moto por km (o mesmo vale pro seguinte cálculo)
                        moto_evitado = km * (1.68/rendimento) - moto
                    moto_total = moto + moto_total
                    moto_evitado_total = moto_evitado_total + moto_evitado
                    
                if (tipo == 2) or (tipo == 3):
                    print("\nQual a Autonomia da sua Moto?")
                    autonomia = float(input("Digite a autonomia da bateria da sua moto em km: "))
                    print("\nQual a Capacidade Total da bateria da sua Moto?")
                    capacidade_bateria = float(input("Digite a quantidade em kWh da Capacidade Total da bateria: "))
# Distância em km * (consumo da moto em kWh por km) * emissão em kg de CO² por kWh
                    moto = km * (capacidade_bateria/autonomia) * 0.0385
# Cálculo da emissão evitada ao utilizar a moto/motor elétrico ao invés de uma moto a gasolina
                    moto_evitado = km * (1.68/40) - moto
                    moto_total = moto + moto_total
                    moto_evitado_total = moto_evitado_total + moto_evitado
                transporte_individual.append(moto_total)
                transporte_individual_evitado.append(moto_evitado_total)

            case "3":
# Calculo de emissões por Van de Transporte Individual
                print("\nQual a Categoria da sua Van (toneladas)?")
                categoria = int(input("1 se for de até 1.30t\n2 se for de 1.30t a 1.74t\n3 se for de 1.74t a 3.5t\nDigite o valor desejado: "))
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
# Calculo de emissões por Caminhão de Transporte Individual
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
                    categoria = int(input("1 se for de 3.5t a 33t\n2 se for acima de 33t:\nDigite o valor desejado: "))
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
# Calculo de emissões por Bicicleta de Transporte Individual
                print("\nQuantos Quilômetros percorridos de Bicicleta?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
                bike_evitado = km * (1.68/9.83)
# A ideia aqui é calcular a emissão evitada utilizando bicicleta
                transporte_individual_evitado.append(bike_evitado)

            case "6":
# Calculo de emissões por Bicicleta Elétrica de Transporte Individual
                print("\nQuantos Quilômetros percorridos de Bicicleta Elétrica?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# Distância em km * emissão em kg de CO² de Bicicleta Elétrica
                bicicleta_eletrica = km * 0.022
# Cálculo da emissão evitada ao utilizar a bicicleta elétrica ao invés de um carro a gasolina
                bicicleta_eletrica_evitado = km * (1.68/9.83) - bicicleta_eletrica
                transporte_individual.append(bicicleta_eletrica)
                transporte_individual_evitado.append(bicicleta_eletrica_evitado)

            case "7":
# Calculo de emissões por Patinete Elétrico de Transporte Individual:
                print("\nQuantos Quilômetros percorridos de Patinete Elétrico?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# Distância em km * emissão em kg de CO² de Patinete Elétrico
                patinete_eletrico = km * 0.125
# Cálculo da emissão evitada ao utilizar o patinete elétrico ao invés de um carro a gasolina
                patinete_eletrico_evitado = km * (1.68/9.83) - patinete_eletrico
                transporte_individual.append(patinete_eletrico)
                transporte_individual_evitado.append(patinete_eletrico_evitado)


# Fim da Iteração do Transporte Individual
            case "0":
                print(" * Transporte Individual Finalizado * ")
                break

            case _:
                print("Digite um número válido")
        
    soma_transporte_individual = sum(transporte_individual)
    soma_transporte_individual_evitado = sum(transporte_individual_evitado)
    return (soma_transporte_individual, soma_transporte_individual_evitado)

# Função Emissão de Carbono de Transporte Coletivo
def calcular_transporte_coletivo():
    transporte_coletivo = []
    transporte_coletivo_evitado = []
# Início da Iteração do Transporte Coletivo
    while True:
        print("Adicione o(s) meio(s) de Transporte Coletivo utilizado(s):")
        opcao_transporte_coletivo = str(input("1 para Táxi\n2 para Metrô\n3 para Trem\n4 para Ônibus Municipal\n5 para Ônibus de Viagem\n0 caso queira concluir\nDigite o valor desejado: "))
# Estrutura de Seleção de Casos do Transporte Coletivo
        match opcao_transporte_coletivo:

            case "1":
# Calculo de emissões por Táxi de Transporte Coletivo
                print("\nQuantos Quilômetros percorridos de Táxi?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# Distância em km * emissão em kg de CO² de Táxi
                taxi = km * 0.19
                transporte_coletivo.append(taxi)

            case "2":
# Cálculo de emissões por Metrô de Transporte Coletivo
                print("\nQuantos Quilômetros percorridos de Metrô?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# Distância em km * emissão em kg de CO² de Metrô
                metro = km * 0.006
# Cálculo da emissão evitada ao utilizar metrô ao invés de um carro a gasolina
                metro_evitado = km * (1.68/9.83) - metro
                transporte_coletivo.append(metro)
                transporte_coletivo_evitado.append(metro_evitado)

            case "3":
# Cálculo de emissões por Trem de Transporte Coletivo
                print("\nQuantos Quilômetros percorridos de Trem?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# Distância em km * emissão em kg de CO² por Passageiro/km de Trem
                trem = km * 0.019
# Cálculo da emissão evitada ao utilizar trem ao invés de um carro a gasolina
                trem_evitado = km * (1.68/9.83) - trem
                transporte_coletivo.append(trem)
                transporte_coletivo_evitado.append(trem_evitado)

            case "4":
# Cálculo de emissões por Ônibus de Transporte Coletivo:
                print("\nQuantos Quilômetros percorridos de Ônibus Municipal?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# Distância em km * emissão em kg de CO² de Ônibus
                onibus = km * 0.080
# Cálculo da emissão evitada ao utilizar ônibus ao invés de um carro a gasolina
                onibus_evitado = km * (1.68/9.83) - onibus
                transporte_coletivo.append(onibus)
                transporte_coletivo_evitado.append(onibus_evitado)

            case "5":
# Cálculo de emissões por Ônibus de Viagem de Transporte Coletivo
                print("\nQuantos Quilômetros percorridos de Ônibus de Viagem?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# Distância em km * emissão em kg de CO² de Ônibus de Viagem
                onibus_viagem = km * 0.080
# Cálculo da emissão evitada ao utilizar ônibus de viagem ao invés de um carro a gasolina
                onibus_viagem_evitado = km * (1.68/9.83) - onibus_viagem
                transporte_coletivo.append(onibus_viagem)
                transporte_coletivo_evitado.append(onibus_viagem_evitado)


# Fim da Iteração do Transporte Coletivo
            case "0":
                print(" * Transporte Coletivo Finalizado * ")
                break

            case _:
                print("Digite um número válido")
        
    soma_transporte_coletivo = sum(transporte_coletivo)
    soma_transporte_coletivo_evitado = sum(transporte_coletivo_evitado)
    return (soma_transporte_coletivo, soma_transporte_coletivo_evitado)

# Função Emissão de Carbono de Transporte de Viagem
def calcular_transporte_viagem():
    transporte_viagem = []
# Início da Iteração do Transporte de Viagem
    while True:
        print("Adicione o(s) meio(s) de Transporte de Viagem utilizado(s):")
        opcao_transporte_viagem = str(input("1 para Avião\n2 para Lancha\n3 para Navio\n0 caso queira concluir\nDigite o valor desejado: "))
# Estrutura de Seleção de Casos do Transporte Coletivo
        match opcao_transporte_viagem:

            case "1":
# Calculo de emissões por Avião de Transporte de Viagem
                print("\nQuantos Quilômetros percorridos de Avião?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# Distância em km * emissão em kg de CO² de avião por passageiro/km
                aviao = km * 0.123
                transporte_viagem.append(aviao)

            case "2":
# Calculo de emissões por Barco de Transporte de Viagem
                print("\nQuantos Quilômetros percorridos de Lancha?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
# Distância em km * emissão em kg de CO² de barcos pequenos
# *Fiz uma conta maluca, usei o valor de emissão em libras de CO² por galão de diesel marinho (21.24) e converti em kg por litro (2.547). Depois fiz a média de rendimento milhas/l (0.91) para km/l (1.464). Então, peguei a emissão de CO² por litro de combustível e descobri quantos quilômetro rendem um litro, multiplicando os dois, temos a emissão a cada km (maluquice)
                barco = km * 3.977
                transporte_viagem.append(barco)

            case "3":
# Calculo de emissões por Navio de Transporte de Viagem
                print("\nQual o tipo do Navio?")
                tipo = int(input("1 para Cruzeiro\n2 para Petroleiro\n3 para Contêiner\n4 para Graneleiro\nDigite o valor desejado: "))
                print("\nQuantos Quilômetros percorridos de Navio?")
                km = float(input("Digite a quantidade de km rodados em um mês: "))
                if tipo == 1:
# Distância em km * emissão em kg de CO² de navio (Cruzeiro) por Passageiro/km
                    navio = km * 0.245
                elif tipo == 2:
# Distância em km * emissão em kg de CO² do tipo de navio
# *Usei a emissão de CO² em toneladas emitidas durante um ano (exemplo graneleiro: 6023248.78), dividi esse valor pelo número de navios do mesmo ano (145) e consegui a emissão por ano de cada navio (41539.647). Após isso, converti esse número de 1 ano para 1 hora (4.808) e tranformei em kg (4808). Por último, dividi pela velocidade do tipo em km/h (37.781), conseguindo assim a emissão por km (127.260) (usei o mesmo procedimento em cada um dos 3 tipos)
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

# Função de Iniciar para permitir a repetição da pergunta inicial caso o usuário escreva algo diferente de SIM ou NÃO
def conferir_iniciar():

    iniciar = str(input("\nDeseja iniciar a Calculadora de Carbono? S/N: "))
# Função que converte a string em maiúscula. O usuário pode escrever "n" ou "N" sem problemas
    iniciar = iniciar.upper()
    
    if (iniciar == "S") or (iniciar == "SIM"):
# Definindo as variáveis como 0 para que o usuário possa calcular apenas a emissão que ele quer sem dar conflito cálculo final
        total_eletricidade = 0
        total_eletricidade_evitado = 0
        porcentegem_eletricidade = 0
        porcentegem_eletricidade_evitado = 0
        total_gas = 0
        porcentagem_gas = 0
        total_transporte_individual = 0
        total_transporte_individual_evitado = 0
        porcentagem_transporte_individual = 0
        porcentagem_transporte_individual_evitado = 0
        total_transporte_coletivo = 0
        total_transporte_coletivo_evitado = 0
        porcentagem_transporte_coletivo = 0
        porcentagem_transporte_coletivo_evitado = 0
        total_transporte_viagem = 0
        porcentagem_transporte_viagem = 0

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
                    tupla_eletricidade = calcular_eletricidade()
                    total_eletricidade = tupla_eletricidade[0]
                    total_eletricidade = total_eletricidade
                    total_eletricidade_evitado = tupla_eletricidade[1]
                    total_eletricidade_evitado = total_eletricidade_evitado

                case "2":
# Início do Cálculo de Consumo de Gás
                    print("\n * Cálculo do Consumo de Gás Residencial * ")
                    total_gas = calcular_gas()

                case "3":
# Início do Cálculo de Transporte Individual
                    print("\n * Cálculo do Consumo de Transporte Individual * ")
                    tupla_transporte_individual = calcular_transporte_individual()
                    total_transporte_individual = tupla_transporte_individual[0]
                    total_transporte_individual = total_transporte_individual
                    total_transporte_individual_evitado = tupla_transporte_individual[1]
                    total_transporte_individual = total_transporte_individual

                case "4":
# Início do Cálculo de Transporte Coletivo
                    print("\n * Cálculo do Consumo de Transporte Coletivo * ")
                    tupla_transporte_coletivo = calcular_transporte_coletivo()
                    total_transporte_coletivo = tupla_transporte_coletivo[0]
                    total_transporte_coletivo = total_transporte_coletivo
                    total_transporte_coletivo_evitado = tupla_transporte_coletivo[1]
                    total_transporte_coletivo = total_transporte_coletivo

                case "5":
# Início do Cálculo de Transporte de Viagem
                    print("\n * Cálculo do Consumo de Transporte de Viagem * ")
                    total_transporte_viagem = calcular_transporte_viagem()
                
# Fim da Iteração do Tipo de Emissão
                case "0":
                    break

                case _:
                    print("Digite um número válido")

# Somatória de todas as emissões com uma função de arredondamento
        total_emissoes = round(total_eletricidade + total_gas + total_transporte_individual + total_transporte_coletivo + total_transporte_viagem, 3)
# Somatória de todas as emissões evitadas com uma função de arredondamento
        total_emissoes_evitado = round(total_eletricidade_evitado + total_transporte_individual_evitado + total_transporte_coletivo_evitado, 3)
# Junção dos dois totais para ter a quantidade de emissões reais do usuário
        total_emissoes_final = (total_emissoes - total_emissoes_evitado)
# Condição que evita de aparecer um valor negativo de emissões, como -10kg de CO² por exemplo
        if total_emissoes_final < 0:
            total_emissoes_final = 0      

# Cálculo das porcentagens das emissões
        if total_emissoes > 0:
# Para a porcentagem, é preciso dividir o valor específico pelo valor total. Portanto, é necessário multiplicar por 100 para conseguir o número na formatação certa
            porcentegem_eletricidade = (total_eletricidade/total_emissoes) * 100
            porcentagem_gas = (total_gas/total_emissoes) * 100
            porcentagem_transporte_individual = (total_transporte_individual/total_emissoes) * 100
            porcentagem_transporte_coletivo = (total_transporte_coletivo/total_emissoes) * 100
            porcentagem_transporte_viagem = (total_transporte_viagem/total_emissoes) * 100
# Cálculo das porcentagens das emissões evitadas
        if total_emissoes_evitado > 0:
            porcentegem_eletricidade_evitado = (total_eletricidade_evitado/total_emissoes_evitado) * 100
            porcentagem_transporte_individual_evitado = (total_transporte_individual_evitado/total_emissoes_evitado) * 100
            porcentagem_transporte_coletivo_evitado = (total_transporte_coletivo_evitado/total_emissoes_evitado) * 100

# Divisão por 1000 nas contas para a conversão de kg de CO² emitidos para toneladas
# Quantidade de árvores a serem plantadas = emissões em toneladas de CO² * quantidade de árvores necessárias para absorverem 1 tonelada de CO²
        arvores_reposicao = (total_emissoes_final/1000) * 7.14
# Quantidade de m² de árvores a serem plantadas = quantidade de árvores a serem plantadas * quantidade de m² que cada árvore ocupa
        m2_reposicao = arvores_reposicao * 6
# Condição que faz com que caso o usuário tenha uma emissão muito baixa, mas ainda existente, o programa não fale pra ele plantar 0 árvores
        if (m2_reposicao > 0) and (arvores_reposicao < 1):
            arvores_reposicao = 1
# 1 Crédito de Carbono = 1 tonelada de CO² evitada
        creditos_carbono = total_emissoes_evitado/1000
# R$ a serem doados = quantidade de CO² emitido em toneladas equivalentes a Créditos de Carbono * valor em R$ de cada Crédito
        reais_doacao = (total_emissoes_final/1000) * 25

            
# Exibição dos Resultados dos Cálculos
        print("\n * Resultados dos Cálculos * ")
        print("Fonte                Emissões(kgCO²)   %Emissões   Evitadas(kgCO²)   %Evitadas")
        print(f"Eletricidade              {total_eletricidade:.2f}            {porcentegem_eletricidade:.1f}%           {total_eletricidade_evitado:.2f}            {porcentegem_eletricidade_evitado:.1f}%")
        print(f"Gás                       {total_gas:.2f}            {porcentagem_gas:.1f}%           ----            ---")
        print(f"Transporte Individual     {total_transporte_individual:.2f}            {porcentagem_transporte_individual:.1f}%           {total_transporte_individual_evitado:.2f}            {porcentagem_transporte_individual_evitado:.1f}%")
        print(f"Transporte Coletivo       {total_transporte_coletivo:.2f}            {porcentagem_transporte_coletivo:.1f}%           {total_transporte_coletivo_evitado:.2f}            {porcentagem_transporte_coletivo_evitado:.1f}%")
        print(f"Transporte de Viagem      {total_transporte_viagem:.2f}            {porcentagem_transporte_viagem:.1f}%           ----            ---")
        print(f"Total                     {total_emissoes:.2f}           {1:.1%}         {total_emissoes_evitado:.2f}           {1:.1%}")
        print(f"\nAo final, você emitiu {total_emissoes_final:.2f}kg de CO² e deixou de emitir {total_emissoes_evitado:.2f}kg de CO².")
        if creditos_carbono >= 1:
            print(f"Parabéns, você gerou o equivalente a {creditos_carbono} Crédito(s) de Carbono graças as emissões evitadas pelas suas ações!")
        if total_emissoes_final > 0:
            print(f"É preciso restaurar {m2_reposicao:.2f}m² de árvores ou plantar {arvores_reposicao:.0f} árvore(s).")
            print(f"Doe R${reais_doacao:.2f} para ajudar a mitigar os impactos causados.")
        print("Obrigado por dar um passo a diante e se tornar uma pessoa mais consciente utilizando a nossa Calculadora de Carbono para medir as suas emissões mensais.")

# -------------------------------------- Finalizações ou Repetições da Execução ------------------------------------------

        encerrar = str(input("\nDeseja Repetir ou Encerrar a Calculadora de Carbono?\n1 para Repetir\n2 para Encerrar\nDigite o valor desejado: "))
# Se o usuário desejar, o programa repetirá todos os passos até ser encerrado
        if encerrar == "1":
            return

# Fim da Iteração do programa
        elif encerrar == "2":
            print("\n------------------------ Programa Encerrado ------------------------\n")
            encerrar = 1
            return encerrar 

# Condição caso o usuário não digite um comando válido, retornando o loop do programa e solicitando que ele escreva novamente
        elif (iniciar != "S") or (iniciar != "SIM") or (iniciar != "N") (iniciar != "NAO") or (iniciar != "NÃO"):
            print("Digite um comando válido")
            return

# Fim da Iteração do programa caso o usuário não queira iniciar
    elif (iniciar == "N") or (iniciar == "NÃO") or (iniciar == "NAO"):
        print("\n------------------------ Programa Encerrado ------------------------\n")
        encerrar = 1
        return encerrar

# Novamente, condição caso o usuário não digite um comando válido, retornando o loop do programa e solicitando que ele escreva novamente
    elif (iniciar != "S") or (iniciar != "SIM") or (iniciar != "N") (iniciar != "NAO") or (iniciar != "NÃO"):
        print("Digite um comando válido")
        return
   
# ---------------------------------------- Início da Execução ------------------------------------------

# Iniciando Iteração inicial do programa
while True:
    encerrar = conferir_iniciar()
    if encerrar == 1:
        break
