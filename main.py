import functions
import os
import sys

resposta_menu = 1


while not(resposta_menu == 3) :
        functions.apagar_menu()
        functions.menu()
        resposta_menu = int(input())

        if resposta_menu == 1:
                        functions.apagar_menu()
                        print("Ok, vamos jogar!")
                        input("Digite 1 para começar a jogar!")
                        
                        

        elif resposta_menu == 2:
                        functions.apagar_menu()
                        functions.instrucoes_quiz()
                        
                        
        elif resposta_menu == 3:
                print('Ok, adeus!')
                break   

        else:
            print('Erro')

            
            
                
                        

                
        

    



            
       
            

    