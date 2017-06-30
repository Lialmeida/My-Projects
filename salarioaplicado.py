print('----Programa de cálculo de porcentagem salarial----\n')
print('==========================================================================')
salario = float(input('\nPor favor insira o seu salário:R$ '))
aumento = float(input('Por favor insira o aumento em % a ser aplicado: '))
calc = (salario + (salario * aumento /100))
print('Seu antigo salário é R$%6.2f, seu novo salário com o aumento de %d por cento será de: R$%6.2f' %(salario, aumento, calc),'\n')
print('==========================================================================')
import os
os.system('pause')
