# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image imagem_questao = ""

# Declare characters used by this game.
define e = Character('Guia', color="#c8ffc8")
define p = Character("[povname]")
define s = Character("[password]")

#Variáveis Python
define login = ""
define senha = ""
define id_aluno = ""
define num_Questao = 3
define resposta = 0

#Connection
init python:

    #Funções de save/load desabilitadas
    _game_menu_screen = "preferences"
    config.quit_action = Quit(confirm=False)

# The game starts here.
label start:

    e "Bem vindo à pesquisa interativa da Fatec!."

    e "Aqui, você vai aprender sobe suas próprias competências, 
    por meio de um simples joguinho de perguntas e respostas!"

    #   login e senha
label login_e_senha:
python:
    povname = renpy.input("Qual é o seu e-mail?")
    povname = povname.strip()
    login = povname.strip()
    password = renpy.input("E qual a sua senha?")
    password =password.strip()
    senha = password.strip()
    
menu confirmacao:
    e "Então, seu e-mail é [povname], e sua senha é [password], correto?"
    
    "Sim!":
        jump envio_login
    "Pensando bem... Não.":
        jump login_e_senha
    
label envio_login:
    #   Protótipo de código de envio de login
    
    python:    
        import json
        import urllib2
        class JSON():
            #METODO CONSTRUTOR
            def __init__(self, linkJSON):
                self.linkJSON = linkJSON   
                
            def getLogin(self, login, senha):
                envioLogin = {}
                envioLogin['userName'] = login
                envioLogin['password'] = senha
                requestResult = urllib2.Request(self.linkJSON)
                opener = urllib2.build_opener()                
                f = opener.open(requestResult)
                dataJSON = json.loads(f.read())        
                return dataJSON
                # id_Aluno = *resposta do banco*
                
                
                
                testejson = JSON('http://api.myjson.com/bins/2zpad')

    
        #   enviar login e senha como objeto JSON
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
#                    if question['number'] == 'null'
#                        renpy.jump (final)
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
                        
        testejson = JSON('http://api.myjson.com/bins/2zpad')
        urllib.urlretrieve("http://s17.postimg.org/axeomjglb/hacker_cat.jpg", "01.jpg")
        imagem_questao = "01.jpg"
        #link_imagem = ('http://s17.postimg.org/axeomjglb/hacker_cat.jpg')

    #   recolher variáveis vindas do servidor
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
    show imagem_questao
    
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
    $   resposta = 1
    jump question_next
label r_b:
    e "Você escolheu a resposta B"
    $   resposta = 2
    jump question_next
label r_c:
    e "Você escolheu a resposta C"
    $   resposta = 3
    jump question_next
label r_d:
    e "Você escolheu a resposta D"
    $   resposta = 4
    jump question_next

label question_next:
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

#       Protótipo de código para envio de respostas
        class Site:
            def __init__(self, url):
                self.url = url
            def to_json(self):
                return {"url": self.url}
        class SendAnswer:
            def __init__(self, log, que, ans, site):
                self.login = log
                self.questao = que
                self.resposta = ans
                self.site = site
            def to_json(self):
                return {"login": self.login, "questao": self.questao, "resposta": self.resposta}
        class GenericJsonEncoder(json.JSONEncoder):
            def default(self, obj):
                if hasattr(obj, 'to_json'):
                    return obj.to_json()
                if isinstance(obj, datetime.datetime):
                    return obj.isoformat()
                return json.JSONEncoder.default(self, obj)

#          def sendDados(self, id_aluno, num_questao, resposta):
#               retorno = {}
#               retorno['user'] = 'id_aluno'
#               retorno['question'] = 'num_questao'
#               retorno['answer'] = 'resposta'
#       Retornar id do aluno, numero da questão e resposta

#       testeEnvio = JSON('http://api.myjson.com/bins/2zpad', login, num_questao, resposta)

label transicao:
        e "Próxima pergunta!"
        $ num_Questao += 1
        $ resposta = 0
        jump new_scene
        
label final:
    e "...Eh? Era a última pergunta? Sério?"
    e "Bem, parece que o quiz acabou. Obrigado pela participação!"
    e "Até a próxima!"
    
