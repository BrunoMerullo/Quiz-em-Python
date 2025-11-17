import os
import sys
import time
import perguntas

def menu():
          print('''
======MENU=====
1 - Jogar
2 - Instruções
3 - Sair
          ''')

def jogar_dificuldades():
                jogar_dificuldades = '''
1 -- Fácil
2 -- Médio
3 -- Dificíl
                                        '''
                print(jogar_dificuldades)
                
                

def sair_instrucao():
                input('Apenas digite OK, quando voce ja ter lido tudo! ')

def instrucoes_quiz():
                    
                    print ("Ok, te passarei as instruções!")
                    time.sleep(3)
                    
                    apagar_menu()


                    print('''📜 INSTRUÇÕES DO QUIZ

                      Bem-vindo ao Quiz da Marvel!
                      Seu objetivo é escolher um nível de dificuldade e responder corretamente o maior número de perguntas possível.
                🔹    Como funciona:
                      No menu principal, escolha:
                      1 — Jogar
                      2 — Instruções
                      3 — Sair
                      Quando escolher Jogar, selecione o nível:

                      1 — Fácil
                      2 — Médio
                      3 — Difícil

                      Cada nível possui uma lista de perguntas com 4 alternativas (a, b, c, d).
                      Digite apenas a letra correspondente à opção que você acha correta.

                      Para cada pergunta:

                      Se acertar → você ganha 1 ponto
                      Se errar → 0 pontos

                      No final do quiz, será exibida sua pontuação total e uma avaliação:

                      70% ou mais → Excelente! Você conhece muito do universo Marvel!
                      40% a 69% → Bom! Você está no caminho certo.
                      Abaixo de 40% → Precisa treinar mais. Continue tentando!

                      Depois do resultado, você poderá escolher:
                      Jogar novamente
                      Voltar ao menu
                      Sair''')
                    sair_instrucao()


def opcao_errada():
        print("Opção errada! Tente novamente.")
        time.sleep(2)
        menu()
        resposta_menu = int(input())

def apagar_menu():
        os.system('clear')

def iniciar_quiz_facil():
        pontos = 0
        for p in perguntas.perguntas_faceis:
                        apagar_menu()
                        print(p["pergunta"])
                        print("a)", p["a"])
                        print("b)", p["b"])
                        print("c)", p["c"])
                        print("d)", p["d"])
                        resposta = input("Sua resposta é: ").lower()
                        if resposta == p["correta"]:
                                        print("Parabéns! você ACERTOU!!!")
                                        pontos = + 1
                                        time.sleep(2)
                        else:
                            print("Bahh, você errou!")
                        
                        print(f"Sua pontuação final foi: {pontos}")
        