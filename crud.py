#Commit 1: Função limpar_tela

import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

#Commit 2: Variáveis de arquivos e função inicializar_arquivos
    
    FILENAME = "treinos.txt"
METAS_FILENAME = "metas.txt"

def inicializar_arquivos():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', encoding='utf-8') as file:
            file.write("ID|Data|Distância (km)|Tempo (min)|Localização|Clima|Tipo\n")
    if not os.path.exists(METAS_FILENAME):
        with open(METAS_FILENAME, mode='w', encoding='utf-8') as file:
            file.write("Meta|Valor|Progresso\n")

# Commit 3: Função gerar_id

def gerar_id():
    try:
        with open(FILENAME, mode='r', encoding='utf-8') as file:
            linhas = file.readlines()
            return len(linhas)
    except FileNotFoundError:
        return 1
        
# Commit 4: Função adicionar_registro (Parte 1)

def adicionar_registro():
    limpar_tela()
    print("=== Adicionar Novo Treino ou Competição ===")
    data = input("Data (DD-MM-AAAA): ")

# Commit 5: Função adicionar_registro (Parte 2)

    while True:
        try:
            distancia = float(input("Distância (km): "))
            if distancia <= 0:
                raise ValueError("Distância deve ser maior que 0.")
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")
            
# Commit 6: Função adicionar_registro (Parte 3)

    while True:
        try:
            tempo = float(input("Tempo (minutos): "))
            if tempo <= 0:
                raise ValueError("Tempo deve ser maior que 0.")
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

# Commit 7: Função adicionar_registro (Parte 4)

    localizacao = input("Localização: ")
    clima = input("Condições Climáticas: ")
    tipo = input("Tipo (Treino/Competição): ")
    novo_id = gerar_id()
    registro = f"{novo_id}|{data}|{distancia}|{tempo}|{localizacao}|{clima}|{tipo}\n"

# Commit 8: Função adicionar_registro (Parte 5)

    with open(FILENAME, mode='a', encoding='utf-8') as file:
        file.write(registro)
    input("Registro adicionado com sucesso! Pressione Enter para continuar...")
    
#Commit 9: Função listar_registros (Parte 1)

def listar_registros():
    limpar_tela()
    try:
        with open(FILENAME, mode='r', encoding='utf-8') as file:
            linhas = file.readlines()
            if len(linhas) <= 1:
                print("Nenhum registro encontrado.")
#Commit 10: Função listar_registros (Parte 2)

            else:
                print("=== Todos os Registros ===")
                for linha in linhas[1:]:
                    print(linha.strip())
    except FileNotFoundError:
        print("Arquivo de registros não encontrado.")
    input("Pressione Enter para continuar...")

#Commit 11: Função definir_meta (Parte 1)

def definir_meta():
    limpar_tela()
    print("=== Definir Meta Pessoal ===")
    meta = input("Defina a meta (ex.: Correr 100 km no mês): ")
                
# Commit 12: Função definir_meta (Parte 2)
    while True:
        try:
            valor = float(input("Qual o valor da meta (ex.: 100 km): "))
            if valor <= 0:
                raise ValueError("O valor da meta deve ser positivo.")
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

# Commit 13: Função definir_meta (Parte 3)

    with open(METAS_FILENAME, mode='a', encoding='utf-8') as file:
        file.write(f"{meta}|{valor}|0\n")
    input("Meta definida com sucesso! Pressione Enter para continuar...")

# Commit 14: Função verificar_metas (Parte 1)

def verificar_metas():
    limpar_tela()
    try:
        with open(METAS_FILENAME, mode='r', encoding='utf-8') as file:
            metas = file.readlines()
            if not metas:
                print("Nenhuma meta definida.")
                
# Commit 15: Função verificar_metas (Parte 2)

            else:
                print("=== Metas Pessoais ===")
                for meta in metas:
                    print(meta.strip())
    except FileNotFoundError:
        print("Arquivo de metas não encontrado.")
    input("Pressione Enter para continuar...")

# Commit 16: Função sugestao_treino (Parte 1)

def sugestao_treino():
    limpar_tela()
    try:
        with open(FILENAME, mode='r', encoding='utf-8') as file:
            linhas = file.readlines()
            if len(linhas) <= 1:
                print("Nenhum treino registrado para sugerir.")

# Commit 17: Função sugestao_treino (Parte 2)

            else:
                ultimo_treino = linhas[-1].strip().split('|')
                try:
                    distancia_sugerida = float(ultimo_treino[2]) + 1
                    tempo_sugerido = float(ultimo_treino[3]) + 5
                    print(f"Sugestão de treino: {distancia_sugerida:.2f} km em {tempo_sugerido:.2f} minutos.")
                except ValueError:
                    print("Erro ao processar os dados do último treino. Verifique o formato do arquivo.")
    except FileNotFoundError:
        print("Arquivo de registros não encontrado.")
    input("Pressione Enter para continuar...")

# Commit 18: Função analise_desempenho (Parte 1)

def analise_desempenho():
    limpar_tela()
    try:
        with open(FILENAME, mode='r', encoding='utf-8') as file:
            linhas = file.readlines()
            if len(linhas) <= 1:
                print("Nenhum registro encontrado para análise.")
                return

# Commit 20: Função analise_desempenho (Parte 3)

                if distancia not in melhor_rendimento or ritmo < melhor_rendimento[distancia]:
                    melhor_rendimento[distancia] = ritmo

            print(f"Distância total percorrida: {distancia_total:.2f} km")
            print(f"Tempo total: {tempo_total:.2f} minutos")
            print("Melhor ritmo por distância:")
            for distancia, ritmo in melhor_rendimento.items():
                print(f"{distancia} km: {ritmo:.2f} min/km")
    except FileNotFoundError:
        print("Arquivo de registros não encontrado.")
    input("Pressione Enter para continuar...")

# Commit 21: Função filtrar_registros (Parte 1)

def filtrar_registros():
    limpar_tela()
    print("Escolha um critério de filtragem:")
    print("1. Filtrar por Distância")
    print("2. Filtrar por Tempo")
    criterio = input("Escolha uma opção: ")
