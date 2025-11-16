import functions
import sys

print("Olá! Bem Vindo ao meu quiz.", end='')
functions.menu()

resposta_menu = int(input())

while resposta_menu >= 4 or resposta_menu < 1 in range (True):
        if resposta_menu >= 4 or resposta_menu < 1:

                functions.opcao_errada

                retornar_opcao = input("(s/n) ")
                if retornar_opcao == "S":
                    functions.menu()
                    resposta_menu = input()
                else:
                        sys.exit()

        
if resposta_menu == 1:
        print("Ok, vamos jogar!")
        functions.retornar_menu()

elif resposta_menu == 2:
        functions.instrucoes_quiz
        functions.retornar_menu()
else:
    print('Ok, adeus!')
    sys.exit()    


    



            
       
            

    