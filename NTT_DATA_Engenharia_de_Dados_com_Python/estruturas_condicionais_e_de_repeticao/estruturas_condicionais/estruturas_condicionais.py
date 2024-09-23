MAIOR_IDADE = 18
IDADE_ESPECIAL = False


idade = int(input("Informe sua idade: "))

if idade < MAIOR_IDADE:
  IDADE_ESPECIAL = True

if idade >= MAIOR_IDADE:
  print("Você pode fazer sua CNH")
if idade < MAIOR_IDADE:
  print("Você precisa ter 18 anos para fazer a CNH")
  
print("----------")

if idade >= MAIOR_IDADE:
  print("Você pode tirar sua CNH")
else:
  print("Você precisa ter 18 anos para tirar a CNH")
  
  print("----------")
  
if idade >= MAIOR_IDADE:
  print("Você pode fazer sua CNH")
elif IDADE_ESPECIAL:
  print("Pode fazer aulas teóricas mas não práticas")
else:
  print("Você precisa ter 18 anos para tirar a CNH")
  
print("-----caso_1-----")
conta_normal = False
conta_especial = False

if idade >= MAIOR_IDADE:
  conta_normal = True
elif IDADE_ESPECIAL:
  conta_especial = True

saldo = 2000
saque = 500
cheque_especial = 300
  
if conta_normal:
  print("Conta normal:\n")
  
  if saldo >= saque:
    print("Saque realizado")
    
  elif saque <= (saldo + cheque_especial):
    print("Saque realizado com cheque_especial")

  else:
    print("Saldo insuficiente")
    
elif conta_especial:
  print("Conta especial:\n")
  
  if saldo >= saque:
    print("Saque realizado")
    
  else:
    print("Saldo insuficiente")
    
else:
  print("Conta não identificada.")
  
print("-----caso_2-----")
saldo = 2000
saque = 2500
cheque_especial = 600

if conta_normal:
  print("Conta normal:\n")
  
  if saldo >= saque:
    print("Saque realizado")
    
  elif saque <= (saldo + cheque_especial):
    print("Saque realizado com cheque_especial")
    
  else:
    print("Saldo insuficiente")
    
elif conta_especial:
  print("Conta especial:\n")
  
  if saldo >= saque:
    print("Saque realizado")
    
  else:
    print("Saldo insuficiente")
    
else:
  print("Conta não identificada.")

print("-----caso_3-----")
saldo = 2000
saque = 2100
cheque_especial = 300
  
saque_normal = "Sucesso" if saldo >= saque else "Falha"
print(f"{saque_normal} ao realizar o saque!")

print("----------")

saque_cheque_especial = "Sucesso" if saque <= (saldo + cheque_especial) else "Falha"
print(f"{saque_cheque_especial} ao realizar o saque com cheque especial!")
print("----------")