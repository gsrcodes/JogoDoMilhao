import os
import time
import random

premio = [1000.00, 2000.00, 3000.00, 4000.00, 5000.00, 10000.00, 20000.00, 30000.00, 40000.00, 50000.00, 100000.00, 2000000.00, 300000.00, 400000.00, 500000.00, 1000000.00]
pergunta_premio = [1000, 10000, 100000, 500000]
premio_parar = [0, 1000, 2000, 3000, 4000, 5000, 10000, 20000, 30000, 40000, 50000, 100000, 200000, 300000, 400000, 500000]
premio_errar = [0, 500, 1000, 1500, 2000, 2500, 5000, 10000, 15000, 20000, 25000, 50000, 100000, 150000, 200000, 0]
carregar = 0

nivel1 = [
            'Qual é a príncipal fonte de alimentação dos macacos?',
            'Macacos são:',
            'Qual é a função da cauda dos macacos?',
            'Qual desses macacos é conhecido pela cor rosa incomum de suas nádegas?',
            'X, o curioso. Qual é o nome do famoso macaco dessa animação?',
            'Qual desses personagens da disney foi criado por macacos em sua infância?',
            'Na animação "Rei Leão", qual era o nome do macaco que ergue simba?',
            'Macacos também podem ser chamados de: '
         ]

nivel2 = [
            'Sobre o Teorema do Macaco infinito, marque a alternativa correta',
            'Quanto tempo dura a gravidez de chimpanzés, gorilas e orangotangos?',
            'Qual é a espécie de macaco de menor tamanho do mundo?',
            'Qual é a espécie de macaco de maior tamanho do mundo?',
            'Em Planeta dos Macacos, qual é o nome do lider da tribo de macacos?',
            'Qual desses macacos é conhecido pelos seus gritos extremamente barulhentos?',
            'Qual é a espécie de macaco mais inteligente?',
            'Qual é a expectativa de vida de um Gorila?',
         ]

nivel3 = [
            'O quão semelhante é o DNA Humano ao DNA de um Chimpanzé?',
            'Quantos pares de cromossomos tem um macaco?',
            'Qual foi foi a maior espécie de macaco de todos os tempos?',
            'Qual é o nome da famosa coleção de NFT onde os protagonistas são os macacos?',
            'Macacos do mar, ou Sea-Monkeys, são: ',
            'Qual desses macacos é considerado um Macaco do Velho Mundo?',
            'Qual desses macacos é considerado um Macaco do Novo Mundo?',
            'Enxergar algumas cores tornam o homem e o macaco especiais dentre os mamíferos, sendo elas:',
         ]

resposta1 = [
                'Bananas',
                'Carnívoros',
                'Balancar e equilibrar seus movimentos',
                'Orangotango',
                'Pedrinho',
                'Mickey',
                'César',
                'Símios',
                'Um macaco, digitando por um tempo infinito, escreverá um roteiro completo de Shakespeare',
                '8 meses',
                'Mico-Leão-Dourado',
                'Chimpanzé',
                'Jonas',
                'Gorila',
                'Chimpanzé',
                '20 - 25 anos',
                '10% somente',
                '21',
                'Maximus mamalias',
                'Non-Fungible Token',
                'Macacos que conseguem nadar',
                'Babuíno',
                'Macaco-Narigudo',
                'vermelha e verde',
            ]

resposta2 = [
                'Requeijão',
                'Veganos',
                'Facilita na coleta de alimentos',
                'Macaco Prego',
                'Joaozinho',
                'Tarzan',
                'Ronaldo',
                'Caninos',
                'Macacos são infinitos, nunca irão parar de se reproduzir',
                '9 meses',
                'Mico-Leão-Preto',
                'Bonobo',
                'César',
                'Bugio',
                'Sagui',
                '26 - 30 anos',
                '50%',
                '22',
                'Gigantopithecus blacki',
                'Nothing For Teams',
                'Camarões de água salgada',
                'Macaco-Aranha',
                'Mandril',
                'verde e azul',
            ]

resposta3 = [
                'Eucalipto',
                'Herbívoros',
                'Permite uma maior agilidade',
                'Mico Leão Dourado',
                'George',
                'Aladin',
                'Rafiki',
                'Osteíctes',
                'O cérebro dos macacos podem armazenar todo o conhecimento infinito do universo espacial',
                '10 meses',
                'Sagui-Pigmeu',
                'King-Kong',
                'Everton',
                'Bonobo',
                'Gorila',
                '31 - 35 anos',
                '90%',
                '23',
                'Cacajao calvus',
                'Bored Ape',
                'Peixes similares a macacos',
                'Mico-Leão-Dourado',
                'Macaco-Aranha',
                'azul e amarelo',
            ]

resposta4 = [
                'Arroz doce',
                'Onívoros',
                'O torna aerodinâmico',
                'Babuíno',
                'Jonas',
                'Pato Donald',
                'Hamood',
                'Galliformes',
                'Não existe um teorema com este nome',
                '1 a 2 anos',
                'Sagui-minimus',
                'Gorila',
                'John',
                'Chimpanzé',
                'Bugio',
                '36 - 40+ anos',
                '+ de 98%',
                '24',
                'Enormous gorilas',
                'Monkey Collection',
                'Golfinhos que emitem sons similares aos dos macacos',
                'Danio margaritatus',
                'Babuíno',
                'amarelo e vermelho',
            ]

correta =   [
                1,
                4,
                1,
                4,
                3,
                2,
                3,
                1,
                1,
                1,
                3,
                4,
                2,
                2,
                1,
                4,
                4,
                4,
                2,
                3,
                2,
                1,
                3,
                1,
            ]

gab1 = [
            'Bananas',
            'Onívoros',
            'Balancar e equilibrar seus movimentos',
            'Babuíno',
            'George',
            'Tarzan',
            'Rafiki',
            'Símios',
        ]

gab2 = [
            'Um macaco, digitando por um tempo infinito, pode escrever até um roteiro completo de Shakespeare',
            '8 meses',
            'Sagui-Pigmeu',
            'Gorila',
            'César',
            'Bugio',
            'Chimpanzé',
            '36 - 40+ anos',
       ]

gab3 = [
            '+ de 98 %',
            '24',
            'Gigantopithecus blacki',
            'Bored Ape',
            'Camarões de água salgada',
            'Babuíno',
            'Macaco-Aranha',
            'vermelha e verde',
       ]

gabarito =  [
                'Bananas',
                'Onívoros',
                'Balancar e equilibrar seus movimentos',
                'Babuíno',
                'George',
                'Tarzan',
                'Rafiki',
                'Símios',
                'Um macaco, digitando por um tempo infinito, pode escrever até um roteiro completo de Shakespeare',
                '8 meses',
                'Sagui-Pigmeu',
                'Gorila',
                'César',
                'Bugio',
                'Chimpanzé',
                '36 - 40+ anos',
                '+ de 98 %',
                '24',
                'Gigantopithecus blacki',
                'Bored Ape',
                'Camarões de água salgada',
                'Babuíno',
                'Macaco-Aranha',
                'vermelha e verde',
            ]

ajudas =    [
                'Universitários',
                'Cartas',
                'Placas',
                'Pulos'
            ]

qtde_ajudas = [
                1,
                1,
                1,
                3
              ]

while (carregar < 4):
    x = 0
    y = 4
    while (x < 5):
        os.system('cls') or None
        print('''
                                                    ~=~=~=~=~=~=~=~=~=
                                                    | Carregando.''', end='')
        print('.' * x, end='')
        print(' ' * y, end='')
        print('''|
                                                    ~=~=~=~=~=~=~=~=~=
        ''')
        x += 1
        y -= 1
        time.sleep(0.3)
    carregar += 1

os.system('cls') or None
print('''
                                                     ~=~=~=~=~=~=~=~=
                                                      | Bem vindo! |
                                                     ~=~=~=~=~=~=~=~=
''')
time.sleep(2)

os.system('cls') or None
print('''
                                    =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                     |                                                 |
                                     |  Regras básicas:                                |
                                     |  > Na primeira rodada, todas as 5 perguntas     |
                                     |    valerão mil reais, sendo eles acumulativos.  |
                                     |                                                 |
                                     |  > Na segunda rodada, todas as 5 perguntas      |
                                     |    valerão R$ 10 mil, sendo eles também         |                                             
                                     |    acumulativos.                                |
                                     |                                                 |
                                     |   > Na terceira rodada, com também 5 perguntas  |
                                     |    cada resposta acertada valerá R$ 100 mil,    |                                             
                                     |    sendo eles também acumulativos.              |
                                     |                                                 |
                                     |   > Na pergunta de número 16, o jogador poderá  |
                                     |     optar entre levar meio milhão para casa ou  |
                                     |     escolher responder a pergunta do milhão     |
                                     |                                                 |
                                     |   > Escolha a opção de resposta somente se      |
                                     |     tiver certeza!                              |
                                     |                                                 |
                                    =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=                                 
''')
time.sleep(4)
input('''
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                       | Pressione enter caso já tenha lido as regras |
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                       
                                       > ''')
os.system('cls') or None
print('''
                                       __
                                      / /___  ____ _____
                                 __  / / __ \/ __ `/ __ \ 
                                / /_/ / /_/ / /_/ / /_/ /
                                \____/\____/\__, /\____/ 
                                            /___/''')
time.sleep(0.6)
os.system('cls') or None
print('''
                                       __                         __          
                                      / /___  ____ _____     ____/ /___ 
                                 __  / / __ \/ __ `/ __ \   / __  / __ \ 
                                / /_/ / /_/ / /_/ / /_/ /  / /_/ / /_/ /
                                \____/\____/\__, /\____/   \__,_/\____/
                                            /___/''')
time.sleep(0.6)
os.system('cls') or None
print('''
                                       __                         __                   _ ____              
                                      / /___  ____ _____     ____/ /___     ____ ___  (_) / /_  ____ _____ 
                                 __  / / __ \/ __ `/ __ \   / __  / __ \   / __ `__ \/ / / __ \/ __ `/ __ |
                                / /_/ / /_/ / /_/ / /_/ /  / /_/ / /_/ /  / / / / / / / / / / / /_/ / /_/ /
                                \____/\____/\__, /\____/   \__,_/\____/  /_/_/_/ /_/_/_/_/ /_/\__,_/\____/ 
                                            /___/''')
macaco = 0
while (macaco < 10):
    time.sleep(0.3)
    os.system('cls') or None
    print('''
                                       __                         __                   _ ____              
                                      / /___  ____ _____     ____/ /___     ____ ___  (_) / /_  ____ _____ 
                                 __  / / __ \/ __ `/ __ \   / __  / __ \   / __ `__ \/ / / __ \/ __ `/ __ |
                                / /_/ / /_/ / /_/ / /_/ /  / /_/ / /_/ /  / / / / / / / / / / / /_/ / /_/ /
                                \____/\____/\__, /\____/   \__,_/\____/  /_/_/_/ /_/_/_/_/ /_/\__,_/\____/ 
                                    ___ ___    /___/                      ______    __  __                     
                                   /  |/  /____ ________ __________      / ____/___/ (_) /_(_)___  ____    
                                  / /|_/ / __ `/ ___/ __ `/ ___/ __ \   / __/ / __  / / __/ / __ \/ __ \   
                                 / /  / / /_/ / /__/ /_/ / /__/ /_/ /  / /___/ /_/ / / /_/ / /_/ / / / /   
                                /_/  /_/\__,_/\___/\__,_/\___/\____/  /_____/\__,_/_/\__/_/\____/_/ /_/
                                
                                                             ▓▓▓▓▓▓▓▓▓▓                          
                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                       ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                   ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                   ░░░░▓▓░░  ██░░░░░░  ██░░▓▓░░░░                
                                                     ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                       ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                         ▓▓░░░░░░░░░░░░░░▓▓                      
                                                           ▓▓▓▓░░░░░░▓▓▓▓                        
                                                               ▓▓▓▓▓▓        ░░                  
                                                             ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                             ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                           ▓▓▓▓░░▓▓░░▓▓▓▓
    ''')
    time.sleep(0.3)
    os.system('cls') or None
    print('''
                                       __                         __                   _ ____              
                                      / /___  ____ _____     ____/ /___     ____ ___  (_) / /_  ____ _____ 
                                 __  / / __ \/ __ `/ __ \   / __  / __ \   / __ `__ \/ / / __ \/ __ `/ __ |
                                / /_/ / /_/ / /_/ / /_/ /  / /_/ / /_/ /  / / / / / / / / / / / /_/ / /_/ /
                                \____/\____/\__, /\____/   \__,_/\____/  /_/_/_/ /_/_/_/_/ /_/\__,_/\____/ 
                                    ___ ___    /___/                      ______    __  __                     
                                   /  |/  /____ ________ __________      / ____/___/ (_) /_(_)___  ____    
                                  / /|_/ / __ `/ ___/ __ `/ ___/ __ \   / __/ / __  / / __/ / __ \/ __ \   
                                 / /  / / /_/ / /__/ /_/ / /__/ /_/ /  / /___/ /_/ / / /_/ / /_/ / / / /   
                                /_/  /_/\__,_/\___/\__,_/\___/\____/  /_____/\__,_/_/\__/_/\____/_/ /_/
                                
                                                             ▓▓▓▓▓▓▓▓▓▓                          
                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                       ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                   ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                   ░░░░▓▓░░██  ░░░░░░██  ░░▓▓░░░░                
                                                     ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                       ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                         ▓▓░░░░░░░░░░░░░░▓▓                      
                                                           ▓▓▓▓░░░░░░▓▓▓▓                        
                                                               ▓▓▓▓▓▓        ░░                  
                                                             ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                             ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                           ▓▓▓▓░░▓▓░░▓▓▓▓
    ''')
    macaco += 1
    
os.system('cls') or None 
input('''
                                       __                         __                   _ ____              
                                      / /___  ____ _____     ____/ /___     ____ ___  (_) / /_  ____ _____  
                                 __  / / __ \/ __ `/ __ \   / __  / __ \   / __ `__ \/ / / __ \/ __ `/ __ |    
                                / /_/ / /_/ / /_/ / /_/ /  / /_/ / /_/ /  / / / / / / / / / / / /_/ / /_/ /
                                \____/\____/\__, /\____/   \__,_/\____/  /_/_/_/ /_/_/_/_/ /_/\__,_/\____/ 
                                    ___ ___    /___/                      ______    __  __                     
                                   /  |/  /____ ________ __________      / ____/___/ (_) /_(_)___  ____    
                                  / /|_/ / __ `/ ___/ __ `/ ___/ __ \   / __/ / __  / / __/ / __ \/ __ \   
                                 / /  / / /_/ / /__/ /_/ / /__/ /_/ /  / /___/ /_/ / / /_/ / /_/ / / / /   
                                /_/  /_/\__,_/\___/\__,_/\___/\____/  /_____/\__,_/_/\__/_/\____/_/ /_/    
                                                       
                                                             ▓▓▓▓▓▓▓▓▓▓                          
                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                       ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                   ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                   ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                     ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                       ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                         ▓▓░░░░░░░░░░░░░░▓▓                      
                                                           ▓▓▓▓░░░░░░▓▓▓▓                        
                                                               ▓▓▓▓▓▓        ░░                  
                                                             ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                             ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                           ▓▓▓▓░░▓▓░░▓▓▓▓
                                                                                                                                     
                                            ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                             |   Para começar o jogo, pressione enter.   |
                                            ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                         
                                         > ''')
os.system('cls') or None
print('''
                                            ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                             |       Prazer! Meu nome é Muquinha!        |
                                            ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                          \/
                                                             ▓▓▓▓▓▓▓▓▓▓                          
                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                       ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                   ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                   ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                     ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                       ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                         ▓▓░░░░░░░░░░░░░░▓▓                      
                                                           ▓▓▓▓░░░░░░▓▓▓▓                        
                                                               ▓▓▓▓▓▓        ░░                  
                                                             ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                             ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                           ▓▓▓▓░░▓▓░░▓▓▓▓''')
time.sleep(2)
os.system('cls') or None
print('''
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                       | Hoje serei o seu guia no Jogo do Milhão - Macaco Edition! |
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                          \/                                                         
                                                             ▓▓▓▓▓▓▓▓▓▓                          
                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                       ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                   ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                   ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                     ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                       ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                         ▓▓░░░░░░░░░░░░░░▓▓                      
                                                           ▓▓▓▓░░░░░░▓▓▓▓                        
                                                               ▓▓▓▓▓▓        ░░                  
                                                             ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                             ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                           ▓▓▓▓░░▓▓░░▓▓▓▓''')
time.sleep(4)
os.system('cls') or None
print('''
                                                        ~=~=~=~=~=~=~=~
                                                         | Vamos lá! |
                                                        ~=~=~=~=~=~=~=~
                                                          \/                                                          
                                                             ▓▓▓▓▓▓▓▓▓▓                          
                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                       ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                   ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                   ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                     ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                       ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                         ▓▓░░░░░░░░░░░░░░▓▓                      
                                                           ▓▓▓▓░░░░░░▓▓▓▓                        
                                                               ▓▓▓▓▓▓        ░░                  
                                                             ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                             ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                           ▓▓▓▓░░▓▓░░▓▓▓▓''')
time.sleep(2)
lista_ale = []
contador = 0
contador_premio = 0
premio_atual = 0
contador2 = 0

while (contador < 15):
    
    if (contador <= 4 and contador2 == 0):
        ale = random.randint(0,7)
        while (ale in lista_ale):
            ale = random.randint(0,7)
        lista_ale.append(ale)
        aux = 0
        while (aux <= 7):
            if (gabarito[ale] == gab1[aux]):
                pergunta = nivel1[aux]
            aux += 1
            
    if (contador >= 5 and contador2 == 0 and contador < 10):
        contador_premio = 1
        ale = random.randint(8,15)
        while (ale in lista_ale):
            ale = random.randint(8,15)
        lista_ale.append(ale)
        aux = 0
        while (aux <= 7):
            if (gabarito[ale] == gab2[aux]):
                pergunta = nivel2[aux]
            aux += 1
            
    if (contador >= 10 and contador2 == 0):
        contador_premio = 2
        ale = random.randint(16,23)
        while (ale in lista_ale):
            ale = random.randint(16,23)
        lista_ale.append(ale)
        aux = 0
        while (aux <= 7):
            if (gabarito[ale] == gab3[aux]):
                pergunta = nivel3[aux]
            aux += 1
    contador3 = 0
    contador2 = 0
    acao = 4
    while (acao < 1 or acao > 3):
        os.system('cls') or None
        print('''
                                        =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                        
                ▓▓▓▓▓▓▓▓▓▓                  Rodada: %d                              
              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                Pergunta valendo R$ %.2f                     
            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                                                    
          ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓            > %s         
      ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                                                                           
      ░░░░▓▓░░██  ░░░░░░██  ░░▓▓░░░░        1 - %s                                                                           
        ░░▓▓░░████░░░░░░████░░▓▓░░                                                                                         
          ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓            2 - %s                           
            ▓▓░░░░░░░░░░░░░░▓▓                                                                                     
              ▓▓▓▓░░░░░░▓▓▓▓                3 - %s                           
                  ▓▓▓▓▓▓        ░░                                                                             
                ▓▓▓▓▓▓▓▓▓▓      ▓▓          4 - %s                          
                ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                                                                               
               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            Prêmio total caso pare: R$ %.2f              
               ▓▓▓▓░░▓▓░░▓▓▓▓               Prêmio total caso erre: R$ %.2f                  
                                                    
                                        =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
        ''' % (contador + 1, pergunta_premio[contador_premio], pergunta, resposta1[ale],
            resposta2[ale], resposta3[ale], resposta4[ale], premio_parar[contador], premio_errar[contador]))
        try:
            acao = int(input('''
                                                ~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                | Insira:              |
                                                | 1- Responder         |
                                                | 2- Usar ajudas       |
                                                | 3- Parar             |
                                                ~=~=~=~=~=~=~=~=~=~=~=~=~= 
                                                
                                                > '''))
        except:
            os.system('cls') or None
            print('''                 
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                       |  ERRO! Não foi inserido um número inteiro!! |
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                        \/           
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
            time.sleep(3)
            contador2 = 1
        
        if (acao < 1 or acao > 3):
            os.system('cls') or None
            print('''                 
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                       |            Ei! Resposta Inválida!          |
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                        \/           
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
            time.sleep(3)
        if (acao == 2):
            ajuda = 6
            while (ajuda < 1 or ajuda > 5):
                os.system('cls') or None
                print('''
                                        =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                        
                ▓▓▓▓▓▓▓▓▓▓                  Rodada: %d                              
              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                Pergunta valendo R$ %.2f                     
            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                                                    
          ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓            > %s         
      ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                                                                           
      ░░░░▓▓░░██  ░░░░░░██  ░░▓▓░░░░        1 - %s                                                                           
        ░░▓▓░░████░░░░░░████░░▓▓░░                                                                                         
          ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓            2 - %s                           
            ▓▓░░░░░░░░░░░░░░▓▓                                                                                     
              ▓▓▓▓░░░░░░▓▓▓▓                3 - %s                           
                  ▓▓▓▓▓▓        ░░                                                                             
                ▓▓▓▓▓▓▓▓▓▓      ▓▓          4 - %s                          
                ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                                                                               
               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            Prêmio total caso pare: R$ %.2f              
               ▓▓▓▓░░▓▓░░▓▓▓▓               Prêmio total caso erre: R$ %.2f                  
                                                    
                                        =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                ''' % (contador + 1, pergunta_premio[contador_premio], pergunta, resposta1[ale],
                resposta2[ale], resposta3[ale], resposta4[ale], premio_parar[contador], premio_errar[contador]))
                try:
                    ajuda = int(input('''       
                                                ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                | Insira:              Disponíveis:   |
                                                | 1- Universitários    %d              |
                                                | 2- Cartas            %d              |
                                                | 3- Placas            %d              |
                                                | 4- Pulos             %d              |
                                                |                                     |
                                                | 5 - Voltar                          |
                                                ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                    
                                                > ''' % (qtde_ajudas[0], qtde_ajudas[1], qtde_ajudas[2], qtde_ajudas[3])))
                except:
                    os.system('cls') or None
                    print('''                 
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                       |  ERRO! Não foi inserido um número inteiro!! |
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                        \/           
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓                                      
''')
                    time.sleep(3)
                    contador2 = 1
                    
                if (ajuda < 1 or ajuda > 5):
                    os.system('cls') or None
                    print('''                 
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                       |            Ei! Resposta Inválida!          |
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                        \/           
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
                    time.sleep(3)
                    
            if (ajuda == 5):
                contador2 = 1
            if (ajuda == 1):
                ajuda -= 1
                os.system('cls') or None
                if (qtde_ajudas[ajuda] < 1):
                    print('''                 
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                       | Você não tem mais ajuda do universitários! |
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                        \/           
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓                                    
''')
                    time.sleep(3)
                    contador2 += 1  
                else:
                    uni = random.randint(1,4)
                    while (uni == correta[ale]):
                        uni = random.randint(1,4)
                    uni2 = random.randint(1,4)
                    while (uni2 == correta[ale] or uni2 == uni):
                        uni2 = random.randint(1,3)
                    print('''
                                        =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                        
                ▓▓▓▓▓▓▓▓▓▓                  Rodada: %d                              
              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                Pergunta valendo R$ %.2f                     
            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                                                    
          ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓            > %s         
      ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                                                                           
      ░░░░▓▓░░██  ░░░░░░██  ░░▓▓░░░░        1 - %s                                                                           
        ░░▓▓░░████░░░░░░████░░▓▓░░                                                                                         
          ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓            2 - %s                           
            ▓▓░░░░░░░░░░░░░░▓▓                                                                                     
              ▓▓▓▓░░░░░░▓▓▓▓                3 - %s                           
                  ▓▓▓▓▓▓        ░░                                                                             
                ▓▓▓▓▓▓▓▓▓▓      ▓▓          4 - %s                          
                ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                                                                               
               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            Prêmio total caso pare: R$ %.2f              
               ▓▓▓▓░░▓▓░░▓▓▓▓               Prêmio total caso erre: R$ %.2f                  
                                                    
                                        =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                ''' % (contador + 1, pergunta_premio[contador_premio], pergunta, resposta1[ale],
                    resposta2[ale], resposta3[ale], resposta4[ale], premio_parar[contador], premio_errar[contador]))
                    
                    print('''
                                                Armando disse: "Tenho certeza que a resposta correta é a %d!"
                                                
                                                Thomas disse: "Acho que a resposta correta é a %d"''' % (uni, correta[ale]))
                    print('''               
                                                Luiza disse: "Estou em dúvida entre a %d e a %d''' % (uni2, correta[ale]))
                    time.sleep(6)
                    input('''
                                                    ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                     |      Para continuar, pressione enter.     |
                                                    ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                    ''')
                    contador2 += 1
                    qtde_ajudas[ajuda] -= 1
                    
            if (ajuda == 2):
                ajuda -= 1
                os.system('cls') or None
                if (qtde_ajudas[ajuda] < 1):
                    print('''                 
                                           ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                            |      Não há mais cartas disponíveis!      |
                                           ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                        \/           
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
                    time.sleep(3)
                    contador2 += 1
                else:
                    cards = 5
                    while (cards < 1 or cards > 4):
                        os.system('cls') or None
                        try:
                            cards = int(input('''
                                            ┌─────────┐┌─────────┐┌─────────┐┌─────────┐
                                            │♥        ││♥        ││♥        ││♥        │
                                            │         ││         ││         ││         │
                                            │         ││         ││         ││         │
                                            │    1    ││    2    ││    3    ││    4    │
                                            │         ││         ││         ││         │
                                            │         ││         ││         ││         │
                                            │        ♥││        ♥││        ♥││        ♥│
                                            └─────────┘└─────────┘└─────────┘└─────────┘
                                
                                                      Escolha uma carta: '''))
                            random_valor = random.randint(1,4)
                            qtde_ajudas[ajuda] -= 1
                        except:
                            os.system('cls') or None
                            print('''                 
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                       |  ERRO! Não foi inserido um número inteiro!! |
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                        \/           
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓                                      
''')
                            time.sleep(3)
                            contador2 = 1
                            random_valor = 0
                            qtde_ajudas[ajuda] = 1
                            
                        if (cards < 1 or cards > 4):
                            os.system('cls') or None
                            print('''                 
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                       |            Ei! Resposta Inválida!          |
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
                            time.sleep(3)
                    
                    os.system('cls') or None
                    if (random_valor == 1):
                            print('''                 
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                       |                Tirou Rei!                 |
                                       |     Nenhuma alternativa foi eliminada!    |
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                        \/           
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓                                      
''')
                    if (random_valor == 2):
                        print('''                 
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                       |                Tirou Ás!                  |
                                       |       Uma alternativa foi eliminada!      |
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                        \/           
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
                        
                        carta = random.randint(1,4)
                        while (carta == correta[ale]):
                            carta = random.randint(1,4)
                            
                        if (carta == 1 and resposta1[ale] != gabarito[ale]):
                            resposta1[ale] = 'ELIMINADA!'
                        if (carta == 2 and resposta2[ale] != gabarito[ale]):
                            resposta2[ale] = 'ELIMINADA!'
                        if (carta == 3 and resposta3[ale] != gabarito[ale]):
                            resposta3[ale] = 'ELIMINADA!'
                        if (carta == 4 and resposta4[ale] != gabarito[ale]):
                            resposta4[ale] = 'ELIMINADA!'
                                
                    if (random_valor == 3):
                        print('''                 
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                       |                Tirou Dois!                |
                                       |     Duas alternativas foram eliminadas!   |
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
                        
                        carta = random.randint(1,4)
                        while (carta == correta[ale]):
                            carta = random.randint(1,4)
                            
                        carta_2 = random.randint(1,4)
                        while (carta == carta_2 or carta_2 == correta[ale]):
                            carta_2 = random.randint(1,4)
                            
                        if (carta == 1 and resposta1[ale] != gabarito[ale] or carta_2 == 1 and resposta1[ale] != gabarito[ale]):
                            resposta1[ale] = 'ELIMINADA!'
                        if (carta == 2 and resposta2[ale] != gabarito[ale] or carta_2 == 2 and resposta2[ale] != gabarito[ale]):
                            resposta2[ale] = 'ELIMINADA!'
                        if (carta == 3 and resposta3[ale] != gabarito[ale] or carta_2 == 3 and resposta3[ale] != gabarito[ale]):
                            resposta3[ale] = 'ELIMINADA!'
                        if (carta == 4 and resposta4[ale] != gabarito[ale] or carta_2 == 4 and resposta4[ale] != gabarito[ale]):
                            resposta4[ale] = 'ELIMINADA!'   
                            
                    if (random_valor == 4):
                        print('''                 
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                       |                Tirou Três!                |
                                       |     Três alternativas foram eliminadas!   |
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
                        if (resposta1[ale] != gabarito[ale]):
                            resposta1[ale] = 'ELIMINADA!'
                        if (resposta2[ale] != gabarito[ale]):
                            resposta2[ale] = 'ELIMINADA!'
                        if (resposta3[ale] != gabarito[ale]):
                            resposta3[ale] = 'ELIMINADA!'
                        if (resposta4[ale] != gabarito[ale]):
                            resposta4[ale] = 'ELIMINADA!'
                    time.sleep(4)
                    contador2 += 1
                    
            if (ajuda == 3):
                ajuda -= 1
                os.system('cls') or None
                if (qtde_ajudas[ajuda] < 1):
                    print('''                 
                                          ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                           |      Não há mais placas disponíveis!      |
                                          ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
                    time.sleep(3)
                    contador2 += 1
                else:
                    if (resposta1[ale] == gabarito[ale]):
                        placas1 = random.randint(40, 60)
                    else:
                        placas1 = random.randint(20, 45)
                    
                    if (resposta2[ale] == gabarito[ale]):
                        placas2 = random.randint(40, 60)
                    else:
                        placas2 = random.randint(20, 45)
                    
                    if (resposta3[ale] == gabarito[ale]):
                        placas3 = random.randint(40, 60)
                    else:
                        placas3 = random.randint(20, 45)
                    
                    if (resposta4[ale] == gabarito[ale]):
                        placas4 = random.randint(40, 60)
                    else:
                        placas4 = random.randint(30, 45)
                    
                    total_plateia = placas1 + placas2 + placas3 + placas4
                    print('''
                                        =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                        
                ▓▓▓▓▓▓▓▓▓▓                  Rodada: %d                              
              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                Pergunta valendo R$ %.2f                     
            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                                                    
          ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓            > %s         
      ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                                                                           
      ░░░░▓▓░░██  ░░░░░░██  ░░▓▓░░░░        1 - %s                                                                           
        ░░▓▓░░████░░░░░░████░░▓▓░░                                                                                         
          ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓            2 - %s                           
            ▓▓░░░░░░░░░░░░░░▓▓                                                                                     
              ▓▓▓▓░░░░░░▓▓▓▓                3 - %s                           
                  ▓▓▓▓▓▓        ░░                                                                             
                ▓▓▓▓▓▓▓▓▓▓      ▓▓          4 - %s                          
                ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                                                                               
               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            Prêmio total caso pare: R$ %.2f              
               ▓▓▓▓░░▓▓░░▓▓▓▓               Prêmio total caso erre: R$ %.2f                  
                                                    
                                        =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                    ''' % (contador + 1, pergunta_premio[contador_premio], pergunta, resposta1[ale],
                    resposta2[ale], resposta3[ale], resposta4[ale], premio_parar[contador], premio_errar[contador]))
                    print('''
                                            =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                            | Na platéia:                              |
                                            | %d pessoas disseram que a 1 é a correta  |
                                            | %d pessoas disseram que a 2 é a correta  |
                                            | %d pessoas disseram que a 3 é a correta  |
                                            | %d pessoas disseram que a 4 é a correta  |
                                            =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                            Pessoas presentes na platéia hoje: %d''' % (placas1, placas2, placas3, placas4, total_plateia))
                    time.sleep(6)
                    input('''
                                            ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                            |      Para continuar, pressione enter.      |
                                            ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=''')
                    contador2 += 1
                    qtde_ajudas[ajuda] -= 1
                    
            if (ajuda == 4):
                ajuda -= 1
                os.system('cls') or None
                if (qtde_ajudas[ajuda] < 1):
                    print('''                 
                                          ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                           |       Não há mais pulos disponíveis!      |
                                          ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
                    contador2 = 1
                    time.sleep(3)
                else:
                    contador2 = 0
                    qtde_ajudas[ajuda] -= 1
                    
    if (acao == 1):
        try:
            lixo = int(input('''
                                        Resposta: '''))
        except:
            os.system('cls') or None
            print('''                 
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                       |  ERRO! Não foi inserido um número inteiro!! |
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓                                      
''')
            time.sleep(3)
            contador2 = 1
            contador3 = 1
            resp = 300
        
        try:
            if (contador3 == 0):
                resp = int(input('''
                                        Por sua conta e risco, resposta final: '''))
        except:
            if (contador3 == 0):
                os.system('cls') or None
                print('''                 
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                       |  ERRO! Não foi inserido um número inteiro!! |
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓                                      
''')
                time.sleep(3)
                contador2 = 1
                contador3 = 1
                resp = 300

        while (resp < 1 and contador3 == 0 or resp > 4 and contador3 == 0):
            resp = int(input('''
                                        Essa alternativa não existe! Insira outra: '''))
        if (resp != correta[ale] and contador3 == 0):
            os.system('cls') or None
            print('''
                                            ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                             |           E sua resposta está...          |
                                            ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
            time.sleep(2)
            os.system('cls') or None
            print('''
                                            ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                             |                  Errada!                  |
                                            ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
            time.sleep(2)
            os.system('cls') or None
            input('''
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                             Você perdeu! :(              
                                                               Rodada: %d                 
                                                    Resposta correta: %d (%s)      
                                                              Ganhos: R$%.2f               
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                        
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                         |      Para fechar o jogo, pressione enter.      |
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                        \/           
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''' % (contador + 1, correta[ale], gabarito[ale],premio_errar[contador]))
            contador = 17
            
        if (resp == correta[ale] and contador3 == 0):
            os.system('cls') or None
            print('''
                                           ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                            |           E sua resposta está...          |
                                           ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
            time.sleep(2)
            os.system('cls') or None
            print('''
                                          ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                            |                 Correta!                 |
                                          ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
            time.sleep(2)
            contador += 1
            contador2 = 0
    if (acao == 3):
        os.system('cls') or None
        input('''
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                        Você escolheu parar!              
                                                            Rodada: %d                 
                                                    Resposta correta: %d (%s)      
                                                           Ganhos: R$%.2f               
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                        
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                         |       Para fechar o jogo, pressione enter.     |
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''' % (contador + 1, correta[ale], gabarito[ale],premio_parar[contador]))
        contador = 17

nivel4 = [
        'Ham, o chimpanzé, foi o primeiro macaco a ir para o espaço no ano de: ',
        'Cobby, o chimpanzé macho mais velho dos Estados Unidos morreu com:',
        'Sabia-se que o outro vírus que afeta os humanos, o HIV-2, se encontrava em um:'
        ]
resposta_milhao1 = [
                    '31 de Janeiro de 1961',
                    '60',
                    'Chimpanzé'
                  ]
resposta_milhao2 = [
                    '31 de Janeiro de 1964',
                    '61',
                    'Babuíno'
                  ]
resposta_milhao3 = [
                    '31 de Janeiro de 1970',
                    '62',
                    'Mangabei'
                  ]
resposta_milhao4 = [
                    '31 de Janeiro de 1974',
                    '63',
                    'Maximus mamalias',
                  ]
gab4 = [
        '31 de Janeiro de 1961',
        '63',
        'Mangabei'
       ]
gab41 = [
            1,
            4,
            3,
        ]
cont_milhao = 0
        
if (contador == 15):
    os.system('cls') or None
    print('''
                                    =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                     | Parabéns, você chegou até a pergunta do milhão! |
                                    =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                        \/      
                                                           ▓▓▓▓▓▓▓▓▓▓                        
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░██  ░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
    ''')
    time.sleep(4)
    os.system('cls') or None
    print('''
                                    =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                     |             Você pode escolher entre:           |
                                    =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=                                  
                                                        \/       
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░  ██░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
    ''')
    time.sleep(2)
    os.system('cls') or None
    print('''
                                  ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                   | Responder ela, correndo o risco de perder TUDO caso erre |
                                  =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~                                         
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░██  ░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
    ''')
    time.sleep(4)
    os.system('cls') or None
    print('''
                                  ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                   |      Ou parar agora, levando R$500.000,00 para casa!     |
                                  =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░  ██░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
    ''')
    time.sleep(4)
    os.system('cls') or None
    print('''
                                  ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                   |        Lembre-se, não será possível usar ajudas!!!       |
                                  =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
    ''')
    time.sleep(4)
    resp = 5
    while (resp != 1 and resp != 2):
        os.system('cls') or None
        try:
            resp = int(input('''
                                                           ~=~=~=~=~=~=~=~=~=
                                                            | Você deseja: |
                                                           =~=~=~=~=~=~=~=~=~
                                                        
                                                           ~=~=~=~=~=~=~=~=~=
                                                            |1 - Continuar!|
                                                           =~=~=~=~=~=~=~=~=~
                                                           ~=~=~=~=~=~=~=~=~=
                                                            |  2- Parar!   |
                                                           =~=~=~=~=~=~=~=~=~
                                                           
                                                           > '''))
        except:
            os.system('cls') or None
            print('''                 
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                       |  ERRO! Não foi inserido um número inteiro!!|
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
            time.sleep(3)
    if (resp == 2):
        os.system('cls') or None
        input('''
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                        Você escolheu parar!              
                                                             Rodada: 15                 
                                                        Ganhos: R$500.000,00           
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                        
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                         |       Para fechar o jogo, pressione enter.     |
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                        \/           
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
    cont_milhao = 0
    if (resp == 1):
        final = 5
        while (final != 1 and final != 2 and final != 3 and final != 4):  
          os.system('cls') or None
          if (cont_milhao == 0):
              ale_milhao = random.randint(0, 2)
              cont_milhao = 1
          try:    
            final = int(input('''
                                          =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                          
                  ▓▓▓▓▓▓▓▓▓▓                  Rodada: 16                              
                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                Pergunta valendo R$ 1.000.000,00                   
              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                                                    
            ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓            > %s         
        ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                                                                           
        ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░        1 - %s                                                                           
          ░░▓▓░░████░░░░░░████░░▓▓░░                                                                                         
            ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓            2 - %s                           
              ▓▓░░░░░░░░░░░░░░▓▓                                                                                     
                ▓▓▓▓░░░░░░▓▓▓▓                3 - %s                           
                    ▓▓▓▓▓▓        ░░                                                                             
                  ▓▓▓▓▓▓▓▓▓▓      ▓▓          4 - %s                          
                  ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                                                                               
                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                         
                ▓▓▓▓░░▓▓░░▓▓▓▓               Prêmio total caso erre: R$ 0,00!            
                                                      
                                          =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                          
                                            > ''' % (nivel4[ale_milhao], resposta_milhao1[ale_milhao], resposta_milhao2[ale_milhao],
                                                    resposta_milhao3[ale_milhao], resposta_milhao4[ale_milhao])))
          except:
            os.system('cls') or None
            print('''                 
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                        |  ERRO! Não foi inserido um número inteiro!!|
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                          \/            
                                                            ▓▓▓▓▓▓▓▓▓▓                          
                                                          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                      ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                  ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                  ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                    ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                      ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                        ▓▓░░░░░░░░░░░░░░▓▓                      
                                                          ▓▓▓▓░░░░░░▓▓▓▓                        
                                                              ▓▓▓▓▓▓        ░░                  
                                                            ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                            ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                          ▓▓▓▓░░▓▓░░▓▓▓▓
          ''')
            time.sleep(3)
        if (final != 1 and final != 2 and final != 3 and final != 4):  
          os.system('cls') or None
          print('''                 
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                       |            Ei! Resposta Inválida!          |
                                      ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                        \/           
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
          time.sleep(3)
        if (final != gab41[ale_milhao]):
            os.system('cls') or None
            print('''
                                            ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                             |           E sua resposta está...          |
                                            ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
            time.sleep(3)
            os.system('cls') or None
            print('''
                                            ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                             |                  Errada!                  |
                                            ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
            time.sleep(3)
            os.system('cls') or None
            print('''
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                            Você perdeu! :(              
                                                              Rodada: 16                 
                                              Resposta correta: %d (%s)   
                                                            Ganhos: R$0,00!        
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
            ''' % (gab41[ale_milhao], gab4[ale_milhao]))
            time.sleep(3)
            input('''
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                         |      Para fechar o jogo, pressione enter.      |
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')

        else:
            os.system('cls') or None
            print('''
                                            ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                             |           E sua resposta está...          |
                                            ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓                                            
''')
            time.sleep(3)
            os.system('cls') or None
            print('''
                                            ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                             |                  Correta!                 |
                                            ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')
            time.sleep(3)
            os.system('cls') or None
            input('''
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                           Você Ganhou!! :)              
                                                              Rodada: 16                      
                                                        Ganhos: R$1.000.000,00        
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                        
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                         |      Para fechar o jogo, pressione enter.      |
                                        ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
                                                        \/            
                                                           ▓▓▓▓▓▓▓▓▓▓                          
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                                                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                      
                                                     ▓▓▓▓░░░░░░▓▓░░░░░░▓▓▓▓                    
                                                 ░░░░▓▓░░░░░░░░░░░░░░░░░░▓▓░░░░                
                                                 ░░░░▓▓░░██  ░░░░░░  ██░░▓▓░░░░                
                                                   ░░▓▓░░████░░░░░░████░░▓▓░░                  
                                                     ▓▓░░▒▒▒▒░░░░░░▒▒▒▒░░▓▓                    
                                                       ▓▓░░░░░░░░░░░░░░▓▓                      
                                                         ▓▓▓▓░░░░░░▓▓▓▓                        
                                                             ▓▓▓▓▓▓        ░░                  
                                                           ▓▓▓▓▓▓▓▓▓▓      ▓▓                  
                                                           ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓                  
                                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    
                                                         ▓▓▓▓░░▓▓░░▓▓▓▓
''')