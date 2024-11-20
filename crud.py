# Commit 1: Função limpar_tela

import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Commit 2: Variáveis de arquivos e função inicializar_arquivos
    
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

#Commit 16: Função sugestao_treino (Parte 1)

def sugestao_treino():
    limpar_tela()
    try:
        with open(FILENAME, mode='r', encoding='utf-8') as file:
            linhas = file.readlines()
            if len(linhas) <= 1:
                print("Nenhum treino registrado para sugerir.")
                
# Commit 12: Função definir_meta (Parte 2)
    while True:
        try:
            valor = float(input("Qual o valor da meta (ex.: 100 km): "))
            if valor <= 0:
                raise ValueError("O valor da meta deve ser positivo.")
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

