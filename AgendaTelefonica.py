#ALUNOS: LUIZ GONZAGA,KLEYTHON DUARTE ROCHA, SEVERINO DO RAMO

agenda = []

def inserirNome():
      return input("Nome: ")

def inserirTelefone():
      return input("Telefone: ")

def inserirEmail():
      return input("E-mail: ")

def dados(nome, telefone, email):
      print("Nome: %s | Telefone: %s | E-mail: %s" % (nome, telefone, email))

def nomeArquivo():
      return input("Nome do arquivo: ")

def pesquisar(nome):
      mnome = nome.lower()
      for p, e in enumerate(agenda):
            if e[0].lower() == mnome:
                  return p
      return None

def adicionar():
      print("Informe os dados do novo contato: ")
      global agenda
      nome = inserirNome()
      telefone = inserirTelefone()
      email = inserirEmail()
      agenda.append([nome, telefone, email])
      print("Contato adicionado com sucesso!")

def alterar():
      print("Digite o nome do contato que deseja alterar")
      p = pesquisar(nomeArquivo())
      if p is not None:
            nome = agenda[p][0]
            telefone = agenda[p][1]
            email = agenda[p][2]
            print("\nContato encontrado: ")
            dados(nome, telefone, email)
            print("Informe os novos dados")
            nome = inserirNome()
            telefone = inserirTelefone()
            email = inserirEmail()
            agenda[p] = [nome, telefone, email]
            print("\nContato alterado com sucesso!\n")
      else:
            print("\nContato não encontrado.\n")

def excluir():
      print("Informe o nome do contato que deseja excluir")
      global agenda
      nome = inserirNome()
      p = pesquisar(nome)
      if p is not None:
            del agenda[p]
            print("\nContato excluído com sucesso!")
      else:
            print("\nContato não encontrado. \n")

def listar():
      print("\n ***** Lista de contatos: ***** \n"
            "\n_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
      for e in agenda:
            dados(e[0], e[1], e[2])
      print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

def zerar():
      global agenda
      if len(agenda) != 0:
            agenda.clear()
            print("\n...Apagando todos os contatos"
                  "\nTodos os contatos foram excluídos!\n")
      else:
            print("\nLista telefônica encontra-se vazia!\n")

def menu():
    print("\n ***** Agenda Telefônica ***** \n"
          "\nOpções:\n"
          "1 - Adicionar contato\n"
          "2 - Alterar contato\n"
          "3 - Apagar contato\n"
          "4 - Ver todos os contatos\n"
          "5 - Apagar todos os contatos\n"
          "0 - Fechar agenda\n")
    return int(input("Digite a opção que deseja executar: "))

while True:
      opcao = menu()
      if opcao == 0:
            print("...fechando agenda!")
            break
      elif opcao == 1:
            adicionar()
      elif opcao == 2:
            alterar()
      elif opcao == 3:
            excluir()
      elif opcao == 4:
            listar()
      elif opcao == 5:
            zerar()
      else:
            print("Valor inválido, verifique e informe um valor correto.")