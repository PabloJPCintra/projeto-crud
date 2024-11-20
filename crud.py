# Commit 1: Função limpar_tela
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
#Commit 4: Função adicionar_registro (Parte 1)

def adicionar_registro():
    limpar_tela()
    print("=== Adicionar Novo Treino ou Competição ===")
    data = input("Data (DD-MM-AAAA): ")

#Commit 7: Função adicionar_registro (Parte 4)

    localizacao = input("Localização: ")
    clima = input("Condições Climáticas: ")
    tipo = input("Tipo (Treino/Competição): ")
    novo_id = gerar_id()
    registro = f"{novo_id}|{data}|{distancia}|{tempo}|{localizacao}|{clima}|{tipo}\n"

#Commit 12: Função definir_meta (Parte 2)
    while True:
        try:
            valor = float(input("Qual o valor da meta (ex.: 100 km): "))
            if valor <= 0:
                raise ValueError("O valor da meta deve ser positivo.")
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

#Commit 3: Função gerar_id

def gerar_id():
    try:
        with open(FILENAME, mode='r', encoding='utf-8') as file:
            linhas = file.readlines()
            return len(linhas)
    except FileNotFoundError:
        return 1
