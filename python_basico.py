#----------------------------------------------------------------------------------
# O BASICO EM PYTHON

faturamento = 1200 #tipo int -> numero inteiro
custo = 750.0 #tipo float -> casa decimal
novas_vendas = 100
faturamento = faturamento + novas_vendas
imposto = faturamento*0.10
lucro =  faturamento - custo - imposto
margem_lucro =  lucro / faturamento
mensagem = "O faturamento foi de"

print("o faturamento foi de", faturamento)
print("o custo foi de", custo)
print("o lucro foi de", lucro)

#round(margem_lucro, 2) -> arredonda

print("a margem de lucro foi de", round(margem_lucro, 2)) 
print(mensagem, faturamento)

# Mod -> % resto da divisao

print(10 % 3)
tempo_contrato = 170
tempo_anos = 170 / 12
tempo_meses = 170 % 12

#----------------------------------------------------------------------------------
#STRINGS EM PYTHON

print(f"Tempo em anos: {int(tempo_anos)} anos")
print(f"tempo em meses: {tempo_meses} meses")

email_cliente = "loschieduardo2@gmail.com"

# MAIUSCULA

email_cliente = email_cliente.upper()
print(email_cliente)

# minuscula

email_cliente = email_cliente.lower()
print(email_cliente)

# encontrar "@"

print(email_cliente.find("@")) # -1 quando nao encontrar

# tamanho do texto

print(len(email_cliente))

# pegar um cartactere

print(email_cliente[14])

# pegar um pedaco do texto

print(email_cliente[:13])
print(email_cliente[13:24])

#trocar pedaco do texto

novo_email = email_cliente.replace("gmail.com", "hotmail.com")
print(novo_email)

nome = "eduardo loschi siqueira"
print(nome.capitalize()) # Deixa a primeira letra maiuscula
print(nome.title())# Deixa a primeira letra de cada palavra em maiusculo

#pegar servidor do email

arroba = email_cliente.find("@")
servidor = email_cliente[arroba + 1:]
print(servidor)

#pegar primeiro nome

espaco = nome.find(" ")
primeiro_nome = nome[:espaco]
print(primeiro_nome.capitalize())

#pegar sobrenome

sobrenome = nome[espaco + 1:]
print(sobrenome.title())

#casos especias - formatacao numerica em texto

margem_lucro = round(margem_lucro, 2)
print(f"Faturamento da empresa: R${faturamento:.2f}, Custo: R${custo:.2f}, Lucro: R${lucro:.2f}, Margem de lucro: {margem_lucro:.0%}")

#----------------------------------------------------------------------------------
#INPUT EM PYTHON

email = input("digite seu email: ")
nome = input("digite seu primeiro nome: ")
nome = nome.capitalize()
print(f"email: {email}")
print(f"nome: {nome}")

faturamento = float(input("Digite o faturamento da sua empresa: "))
imposto = faturamento*0.1
total = faturamento - imposto

print(f"{nome}, enviamos um email de confirmacao para voce, no seguinte endereco: {email}. O faturamento da sua empresa depois dos impostos: {total}")

#----------------------------------------------------------------------------------
#LISTAS EM PYTHON

vendas = [50, 20, 70, 300, 700, 1000]
#soma de vendas

soma_vendas = sum(vendas)
print(soma_vendas)

#tamanho da lista

quantidade_dias = len(vendas)
print(quantidade_dias)

#max e min

maximo = max(vendas)
minimo = min(vendas)
print(minimo)
print(maximo)

#pegar posicao

print(vendas[3])

#procurar elementos dentro de uma lista

lista_produtos = ["iphone", "macbook", "airpod", "ipad", "airtag"]
produto_digitado = input("Digite o produto que deseja: ")
produto_digitado = produto_digitado.lower()
print(produto_digitado in lista_produtos)

#Adicionar um item

lista_produtos.append("apple watch")
print(lista_produtos)

#Remover um item

lista_produtos.remove("apple watch")
print(lista_produtos)
lista_produtos.pop(0)
print(lista_produtos)

#Editar um item

precos = [1000, 3500, 1500]
precos[0] = 6000
print(precos)

#Contar quantas vezes o item aparece na lista

lista_produtos = ["iphone", "macbook", "airpod", "ipad", "airtag", "iphone", "ipad", "iphone"]
print(f"{lista_produtos.count('iphone')} iphones aparecem na lista")

#Ordenar uma lista

lista_produtos.sort(reverse = True)
print(lista_produtos)

#----------------------------------------------------------------------------------
#CONDICIONAIS EM PYTHON

vendas = float (input("Digite quanto voce vendeu: "))
meta = 2000

if vendas < meta:
  print("Vendedor ainda nao atingiu a meta")
else:
  print("Vendedor atingiu a meta!!")
  bonus = 0.1 * vendas
  print(f"bonus do vendedor: {bonus:.1f}")

#Segundo caso (diferentes tipos de bonus)
#PODEMOS usar and e or para fazer multiplas operacoes

vendas = float (input("Digite quanto voce vendeu: "))
meta = 2000
if vendas >= 2500:
  bonus = 0.15 * vendas
elif vendas >= 2000:
  bonus = 0.13 * vendas
else:
    bonus = 0
print(f"Bonus total de: {bonus}")

#Terceiro caso(lista de produtos com IF)

lista_produtos = ["iphone", "macbook", "ipad", "airpods"]
produto_procurado = input("Digite o produto: ")
produto_procurado = produto_procurado.lower()

if produto_procurado in lista_produtos:
  print(f"O produto {produto_procurado} existe")
else:
  print("O produto procurado nao existe nos estoques")

#----------------------------------------------------------------------------------
#LOOPS EM PYTHON

lista_vendas = [1000, 800, 400, 300, 1500, 1600, 700]
bonus_venda = 0.1

for venda in lista_vendas:
  if venda >= 550:
    total = bonus_venda * venda
    print(f"{venda} Ganhou bonus de: {total}")
  else:
    print(f"{venda} Nao elegivel para bonus")

#----------------------------------------------------------------------------------
#DICIONARIOS EM PYTHON

dic_produtos = {"iphone":5000, "airpad": 3000, "macbook": 8000, "airpod": 1500}

#Pegar um elemento

print(dic_produtos["iphone"])

#Editar um elemento

dic_produtos["iphone"] = dic_produtos["iphone"] * 1.2
print(dic_produtos)

#Quantidade de itens

print(len(dic_produtos))

#Retiar um item

dic_produtos.pop("airpod")
print(dic_produtos)

#Add um item

dic_produtos["apple watch"] = 2500
print(dic_produtos)

#Verificar se um item existe

if "iphone" in dic_produtos:
  print("item existe")
else:
  print("item nao existe")

#Verificar se um valor existe

if 6000 in dic_produtos.values():
  print("valor existe")
else:
  print("valor inexistente")

#Exercicio 1 (cadastrar produtos atraves do input do usuario)

novo_produto = input("digite o nome do produto: ")
novo_valor = input("digite o valor do produto: ")

novo_produto = novo_produto.lower()
novo_valor = float(novo_valor)

dic_produtos[novo_produto] = novo_valor
print(dic_produtos)

#Agora o programa tem que atualizar a tabela de valores, todos aumentaram 10%

for item in dic_produtos:
  novo_preco = round(dic_produtos[item] * 1.1, 1)
  dic_produtos[item] = novo_preco

print(f"novo valor atualizado dos produtos: {dic_produtos}")
