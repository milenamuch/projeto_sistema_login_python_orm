from controller import ControllerCadastro, ControllerLogin
import os
while True:
    print('= = = = = MENU = = = = = ')
    escolha = int(input(
                            f'\nSeja bem vindo!\n'
                            f'[1] Cadastrar usuário\n'
                            f'[2] Login\n'
                            f'[3] Sair\n'
                            f'Qual é a sua escolha? '))
    
    if escolha == 1:
        print('= = = = = CADASTRO DE USUAŔIO = = = = =')
        nome = input('Digite o seu nome: ')
        email = input('Digite seu email: ')
        senha = input('Digite a senha: ')
        resultado = ControllerCadastro.cadastrar(nome, email, senha)
        
        if resultado == 2:
            print('\nO nome precisa conter mais do que dois caracteres.')
        elif resultado == 3:
            print('\nO email cadastrado passou do tamanho limite de 200 caracteres.')
        elif resultado == 4:
            print('\nA senha precisa ter entre 6 e 100 caracteres.')
        elif resultado == 5:
            print('\nEste email já está cadastrado.')
        elif resultado == 6:
            print('\nErro interno do sistema.')
        elif resultado == 1:
            print('\nCadastro realizado com sucesso!')
    elif escolha == 2:
        print('= = = = = LOGIN DE USUAŔIO = = = = =')
        email = input('Digite seu email: ')
        senha = input('Digite a senha: ')
        resultado = ControllerLogin.login(email,senha)
        if not resultado:
            print('Email ou senha inválidos.')
        else:
            print(resultado)
    elif escolha == 3:
        break
    else:
        print("Escolha um valor válido.")
