print(True and True)
print(True and False)
print(False and False)

print(True or True)
print(True or False)
print(False or False)

print("---------separador---------")

saldo = 1000
saque = 200
limite = 100
conta_especial = True



retirar_dinheiro = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(retirar_dinheiro)

retirar_dinheiro_dois = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(retirar_dinheiro_dois)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

retirar_dinheiro_tres = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(retirar_dinheiro_tres)
