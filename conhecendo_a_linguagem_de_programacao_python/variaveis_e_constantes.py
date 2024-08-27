import os

age = 24
name = 'Yuri'

print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade. ')

age, name = (24, 'Yuri')

print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade. ')

age, name = (27, 'Guilherme')

print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade. ')

age, name = (28, "Giovana")

print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade. ')

print("---------------------")


ABS_PATH = os.getcwd()

DEBUG = True

BRAZILIAN_STATES = [
      'MG',
      'RJ',
      'SP']

limite_saque_diario = 500 
limiteSaqueDiario = 500

print(ABS_PATH)
print(BRAZILIAN_STATES)