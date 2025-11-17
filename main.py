import functions
import perguntas
import os
import sys

resposta_menu = 0


while True :
        functions.apagar_menu()
        functions.menu()
        resposta_menu = int(input())

        if resposta_menu == 1:
                        functions.apagar_menu()
                        print("Ok, vamos jogar!")
                        functions.apagar_menu()
                        functions.jogar_dificuldades()
                        opcao_dificuldades = int(input())

                        match opcao_dificuldades:
                                case 1:
                                        print('Lets play!')
                                        functions.iniciar_quiz_facil()

                                        
                                case 2:
                                        print('Opção média.')
                                      
                                case 3:
                                        print('Opção Dificil')
                                       
                        

        elif resposta_menu == 2:
                        functions.apagar_menu()
                        functions.instrucoes_quiz()
                        
                        
        elif resposta_menu == 3:
                print('Ok, adeus!')
                break   

        else:
            print('Erro')

            
            
                
                        

                
        

    



            
       
            

    