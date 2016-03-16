# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Guia', color="#c8ffc8")
define p = Character("[povname]")
define s = Character("[password]")

define num_Questao = 3

#Connection
init python:

    #Funções de save/load desabilitadas
    _game_menu_screen = "preferences"
    config.quit_action = Quit(confirm=False)

# The game starts here.
label start:

    e "Bem vindo à pesquisa interativa da Fatec!."
    
   #retorno =  teste_print("Poi")
   #e "Será que [retorno] funciona?"

    e "Aqui, você vai aprender sobe suas próprias competências, 
    por meio de um simples joguinho de perguntas e respostas!"

    #   login e senha
label login_e_senha:
python:
    povname = renpy.input("Qual é o seu e-mail?")
    povname = povname.strip()
    password = renpy.input("E qual a sua senha?")
    password =password.strip()
    
menu confirmacao:
    e "Então, seu e-mail é [povname], e sua senha é [password], correto?"
    
    "Sim!":
        jump envio_login
    "Pensando bem... Não.":
        jump login_e_senha
    
label envio_login:
        #   enviar login e senha
        #       $ if "Login sucedido"   jump inicio
        #       $else
        #               e "Um... Seu login ou senha estão errados... Vamos tentar de novo."
        #               jump login_e_senha
    
label inicio:
    e "Ótimo! Então, podemos começar para valer!"
    e "Aqui vai a primeira pergunta!"
    jump new_scene
    
label new_scene:
    
    python: 
        import json
        import urllib2
        class JSON():
            #METODO CONSTRUTOR
            def __init__(self, linkJSON):
                self.linkJSON = linkJSON    
                
            #METODO QUE CARREGA OS DADOS
            def getCarregaDados(self):
                requestResult = urllib2.Request(self.linkJSON)
                opener = urllib2.build_opener()                
                f = opener.open(requestResult)
                dataJSON = json.loads(f.read())        
                return dataJSON
        
            #METODO QUE RETORNA UMA PERGUNTA ESPECIFICA
            def getQuestaoCompleta(self, numPergunta):
                for question in self.getCarregaDados():
                    if question['number'] == numPergunta:
                        return question['question'], \
                               question['answers'][0]['answer'], \
                               question['answers'][1]['answer'], \
                               question['answers'][2]['answer'], \
                               question['answers'][3]['answer']
                return None
                
            def getPergunta(self, numPergunta):
                for question in self.getCarregaDados():
                    if question['number']== numPergunta:
                        return question['question']
                        
            def getPrimeiraAlternativa(self, numPergunta):
                for question in self.getCarregaDados():
                    if question['number']== numPergunta:
                        return question['answers'][0]['answer']
                        
            def getSegundaAlternativa(self, numPergunta):
                for question in self.getCarregaDados():
                    if question['number']== numPergunta:
                        return question['answers'][1]['answer']
                        
            def getTerceiraAlternativa(self, numPergunta):
                for question in self.getCarregaDados():
                    if question['number']== numPergunta:
                        return question['answers'][2]['answer']
                        
            def getQuartaAlternativa(self, numPergunta):
                for question in self.getCarregaDados():
                    if question['number']== numPergunta:
                        return question['answers'][3]['answer']
                        
        testejson = JSON('http://api.myjson.com/bins/51nfb')
    
   # $ dadosJSON = testejson.getQuartaAlternativa(3)
    #e"[dadosJSON]"
    
   # $ q1 = getPergunta(self, numPergunta)
    
    #   recolher variáveis vindas do servidor
    
    #   $ n_questao = dic["number"]
    #$ questao_1="Aqui deveria ter uma pergunta, mas... Pode escolher qualquer letra."
    python:
        questao_1 = testejson.getPergunta(num_Questao)
    #variável vinda do json (questão 1)
    $ resposta_1a =  testejson.getPrimeiraAlternativa(num_Questao)
    #variável vinda do json (resposta 1)
    $ resposta_1b= testejson.getSegundaAlternativa(num_Questao)
    #variável vinda do json (resposta 2)
    $ resposta_1c= testejson.getTerceiraAlternativa(num_Questao)
    #variável vinda do json (resposta 3)
    $ resposta_1d= testejson.getQuartaAlternativa(num_Questao)
    #variável vinda do json (resposta 4)
    
menu:
    #   e "Pergunta número [n_questao]"
    e "[questao_1]"
    
    "[resposta_1a]":
        jump r_a
    "[resposta_1b]":
        jump r_b
    "[resposta_1c]":
        jump r_c
    "[resposta_1d]":
        jump r_d
        
label r_a:
    e "Você escolheu a resposta A"
    #enviar letra da resposta
    jump question_next
label r_b:
    e "Você escolheu a resposta B"
    #enviar letra da resposta
    jump question_next
label r_c:
    e "Você escolheu a resposta C"
    #enviar letra da resposta
    jump question_next
label r_d:
    e "Você escolheu a resposta D"
    #enviar letra da resposta
    jump question_next

label question_next:
        
#       $ if "mensagem de termino" == True
#       $          jump final
#       $else jump transicao

label transicao:
        e "Próxima pergunta!"
        num_Questao = num_Questao + 1
        # jump new_scene
        
label final:
    e "...Eh? Era a última pergunta? Sério?"
    e "Bem, parece que o quiz acabou. Obrigado pela participação!"
    e "Até a próxima!"
    
