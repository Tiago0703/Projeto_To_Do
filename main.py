import json
import os

# Nome do arquivo para armazenar as tarefas
ARQUIVO_TAREFAS = "tarefas.json"

# Lista global de tarefas
tarefas = []

# Função para carregar tarefas do arquivo
def carregar_tarefas():
    global tarefas
    if os.path.exists(ARQUIVO_TAREFAS):
        try:
            with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as arquivo:
                tarefas = json.load(arquivo)
        except json.JSONDecodeError:
            print("Erro ao carregar o arquivo. Iniciando com lista vazia.")
            tarefas = []
    else:
        tarefas = []

# Função para salvar tarefas no arquivo
def salvar_tarefas():
    try:
        with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as arquivo:
            json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Erro ao salvar tarefas: {e}")

def adicionar_tarefa(qual_tarefa):
    tarefa = {"qual_tarefa": qual_tarefa, "concluida": False}
    tarefas.append(tarefa)
    salvar_tarefas()  # Salva após adicionar
    print(f"A tarefa '{qual_tarefa}' foi adicionada!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    for i, tarefa in enumerate(tarefas, 1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i}. {tarefa['qual_tarefa']} - {status}")

def marcar_concluida(indice):
    if 1 <= indice <= len(tarefas):
        tarefas[indice-1]["concluida"] = True
        salvar_tarefas()  # Salva após marcar como concluída
        print(f"Tarefa '{tarefas[indice-1]['qual_tarefa']}' marcada como concluída!")
    else:
        print("Índice inválido!")

def remover_tarefa(indice):
    if 1 <= indice <= len(tarefas):
        tarefa = tarefas.pop(indice-1)
        salvar_tarefas()  # Salva após remover
        print(f"Tarefa '{tarefa['qual_tarefa']}' removida com sucesso!")
    else:
        print("Índice inválido!")

def menu():
    carregar_tarefas()  # Carrega as tarefas ao iniciar
    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ")
        
        if opcao == "1":
            qual_tarefa = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(qual_tarefa)
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            listar_tarefas()
            try:
                indice = int(input("Digite o número da tarefa a marcar como concluída: "))
                marcar_concluida(indice)
            except ValueError:
                print("Por favor, digite um número válido.")
        elif opcao == "4":
            listar_tarefas()
            try:
                indice = int(input("Digite o número da tarefa a remover: "))
                remover_tarefa(indice)
            except ValueError:
                print("Por favor, digite um número válido.")
        elif opcao == "5":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()

input("Pressione Enter para sair...")
