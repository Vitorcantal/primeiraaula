#Informes de salári

def calcular_media():
    print('você escolheu a função calcular media')
    n1= float(input('nota1: '))
    n2= float(input('nota2: '))
    meida= n1+n2/2
    print(meida)

def inserir_aluno():
    print('você escolheu a função inserir aluno')

def excluir_aluno():
    print('você escolheu a função excluir aluno')

def opção_invalida():
    print('opção selecionada invalida')

def menu():
    print('1- calcular a media')
    print('2- inserir aluno')
    print('3- excluir aluno ')
    escolha= input('escolha uma opção: ')

    if escolha == '1':
        calcular_media()
    elif escolha == '2':
        inserir_aluno
    elif escolha == '3':
        excluir_aluno
    else:
        opção_invalida    




























