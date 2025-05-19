#python jogadores.py
import csv
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') 
jogadores = []

with open("BRA_players.csv", mode="r") as arq:
  dados_csv = csv.DictReader(arq)
  for linha in dados_csv:
    jogadores.append(linha)


def titulo(texto):
  print()
  print(texto)
  print("-"*40)


def top10_clubes():
    
    titulo("Clubes + Valiosos")

    valiosos = {}

    for jogador in jogadores:
      clube = jogador['Team']
      if jogador['Market Value'] == '':
        valor = 0
      else:        
        valor = float(jogador['Market Value'])  
      valiosos[clube] = valiosos.get(clube, 0) + valor
      #valiosos('São Paulo':450000, 'Internacional':380000)  
    valiosos2 = dict(sorted(valiosos.items(),
                             key= lambda valioso: valioso[1], reverse=True))  
    print("Nº Nome do clube......: R$ Total.........:")  
    
    for num, (clube, valor) in enumerate(valiosos2.items(), start=1):
      valor2 = locale.currency(valor, grouping=True, symbol=None)
      print(f"{num:2} {clube:20s} {valor2:>15s}")
      if num == 10:
        break
  
def equipes_idade():
   titulo("Top 10 jogadores + Experientes")

   jogadores2 = sorted(jogadores,
                        key=lambda jogador: int(jogador['Age']), reverse=True)
   print(f"\nNº Nome do jogador....: Clube..........: Idade.:")
   print(    "-----------------------------------------------")

   for num, jogador in enumerate(jogadores2, start=1): 
     print(f"{num:2d} {jogador['Player']:20s} {jogador['Team']:16s} {jogador['Age']} anos")
     if num == 10:
       break
       
   print("\n")
   titulo("Top 10 jogadores + Jovens")

   jogadores3 = reversed(jogadores2)
   print(f"\nNº Nome do jogador....: Clube..........: Idade.:")
   print(    "-----------------------------------------------")

   for num, jogador in enumerate(jogadores3, start=1): 
     print(f"{num:2d} {jogador['Player']:20s} {jogador['Team']:16s} {jogador['Age']} anos")
     if num == 10:
       break
  
def compara_clubes():
  titulo("Compara clube")

  clube1 = input("1º Clube: ")
  clube2 = input("2º Clube: ")

  num1 = 0
  soma1 = 0
  num2 = 0 
  soma2 = 0
  
  for jogador in jogadores:
    if jogador['Team'].upper() == clube1.upper():
      num1 = num1 + 1
      soma1 = soma1 + int(jogador['Age'])
    elif jogador['Team'].upper() == clube2.upper():
      num2 = num2 + 1
      soma2 = soma2 + int(jogador['Age'])
  print(f"Média da Idade ddos jogador do {clube1}: {soma1/num1:4.1f} anos")
  print(f"Média da Idade ddos jogador do {clube2}: {soma2/num2:4.1f} anos")
  #alt + shift + setabaixo
  
def pesquisa_jogador():
    titulo("Pesquisa Jogador")

    nome = input("Nome do Jogador: ")

    lista = [jogador for jogador in jogadores if nome.upper() in jogador['Player'].upper() ]

    if len(lista) == 0:
      print(f"Não há jogadores com o nome: {nome}")
    else:
      print(f"\nNome do jogador.....: Clube.............:")  

      for jogador in lista:
        print(f"{jogador['Player']:20s}{jogador['Team']}")
  
def analisa_idade():
    titulo("Analisa Clubes por Idade")

    idade = int(input("Idade: "))
   #converter em conjunto elimina as repetições
    clubes = set([jogador['Team'] for jogador in jogadores if int(jogador['Age']) == idade])
    clubes2 = sorted(list(clubes))

    print(f"Clubes com Jogadores {idade} anos: {', '.join(clubes2)}")

    todos_clubes = set( [jogador['Team'] for jogador in jogadores] )
    # usa o método difference() para "subtrair" todos os clubes de clubes
    clubes_sem = todos_clubes.difference(clubes)

    clubes3 = sorted(list(clubes_sem))

    print(f"Clubes que não possuem Jogadores com {idade} anos: {', '.join(clubes3)}")




while True:
  titulo("Dados do Brasileirao 2024")
  print("1. Top 10 Clubes + Valiosos")
  print("2. Top 10 idades (Jovem/Experiente)")
  print("3. comparar dois clubes")
  print("4. pesquisar jogador")
  print("5. analizar por idade")
  print("6. Finalizar")   
  opcao = int(input("Opção: "))
  if opcao == 1:
    top10_clubes()
  elif opcao == 2:
    equipes_idade()
  elif opcao == 3:
    compara_clubes()
  elif opcao == 4:
    pesquisa_jogador()
  elif opcao == 5:
    analisa_idade()
  else:
    break
  