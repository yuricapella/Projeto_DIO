nome = input("Informe o seu nome: ")
sobrenome = input("Informe o seu sobrenome: ")
idade = input("Informe a sua idade: ")

print(nome,idade)
print("teste", end=" ")
print(nome,idade, end=" ...\n")
print(nome,idade, sep="#", end=" ... \n")
print(nome,idade, sep="#")
print("------------------")
print(nome,end="...")
print(nome)
print("------------------")
print(nome,sobrenome,idade,sep="#")
print("------------------")
print("Cliente: ",nome,sobrenome,idade, sep="|",end="| essas são as informações do cliente!")