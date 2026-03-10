sexo = str(input('Informe seu sexo:')).upper().strip()[0]
while sexo not in ('M', 'F'):
      sexo = str(input('Dados inválidos. Por favor, informe seu sexo:')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso')



