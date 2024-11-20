import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
    
#Commit 12: Função definir_meta (Parte 2)
    while True:
        try:
            valor = float(input("Qual o valor da meta (ex.: 100 km): "))
            if valor <= 0:
                raise ValueError("O valor da meta deve ser positivo.")
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

