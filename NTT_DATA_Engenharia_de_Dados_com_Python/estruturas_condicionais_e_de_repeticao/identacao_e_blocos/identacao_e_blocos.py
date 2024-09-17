def sacar(valor):
  saldo = 500
  
  if saldo >= valor:
    print(f"Valor sacado: {valor}")
    print("Retire seu dinheiro da boca do caixa.")
  print("Obrigado por ser nosso cliente, tenha um bom dia!")
  
    
sacar(100)
print("---")
sacar(1000)
print("---")

def depositar(valor):
  saldo = 500
  saldo += valor
  if valor:
    print(f"Valor depositado: {valor}")
    
depositar(100)
print("---")
depositar(0)
print("---")
depositar(1)