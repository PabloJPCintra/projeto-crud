SISTEMA DE CONTROLE DE TREINOS E COMPETIÇÕES DE CORREDORES:

Este sistema tem como objetivo controlar os treinos e competições de corredores, proporcionando funcionalidades que ajudam o usuário a registrar treinos, estabelecer metas e monitorar seu desempenho ao longo do tempo. Além disso, o sistema sugere treinos de forma off-line com base em registros anteriores e fornece uma análise detalhada da interação com o atleta.

ESTRUTURA DE ARMAZENAMENTO DE DADOS
Os dados são armazenados em dois arquivos TXT:
treinos.txt (para registros de treinos e competições)
metas.txt (para registros de metas estabelecidas pelo usuário)

FUNÇÕES E MÉTODOS
O código é composto por diversas funções e métodos, cada um responsável por uma tarefa específica:

Função limpar_tela() :
Realiza a limpeza da tela do terminal, adaptando-se automaticamente ao sistema operacional (Windows ou Linux).

Função inicializar_arquivos() :
Verifica se os arquivos de metas e treinos existem. Se algum estiver ausente, ele cria o arquivo com uma mensagem de cabeçalho.

Função gerar_id() :
Atribui um ID único aos novos registros de treinos ou competições com base no número de linhas já existentes no arquivo.

Função adicionar_registro() :
Permite ao usuário adicionar um novo treino ou competição, registrando informações como:

1)Data

2)Distância

3)Tempo

4)Local

5)Condições climáticas

6)Tipo do evento

7)Esses dados são então armazenados no arquivo treinos.txt.

8)Função listar_registros()

9)Exibe todos os registros contidos no arquivo treinos.txt.


Função definir_meta() :
Permite ao usuário definir uma meta, como correr uma determinada distância em um mês. A meta é registrada no arquivo metas.txt.

Função verificar_metas() :
Lê as metas definidas e, caso nenhuma meta tenha sido estabelecida, notifica o usuário sobre a ausência de metas.

Função sugestao_treino() :
Baseada no último registro de treino, sugere um aumento na distância e tempo para a próxima sessão de treino, estimulando o progresso do atleta.

Função analise_desempenho() : 
Realiza uma análise detalhada do desempenho do corredor, incluindo:

1)Distância total percorrida

2)Tempo total gasto

3)Melhor ritmo por distância Para cada distância registrada.


Função filtrar_registros() :
Permite ao usuário filtrar os registros com base em critérios específicos, como:

Distância mínima
Duração máxima

Funcionamento do Programa:

O programa é baseado em um menu principal, no qual o usuário pode escolher diferentes opções. Ele continuará executando até que o usuário escolha sair. Além disso, o código possui controles de erro robustos. Blocos try-except são usados para garantir que o usuário insira apenas dados válidos, como distâncias e tempos positivos. Se arquivos essenciais estiverem ausentes, o programa cria automaticamente os arquivos necessários para continuar a execução sem interrupções.
