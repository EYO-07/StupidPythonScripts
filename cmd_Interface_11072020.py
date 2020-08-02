#!/usr/bin/env python
# -*- coding: utf-8 -*-

project_dr = "E:\\mdr\\pdr\\python_cmd_Interface_07072020\\" # Mude isso caso mude o local do diretorio

# -------------------------------------------------------------------------------------------------------
# TEORIA : Descricao da Teoria Auxiliar para o Projeto
# -------------------------------------------------------------------------------------------------------
# [ Interface ] : E um objeto capaz de salvar e carregar um arquivo de configuracoes
# 
# [ Trialetica de (Header Object, Main Object, Oriented Object) ] : 
#   1 - Header Object : E um objeto Interface que observa um oriented object
#   2 - Oriented Object : E um objeto interface que forma uma rede entre outros objetos de mesma classe
#       , ele forma um espaco para que o header possa navegar.
#   3 - Main Object : E um objeto Interface que pega interpreta junto com o loop main as diferentes 
#       diferentes mensagens entre o Header Object e o Oriented Object
#
# [ Orientede Interface ] : Eh uma interface que armazena referencias de outras interfaces, formando
#       uma rede de Orientede Objects capaz de ser navegada por header object.
# 
# 
# 
# -------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------
# GLOBAL VARS
# -------------------------------------------------------------------------------------------------------

# Imports 
import os, ast
import keyboard as kbd
import win32gui as w32
from datetime import date
from random import randint
from colorama import init
from colors import red, green, blue, color, yellow, white, cyan
from time import time

init() # ~ colorama

# Variables [ Pomodoro and RPG status ]
POMO_MIN_SEC = 45*60 # 60*45
POMO_MIN_SEC_desc = '(45 min)'
HP = 30
MP = 50

# Variables [ Debug ]
flag = red("RED FLAG")

# Variables [ Messages and Strings ]
LINE_str = "-----------------------------------------------------------------------------"
PROG_NAME_str = "\n Programa [ Interface de Comandos em Python ] : { 10072020 : Version 0 }"
PROG_DESC_str = "    Interface de Comandos em Python"

COM_str0 = """
[ Interface de Comandos em Python ] : 

    1 - [ Comando ] : Os comandos sao strings da forma @COMANDO
    2 - [ Interface ] : Interface eh o objeto que executa os comandos,
        de acordo com a interface os comandos sao interpretados de 
        maneira diferente
    3 - [ Interface Principal ] : Eh a interface inicial, digite 
        @network para mostrar as interfaces associadas

Comandos [ Gerais ] :
    
    @help : Digite @help para mostrar os comandos e opcoes de navegacao
    
    @listdir : lista os arquivos no diretorio da interface
    
    @exit : Digite @exit para sair da interface salvando os arquivos de 
        configuracao ou para voltar para interface principal   
    @save : Digite para salvar arquivos, se comporta de acordo com a 
        interface selecionada
    @load : Se existe arquivosave definido entao carrega o arquivo
    """

COM_NAV_geral = """
        Comandos [ de Navegacao ] :
        
1 -         @origem : Retorna para Interface de Origem
2 -         @network : Mostra as opcoes de Interfaces
3 -         @goto : Mostra as opcoes de Interface
4 -         @goto NOME : Vai para uma interface cujo nome e NOME
"""

COM_TEXT_str = """
        Comandos [ de Interface de Manipulacao de Texto ] :
        
1 -         @origem : Retorna para Origem
2 -         @network : Mostra as opcoes da rede de Navegacao de Interfaces
3 -         @content : mostra o conteudo do arquivo de texto selecionado
4 -         @goto NOME : Vai para uma interface cujo nome e NOME           
5 -         @create NOME.txt : cria um arquivo de texto
6 -         @editor : Abre o editor externo padrao para arquivos de texto
7 -         @load : Mostra uma lista de nomes de arquivos na pasta corrente
8 -         @load NOME : Abre o arquivo NOME
9 -         @load= : Mostra uma lista numerada dos arquivos na pasta corrente
10 -        @load=NUMERO : Abre o arquivo correspondente ao numero
11 -        @select NOME: Apenas muda o nome do arquivo texto, 
                nao muda o conteudo, requer @load para carregar
            """

# Variables [ Directories and Path ]
dir_origem = os.getcwd()
os.chdir(project_dr)
listDir = os.listdir()

# Functions [ Auxiliary Functions ]
def try_pass(F,ARGS,message_bool=False, message='erro'):
    """ try pass function :
    F : Function possibly raising error
    ARGS : Tuple of Arguments of FINALIZADO
    message : Display warning message if catch a error
    """
    try:
        return F(*ARGS)
    except:
        if message_bool: 
            input( message )
            return None
            
def None_D(X):
    if X==None:
        return {}
    else : 
        return X
        
def None_S(X):
    if X==None:
        return ''
    else:
        return X

def progress_bar(number, max_number=10):
    len_L = len(LINE_str) - 4
    FULL = int( number*len_L/max_number )
    EMPTY = len_L - FULL
    STRING = '\n[ '+FULL*'#'+EMPTY*'-'+' ]'
    return STRING
    
def status(number, max_number=10, desc='', color_func=red):
    len_L = len(LINE_str) - 4
    FULL = int( number*len_L/max_number )
    EMPTY = len_L - FULL
    STRING = color_func(' '+desc+' :\n'+'[ '+FULL*'#')+color_func(EMPTY*'-')+color_func(' ]')
    return STRING + white('\n') #+white('\n')
    
def count_ast(string):
    ast = 0
    L = len(string)
    count = 0
    while ast<L:
        if string[ast]=='*':
            ast = ast + 1
        count = count + 1
        if ast!=count: break
    return ast

def print_dict(obj):
    print()
    for key in obj.keys():
        print( 3*' ',key, ':', try_substr( str( obj[key] ),0,30) )
    print()

def teste():
    print(flag, ': Para ser usado no comando @teste do HeadInterface')

def try_substr(string,a,b):
    try   : 
        if   b=='all': return string[a:]
        elif a=='all': return string[:b]
        else         : return string[a:b]
    except: return None

# -------------------------------------------------------------------------------------------------------
# CLASSES ABSTRATAS PRINCIPAIS
# -------------------------------------------------------------------------------------------------------

class Interface(object): # PROIBIDO MODIFICAR 06072020
    """ Classe Generica de Interface de Leitura e Escrita em Dicionarios """
    def __init__(self,filename=None,main_obj=None):
        self.states = {'filename':filename, 'auto interface info':True}
        self.desc = ''
    
    # Interface > Funcoes > Auxiliar
    def __flag(self): # Debug : Mostra a Localizacao do Erro
        print( yellow('Classe : Interface') )
        print( print_dict(self.states) )
        print( self.desc )
    def print_dict(self):
        print()
        obj = self.states
        for key in obj.keys():
            print( 3*' ',key, ':', str( obj[key] ) )
        print()
    def help_c(self):
        print(white(LINE_str))
        print(yellow(COM_str0))
    def short_desc(self):
        return yellow(self.desc)
    def write_str(self,filename,obj):
        fhandle = open(filename,'w')
        fhandle.write( str(obj) )
        fhandle.close()
    def try_saveBy_name(self,write,filename,state_name):
        if filename=='': # filename nao especificado no comando
            try:
                write(self.states[state_name],self.states)
            except: # input the filename
                try:
                    self.states[state_name] = input('Nome do Arquivo : ')
                    write(self.states[state_name],self.states)
                except:
                    print( red('Nao Foi Possivel Salvar o Arquivo') )
                    self.__flag()
        else: # filename especificado
            try:
                self.states[state_name]=filename
                write(self.states[state_name],self.states)
            except:
                print( red('Nao Foi Possivel Salvar o Arquivo') )
                self.__flag()
    def read_lit(self,filename):
        file_obj = open(filename,'r')
        RET = ast.literal_eval( file_obj.read() )
        file_obj.close()
        return RET
    def try_loadBy_name(self, filename):
        import ast
        try:
            return self.read_lit(filename)
        except:
            print('Nao Foi Possivel Carregar o Arquivo')
            self.__flag()
    
    # Interface > Funcoes > Principais        
    def save( self, string='' ):
        self.try_saveBy_name( 
            write = self.write_str, 
            filename = string,
            state_name = 'filename'
            )
    def load(self):
        self.states.update( self.try_loadBy_name(
            filename = self.states['filename']
            ) )
    
    # Interface > Funcoes > Principais > Comandos
    def commands(self,input_str,main_obj):
        # print(try_substr(input_str,'all',5))
        if input_str=='@exit':
            #if main_obj==self:
            return True
        elif input_str=='@help':
            self.help_c()
            return False
        elif input_str=='@jump':
            print(50*'\n')
            return False
        elif try_substr(input_str,0,5)=='@save':
            filename = try_substr(input_str,6,'all')
            self.save(filename)
            return False
        elif try_substr(input_str,0,5)=='@load':
            self.load()
            return False
        elif input_str == '@interface info':
            print(self.states)
            return False
        elif input_str == '@listdir':
            print()
            for k in os.listdir():
                print( green( k ) )
            print()
            return False
        else:
            return False

class VerticalOrientedInterface(Interface): # PROIBIDO MODIFICAR 06072020
    """ Interface Orientada : possui referencias de Outras Interfaces podendo ser utilizado para navegar entre interfaces
        
        1 - Temos a Interface de Origem que e a Interface de Retorno
        2 - Temos uma opcao de subinterface inicialmente vazia para poder permitir a criacao de subinterfaces
        3 - E uma classe abstrata, serve para organizar as classes operacionais
    
    """
    def __init__(self,filename=None,dad_ref=None,main_obj=None):
        Interface.__init__(self,filename,main_obj)
        self.network = { 'Interface de Origem' : dad_ref }
        self.listdir = os.listdir() #listDir
        self.states.update( {'return?':False} )
        
    # VerticalOrientedInterface > Comandos > Auxiliares
    
    # callbacks de input de keyboard
    def up_callback(self,head,X):
        if w32.GetWindowText( w32.GetForegroundWindow() )=='C:\Python\Python38\python.exe': 
            kbd.press('enter')
    def down_callback(self,head,X):
        if w32.GetWindowText( w32.GetForegroundWindow() )=='C:\Python\Python38\python.exe': 
            kbd.press('enter')
    def left_callback(self,head,X):
        head.head = self.network['Interface de Origem']
        if w32.GetWindowText( w32.GetForegroundWindow() )=='C:\Python\Python38\python.exe': 
            kbd.press('enter')
    def right_callback(self,head,X):
        if w32.GetWindowText( w32.GetForegroundWindow() )=='C:\Python\Python38\python.exe': 
            kbd.press('enter')
            
    def __flag(self):
        print( yellow('Classe : VerticalOrientedInterface') )
        print( print_dict(self.states) )
        print( self.desc )
    
    def comm_new_child_interface(self,child_filename):
        """ Cria uma Interface de NAvegacao Filha """
        Child = VerticalOrientedInterface(
            filename = child_filename, 
            dad_ref  = self
            )
        self.network.update( { child_filename : Child } )
    def comm_del_child_interface(self,child_filename):
        try:
            var = self.network[child_filename]
            self.network[child_filename] = None
            del var
            self.network.pop(child_filename)
            print('Objeto Deletado')
        except:
            print('Objeto Nao Existe')
            self.__flag()
    def comm_show_network(self):
        print( '\n'+green( '[ Network ] :') )
        for key in self.network.keys():
            print(2*' ',green(key) )
        print()
        
    # VerticalOrientedInterface > Comandos > Principal
    def rpg_status_update(self,main_obj):
        pass
    def commands(self,input_str,main_obj):
        # print(try_substr(input_str,'all',5))
        if input_str=='@exit':
            if self.desc=='INTERFACE PRINCIPAL':
                return True
            else:
                self.states.update( { 'return?':True } )
                return False
        elif input_str=='@help':
            self.help_c()
            print(green(COM_NAV_geral))
            return False
        elif input_str=='@jump':
            print(50*'\n')
            return False
        elif try_substr(input_str,0,5)=='@save':
            filename = try_substr(input_str,6,'all')
            self.save(filename)
            return False
        elif try_substr(input_str,0,5)=='@load':
            self.load()
            return False
        elif try_substr(input_str,0,len('@child interface') ) == '@child interface':
            self.comm_new_child_interface( try_substr(input_str,len('@child interface')+1, 'all' ) )
            return False
        elif try_substr(input_str,0,len('@del child interface') ) == '@del child interface':
            self.comm_del_child_interface( try_substr(input_str,len('@del child interface')+1, 'all' ) )
            return False
        elif input_str=='@network':
            self.comm_show_network()
        elif input_str == '@interface info':
            print(self.states)
            return False
        else:
            return Interface.commands(self,input_str,main_obj)

class HeadInterface(Interface): # PROIBIDO MODIFICAR 06072020
    """ E uma interface que observa uma interface orientada, e usada pela funcao main para interpretar os comandos
        
        1 - Tem o comando para mudar sua posicao para uma interface dentro da interface de navegacao
    """
    def __init__(self,filename, oriented_interface,main_obj=None):
        Interface.__init__(self,filename,main_obj)
        self.head = oriented_interface
    def __flag(self):
        print( yellow('Classe : HeadInterface') )
        print( print_dict(self.states) )
        print( self.desc )
    def commands(self,input_str,main_obj):
        if input_str == '@origem':
            save_head = self.head
            self.head = self.head.network['Interface de Origem']
        elif try_substr(input_str,0,len('@goto') ) == '@goto':
            try:
                self.head = self.head.network[ try_substr(input_str,len('@goto')+1, 'all' ) ]
            except:
                self.head.comm_show_network()
            return False
        elif input_str == '@teste':
            try:
                teste()
            except:
                print(red('ERRO') )
            return False
        else:
            return self.head.commands(input_str,main_obj)
        
# -------------------------------------------------------------------------------------------------------
# CLASSES de APLICACAO
# -------------------------------------------------------------------------------------------------------         

class TextInterface(VerticalOrientedInterface): # PROIBIDO MODIFICAR 07072020
    """ Tem um arquivo de texto que pode ser lido e manipulado, alem do arquivo de estados """
    def __init__(self,filename,dad_ref,main_obj,txt_dir=project_dr):
        VerticalOrientedInterface.__init__(self,filename,dad_ref,main_obj)
        self.desc = 'TEXT INTERFACE'
        self.states.update( { 'content': """ ... """, 'exist text filename': False }  )
        self.txt_dir = txt_dir
        
        #os.chdir(dir)
        #self.states['auto interface info']=False
    
    # TextInterface > Funcoes
    #def print_dict(self):
    #    print()
    #    obj = self.states
    #    for key in obj.keys():
    #        if key !='content':
    #            print( 3*' ',key, ':', str( obj[key] ) )
    #        else:
    #            print( 3*' ', key, ':' , obj['exist text filename'] )
    #    print()
    def print_dict(self):
        print()
        print( 'Arquivo de Estados da Interface : ' , self.states['filename'] )
        print( 'conteudo : ' , self.states['exist text filename'] )
        try:
            print( 'Arquivo do Texto Selecionado : ', self.states['text filename'] )
        except:
            print(red('Selecione um Arquivo de Texto com @load ou @load=') )
        print()    
    def comm_select_filename(self,filename):
        self.states.update( { 'exist text filename': True, 'text filename':filename } )
        
    def comm_extern_editor(self):
        import sys, os
        #print( main_obj.states['default text editor'] +' '+self.states['text filename'] )
        # self.states['Interface de Origem'].states['default text editor'] +' '+
        # print( self.network['Interface de Origem'] ) 
        os.system( self.network['Interface de Origem'].states['default text editor'] +' '+ self.states['text filename'] )
        
    def show_content(self):
        print(white('\n [ CONTEUDO ] : { ') + red('Conteudo do Arquivo de Texto') + white(' }') )
        print(white(LINE_str))
        print(green( self.states['content'] ))
        print()
    def comm_create_text_file(self,filename):
        os.chdir(self.txt_dir)
        self.states.update( { 'text filename':filename, 'exist text filename': True } )
        fhandle = open(filename,'w')
        fhandle.write( self.states['content'] )
        fhandle.close()
        self.comm_load_text_file( filename )
        os.chdir(project_dr)
        #print(filename)
    def save(self):
        os.chdir(self.txt_dir)
        if self.states['exist text filename']:
            fhandle = open( self.states['text filename'] ,'w')
            fhandle.write( self.states['content'] )
            fhandle.close()
        os.chdir(project_dr)
    def comm_load_text_file(self,filename):
        os.chdir(self.txt_dir)
        try:
            file_obj = open(filename,'r')
            RET = file_obj.read()
            file_obj.close()
            self.states.update( {'content': RET,'text filename' : filename, 'exist text filename': True } )
        except:
            self.states.update( { 'exist text filename': False } )
            print('Nao Foi Possivel Carregar o Arquivo')
        os.chdir(project_dr)
    # TextInterface > Funcoes > Comandos
    def commands(self, input_str,main_obj):
        if input_str == '@content':
            self.show_content()
            return False
        elif input_str=='@save':
            self.save()
        elif try_substr(input_str,0,len('@create')) == '@create':
            if try_substr( input_str, len('@create')+1,'all' )!='':
                self.comm_create_text_file( try_substr( input_str, len('@create')+1,'all' ) )
                #self.states.update( {'content':' ... '} )
                return False
            else:
                return False
        elif try_substr( input_str, 0,len('@load=') ) == '@load=':
            os.chdir(self.txt_dir)
            for i in range( len( os.listdir() ) ):
                print(i,' : ' ,green( os.listdir()[i] ) )
            print()
            try:
                X = try_substr(input_str, len('@load='), 'all')
                Y = os.listdir()
                self.comm_load_text_file( Y[ int(X) ] )
                os.chdir(project_dr)
                return False
            except:
                print(red( ' Escolha um Numero ') )
                os.chdir(project_dr)
                return False
            os.chdir(project_dr)
        elif try_substr(input_str,0,len('@load')) == '@load':
            os.chdir(self.txt_dir)
            if try_substr( input_str, len('@load')+1,'all' )!='':
                self.comm_load_text_file( try_substr( input_str, len('@load')+1,'all' ) )
            else:
                print()
                for i in os.listdir():
                    print(i)
                print()
                if self.states['exist text filename']:
                    try:
                        self.comm_load_text_file( self.states['text filename'] )
                    except:
                        print(flag)
            os.chdir(project_dr)            
            return False
        elif try_substr(input_str,0,len('@select') ) == '@select':
            os.chdir(self.txt_dir)
            try:
                if try_substr( input_str , len('@select')+1, 'all' )=='':
                    print()
                    for i in os.listdir():
                        print(i)
                    print()
                else:
                    self.comm_select_filename( try_substr( input_str , len('@select')+1, 'all' ) )
                os.chdir(project_dr)    
                return False
            except:
                print('Escreva um Nome Correto')
                os.chdir(project_dr)
                return False
        elif input_str=='@editor':
            os.chdir(self.txt_dir)
            try:
                self.comm_extern_editor()
            except:
                print('Selecione um Arquivo com @select')
            os.chdir(project_dr)    
        elif input_str=='@help':
            self.help_c()
            print(green(COM_TEXT_str))
            return False
        else:
            os.chdir(self.txt_dir)
            X = VerticalOrientedInterface.commands(self,input_str,main_obj)
            os.chdir(project_dr)
            return X

class add_cell_header_TextInterface(TextInterface): # PROIBIDO MODIFICAR 07072020
    def __init__(self,filename, dad_ref,main_obj,txt_dir):
        TextInterface.__init__(self, filename, dad_ref,main_obj,txt_dir)
        self.desc = 'ADD CELL TEXT INTERFACE'
    
    def add_cell_header(self,cell_info):
        #print(self.states['content'])
        X = self.states['content']
        self.states['content'] = X + 2*'\n' + '>>>>> ' + cell_info + '\n' + LINE_str + 3*'\n' + LINE_str
        self.save()
        
    def commands(self,input_str,main_obj):
        #print( try_substr ( input_str,len(input_str)-1,'all') )
        if try_substr ( input_str,len(input_str)-1,'all')=='!':
            self.add_cell_header(try_substr(input_str,0,len(input_str)-1))
            return False
        elif input_str=='@help':
            self.help_c()
            print(green("""
        Comandos [ de Interface de Manipulacao de Texto ] :
            
            1 - Esta interface adiciona informacoes em arquivo de texto
                formatado.
        
        INFORMACAO ! : finalizar um input com ! ira adicionar no arquivo de 
            texto o que estiver escrito antes
        
1 -         @origem : Retorna para Origem
2 -         @network : Mostra as opcoes da rede de Navegacao de Interfaces
3 -         @content : mostra o conteudo do arquivo de texto selecionado
4 -         @goto NOME : Vai para uma interface cujo nome e NOME           
5 -         @create NOME.txt : cria um arquivo de texto
6 -         @editor : Abre o editor externo padrao para .txt
7 -         @load : Mostra uma lista de nomes de arquivos na pasta corrente
8 -         @load NOME : Abre o arquivo NOME
9 -         @load= : Mostra uma lista numerada dos arquivos na pasta corrente
10 -        @load=NUMERO : Abre o arquivo correspondente ao numero
11 -        @select NOME: Apenas muda o nome do arquivo texto, 
                nao muda o conteudo, requer @load          
            """))
        else:
            return TextInterface.commands(self,input_str,main_obj)

class inventoryTextInterface(add_cell_header_TextInterface): # PROIBIDO MODIFICAR 08072020
    """"""
    def __init__(self, filename, dad_ref, main_obj, txt_dir):
        add_cell_header_TextInterface.__init__(self, filename, dad_ref,main_obj,txt_dir)
        self.desc = 'INVENTORY INTERFACE'
        self.states['exist dict'] = False
        self.states['dict'] = {}
        self.title = '# Inventario : { ' + str(date.today()) + ' }'
    def teste(self):
        print(flag,'Este eh o teste')
        print(date.today())
    
    # inventoryTextInterface > funcoes > auxiliares
    def print_dict_info(self):
        D = self.states['dict']
        K = D.keys()
        try:
            print()
            
            for i in K:
                if D[i]<=5:
                    print(i,':',red(D[i]))
                elif D[i]>5 and D[i] <=10:
                    print(i,':',yellow( D[i] ))
                else:
                    print(i, ':', green( D[i] ))
            print()
        except:
            print()
    def add_cell_header(self, cell_info):
        X = self.states['content']
        self.states['content'] = X + '\n' + '' + cell_info # + LINE_str + 3*'\n' + LINE_str
        self.save()           
    def content2dict(self): # calmala
        D = {}
        for i in self.content2list():
            idx = 0 # count_ast(i)
            if try_substr(i,0,1)!='#' and idx<len(i) :
                if idx == 0 :
                    D.update( { i[idx:] : idx } )
                else:
                    D.update( { i[idx+1:] : idx } )
        return D
    def dict2content(self,dictionary):
        self.states['content'] = self.title + '{ ' + self.states['text filename'] + ' }\n'
        X = self.states['content']
        for J in dictionary.keys():
            if dictionary[J]==0:
                X = X +J+'\n' 
            else:
                X = X + dictionary[J]*'*'+' '+J+'\n' 
        self.states['content'] = X
    def content2list(self):
        X = self.states['content']
        X_list = X.split('\n')
        return X_list
    
    # inventoryTextInterface > funcoes > principais
    def save(self): ##
        os.chdir(self.txt_dir)
        
        if self.states['exist text filename'] and self.states['exist dict']:
            self.dict2content( self.states['dict'] )
            fhandle = open( self.states['text filename'] ,'w')
            fhandle.write( self.states['content'] )
            fhandle.close()
            
            
        #Interface.save(self)
        
        os.chdir(project_dr)
    def comm_load_text_file(self,filename):
        os.chdir(self.txt_dir)
        try:
            file_obj = open(filename,'r')
            RET = file_obj.read()
            file_obj.close()
            self.states.update( {'content': RET,'text filename' : filename, 'exist text filename': True } )
        except:
            self.states.update( { 'exist text filename': False } )
            print('Nao Foi Possivel Carregar o Arquivo')
        try:
            self.states['dict'].update( self.content2dict() )
            self.states['exist dict'] = True
            
            # print_dict(self.states) ##
            #print_dict(self.states['dict']) ## 
            self.print_dict_info()
            # print(self.states['dict']) ##
            
        except:
            print(flag,'DEU MERDA')
            self.states['exist dict'] = False
        os.chdir(project_dr)        
        
    # inventoryTextInterface > funcoes > comandos    
    def commands(self, input_str, main_obj):
        if input_str=='@teste':
            try:
                self.teste()
            except:
                print(flag, 'teste errado')
        elif try_substr(input_str,0,len('@create')) == '@create':
            if try_substr( input_str, len('@create')+1,'all' )!='':
                self.comm_create_text_file( try_substr( input_str, len('@create')+1,'all' ) )
                #self.states.update( {'content':' ... '} )
                return False
            else:
                return False
        elif input_str=='@save':
            self.save()
        elif try_substr( input_str, 0,len('@load=') ) == '@load=':
            os.chdir(self.txt_dir)
            for i in range( len( os.listdir() ) ):
                print(i,' : ' ,green( os.listdir()[i] ) )
            print()
            try:
                X = try_substr(input_str, len('@load='), 'all')
                Y = os.listdir()
                self.comm_load_text_file( Y[ int(X) ] )
                os.chdir(project_dr)
                return False
            except:
                print(red( ' Escolha um Numero ') )
                os.chdir(project_dr)
                return False
            os.chdir(project_dr)
        elif try_substr(input_str,0,len('@load')) == '@load':
            os.chdir(self.txt_dir)
            if try_substr( input_str, len('@load')+1,'all' )!='':
                self.comm_load_text_file( try_substr( input_str, len('@load')+1,'all' ) )
            else:
                print()
                for i in os.listdir():
                    print(i)
                print()
                if self.states['exist text filename']:
                    try:
                        self.comm_load_text_file( self.states['text filename'] )
                    except:
                        print(flag)
            os.chdir(project_dr)            
            return False
        elif input_str=='@help':
            self.help_c()
            print(green("""
        Comandos [ de Interface de Manipulacao de Texto ] :
            
            1 - Esta interface adiciona informacoes em arquivo de texto
                formatado.
        
        INFORMACAO ! : finalizar um input com ! ira adicionar no arquivo de 
            texto o que estiver escrito antes
        
1 -         @origem : Retorna para Origem
2 -         @network : Mostra as opcoes da rede de Navegacao de Interfaces
3 -         @content : mostra o conteudo do arquivo de texto selecionado
4 -         @goto NOME : Vai para uma interface cujo nome e NOME           
5 -         @create NOME.txt : cria um arquivo de texto
6 -         @editor : Abre o editor externo padrao para .txt
7 -         @load : Mostra uma lista de nomes de arquivos na pasta corrente
8 -         @load NOME : Abre o arquivo NOME
9 -         @load= : Mostra uma lista numerada dos arquivos na pasta corrente
10 -        @load=NUMERO : Abre o arquivo correspondente ao numero
11 -        @select NOME: Apenas muda o nome do arquivo texto, 
                nao muda o conteudo, requer @load          
            """))    
        else:
            return add_cell_header_TextInterface.commands(self,input_str, main_obj)

class brainWasherInterface(inventoryTextInterface): # PROIBIDO MODIFICAR 09072020
    """"""
    def __init__(self, filename, dad_ref, main_obj, txt_dir):
        inventoryTextInterface.__init__(self, filename, dad_ref,main_obj,txt_dir)
        self.desc = 'BRAINWASHER INTERFACE' #'INVENTORY INFO INTERFACE' 
        self.states['exist dict'] = False
        self.states['dict'] = {}
        self.title = '# Inventario [ de Informacoes ] : { ' + str(date.today()) + ' }'
        self.main_obj = main_obj
    def teste(self):
        print(flag,'Este eh o teste')
        
        print(date.today())
    
    # brainWasherInterface > funcoes > auxiliares
    def rpg_status_update(self,main_obj):
        if POMO_MIN_SEC - main_obj.time_shift <0: # SP BAIXO ~ Comida
            while input('\n\t Seu SP esta baixo, deveria comer alguma coisa ...')!='comi':
                print('\n \t \t Coma algo ! (digite : comi)')
            main_obj.time_shift = 0
            main_obj.time_init = time()
        elif False: # HP BAIXO ~ Heal de MP
            pass
        elif False: # MP BAIXO ~ Comida
            pass
        else:
            main_obj.time_shift = time() - main_obj.time_init
            if POMO_MIN_SEC - main_obj.time_shift>=0:
                print()
                #print( status(10,10,'HP', red) )
                print( status(POMO_MIN_SEC - main_obj.time_shift, POMO_MIN_SEC,'POMODORO '+POMO_MIN_SEC_desc, cyan) )
                #print( status(10,10,'MP',green) )
    def print_dict_info(self):
        D = self.states['dict']
        K = D.keys()
        print()
        for i in K:
            if D[i]<=5:
                print(i,':',red(D[i]))
            elif D[i]>5 and D[i] <=10:
                print(i,':',yellow( D[i] ))
            else:
                print(i, ':', green( D[i] ))
        print()
    def add_cell_header(self, cell_info):
        X = self.states['content']
        self.states['content'] = X + '\n' + '' + cell_info + ' ;' # + LINE_str + 3*'\n' + LINE_str
        self.save()
    def uniform_study(self,repetition_number=50,nivel=20):
        for i in range(repetition_number):
            try:
                self.rpg_status_update(self.main_obj)
            except:
                pass
            print('\nPERGUNTA ['+yellow(' SORTEIO UNIFORME ')+'] :\n'+LINE_str)
            N = self.random_info(nivel)
            if N == None: break
            print( 'MODO [ ' + green('ESTUDO')+' ] : { ', yellow('Nro de Sorteios :'), red(str(repetition_number-i))  ,' }'  )
            print(white(LINE_str))
            INP = input(' [ ? ou G ] >>>>> ')
            os.system('CLS')
            if self.states['dict'][N]!=0:
                if INP == '?':
                    self.states['dict'][N] = self.states['dict'][N] - 1
                elif INP == 'G':
                    self.states['dict'][N] = self.states['dict'][N] + 1
            else:
                if INP == 'G':
                    self.states['dict'][N] = self.states['dict'][N] + 1
            X = self.states['dict']
            
            print()
            
            self.print_dict_info()
            # print_dict(self.states['dict'])
        self.save()
    def random_info(self,nivel): ##
        if self.states['exist dict']:
            K = list( self.states['dict'].keys() )
            L = len( K )
            idx = int(randint(0,L-1))
            counter = 0
            while self.states['dict'][ K[idx] ] > nivel and counter < 50:
                idx = int(randint(0,L-1))
                counter = counter + 1
            if counter == 50 : return None
            print(2*'\n')
            print(4*' ' + K[ idx ] )
            print(2*'\n')
            return K[ idx ]
        return None
    def content2dict(self): # calmala
        D = {}
        for i in self.content2list():
            idx = count_ast(i)
            if idx<len(i) and try_substr(i,0,1)!='#':
                if idx == 0 :
                    D.update( { i[idx:] : idx } )
                else:
                    D.update( { i[idx+1:] : idx } )
        return D
    def dict2content(self,dictionary):
        self.states['content'] = self.title + '{ ' + self.states['text filename'] + ' }\n'
        
        X = self.states['content']
        for J in dictionary.keys():
            if dictionary[J]==0:
                X = X +J+'\n' 
            else:
                X = X + dictionary[J]*'*'+' '+J+'\n' 
        self.states['content'] = X
    def content2list(self):
        X = self.states['content']
        X_list = X.split('\n')
        return X_list
    
    # brainWasherInterface > funcoes > principais
    def save(self): ##
        os.chdir(self.txt_dir)
        
        if self.states['exist text filename'] and self.states['exist dict']:
            self.dict2content( self.states['dict'] )
            fhandle = open( self.states['text filename'] ,'w')
            fhandle.write( self.states['content'] )
            fhandle.close()
            
        #Interface.save(self)
        
        os.chdir(project_dr)
    def comm_load_text_file(self,filename):
        os.chdir(self.txt_dir)
        try:
            file_obj = open(filename,'r')
            RET = file_obj.read()
            file_obj.close()
            self.states.update( {'content': RET,'text filename' : filename, 'exist text filename': True } )
        except:
            self.states.update( { 'exist text filename': False } )
            print('Nao Foi Possivel Carregar o Arquivo')
        try:
            self.states['dict'] = {}
            self.states['dict'].update( self.content2dict() )
            self.states['exist dict'] = True
            
            # print_dict(self.states) ##
            #print_dict(self.states['dict']) ## 
            self.print_dict_info()
            # print(self.states['dict']) ##
            
        except:
            print(flag,'DEU MERDA')
            self.states['exist dict'] = False
        os.chdir(project_dr)        
        
    # brainWasherInterface > funcoes > comandos    
    def commands(self, input_str, main_obj):
        if input_str=='@teste':
            try:
                self.teste()
            except:
                print(flag, 'teste errado')
        elif try_substr(input_str,0, len('@start=(') ) == '@start=(':
            X = try_substr(input_str, len('@start=('), 'all' )[:-1]
            Y = X.split(',')
            try:
                self.uniform_study( int(Y[0]) , int(Y[1]) )
            except:
                print(red('Coloque um Numero'))
        elif try_substr(input_str,0, len('@start=') ) == '@start=':
            X = try_substr(input_str, len('@start='), 'all' )
            try:
                self.uniform_study( int(X) )
            except:
                print(X)
                print(red('Coloque um Numero'))
        elif input_str == '@start':
            self.uniform_study()
        elif try_substr(input_str,0,len('@create')) == '@create':
            if try_substr( input_str, len('@create')+1,'all' )!='':
                self.comm_create_text_file( try_substr( input_str, len('@create')+1,'all' ) )
                #self.states.update( {'content':' ... '} )
                return False
            else:
                return False
        elif input_str=='@save':
            self.save()
        elif try_substr( input_str, 0,len('@load=') ) == '@load=':
            os.chdir(self.txt_dir)
            for i in range( len( os.listdir() ) ):
                print(i,' : ' ,green( os.listdir()[i] ) )
            print()
            try:
                X = try_substr(input_str, len('@load='), 'all')
                Y = os.listdir()
                self.comm_load_text_file( Y[ int(X) ] )
                os.chdir(project_dr)
                return False
            except:
                print(red( ' Escolha um Numero ') )
                os.chdir(project_dr)
                return False
            os.chdir(project_dr)
        elif try_substr(input_str,0,len('@load')) == '@load':
            os.chdir(self.txt_dir)
            if try_substr( input_str, len('@load')+1,'all' )!='':
                self.comm_load_text_file( try_substr( input_str, len('@load')+1,'all' ) )
            else:
                print()
                for i in os.listdir():
                    print(i)
                print()
                if self.states['exist text filename']:
                    try:
                        self.comm_load_text_file( self.states['text filename'] )
                    except:
                        print(flag)
            os.chdir(project_dr)            
            return False
        elif input_str=='@reset study':
            try:
                for i in self.states['dict'].keys():
                    self.states['dict'][i] = 0
                    self.save()
            except:
                print(flag, 'erro!')
            return False
        elif input_str=='@help':
            self.help_c()
            print(green("""
Comandos [ de Interface de Estudo : BrainWasher ] :
            
    1 - Esta interface adiciona informacoes em arquivo de texto formatado. 
    2 - Estas informacoes sao linhas que representam o nome de uma informacao. 
    
        Exemplo de uso, se digitar :
        
            Teorema [ Fundamental do Calculo ] AP pg 100 !
    
            'Teorema [ Fundamental do Calculo ] AP pg 100' ira ser adicionado
                no inventario
            
    3 - O proposito desta inteface eh criar um inventario de nomes 
        de informacoes para estuda-los usando o comando @start
        
1 -     @origem : Retorna para Origem
2 -     @network : Mostra as opcoes da rede de Navegacao de Interfaces
3 -     @content : mostra o conteudo do arquivo de texto selecionado

1 -     @load : Mostra uma lista de nomes de arquivos na pasta corrente
2 -     @load NOME : Abre o arquivo NOME
3 -     @load= : Mostra uma lista numerada dos arquivos na pasta corrente
4 -     @load=NUMERO : Abre o arquivo correspondente ao numero
5 -     @select NOME: Apenas muda o nome do arquivo texto, 
                nao muda o conteudo, requer @load
                
1 -     @start : Inicia um estudo com um loop de 50 iteracoes
2 -     @start=NUMERO : Inicia um estudo com loop de NUMERO iteracoes
3 -     @start=(NUMERO,NIVEL) : Inicia um estudo com NUMERO de iteracoes
            e apenas as informacoes com acertos menor ou igual a NIVEL
            sao selecionadas para estudo.
4 -     @reset study : reinicia a pontuacao das informacoes do inventario            
            """))     
        else:
            return inventoryTextInterface.commands(self,input_str, main_obj)
        
class bookshelfInterface(inventoryTextInterface): # PROIBIDO MODIFICAR 09072020
    def __init__(self, filename, dad_ref, main_obj, txt_dir):
        inventoryTextInterface.__init__(self, filename, dad_ref, main_obj, txt_dir)
    def content2dict(self): # calmala
        D = {}
        for i in self.content2list():
            if try_substr(i,0,1)!='#' and i!='' and try_substr(i,0,1)!=' ':
                L = i.split('|')
                SHORT = L[0]
                PATH = L[1]
                D.update( { SHORT.rstrip() : PATH.lstrip() } )
        return D
    def dict2content(self,dictionary):
        self.states['content'] = self.title + '{ ' + self.states['text filename'] + ' }\n'
        X = self.states['content']
        for J in dictionary.keys():
            if dictionary[J]==0:
                X = X +J+'\n' 
            else:
                X = X + dictionary[J]*'*'+' '+J+'\n' 
        self.states['content'] = X    
    def commands(self, input_str, main_obj):
        if input_str == '@shortcuts':
            print('Biblioteca : \n')
            for i in self.states['dict'].keys():
                print( green(i) )
                print( len(i)*'-' )
                print('\t' ,yellow( self.states['dict'][i] ) )
            print()
            return False
        elif input_str=='@save':
            return False
        elif input_str=='@help':
            self.help_c()
            print(green("""
        Comandos [ Biblioteca de Atalhos de Livros ] :
            
            1 - Organizar atalhos de livros para ser usado com o comando @pdf=
            2 - Formato:
                ATALHO | ENDERECO_DO_ARQUIVO
        
        INFORMACAO ! : finalizar um input com ! ira adicionar no arquivo de 
            texto o que estiver escrito antes
        
1 -         @origem : Retorna para Origem
2 -         @network : Mostra as opcoes da rede de Navegacao de Interfaces
3 -         @content : mostra o conteudo do arquivo de texto selecionado
4 -         @goto NOME : Vai para uma interface cujo nome e NOME           
5 -         @create NOME.txt : cria um arquivo de texto
6 -         @editor : Abre o editor externo padrao para .txt
7 -         @load : Mostra uma lista de nomes de arquivos na pasta corrente
8 -         @load NOME : Abre o arquivo NOME
9 -         @load= : Mostra uma lista numerada dos arquivos na pasta corrente
10 -        @load=NUMERO : Abre o arquivo correspondente ao numero
11 -        @select NOME: Apenas muda o nome do arquivo texto, 
                nao muda o conteudo, requer @load          
12 -        @shortcuts : Mostra os livros e seus atalhos para serem usados 
                com o comando @pdf=
            """))
            return False
        else:
            return inventoryTextInterface.commands(self,input_str, main_obj)
        
class randomTaskInterface(brainWasherInterface): # PROIBIDO MODIFICAR 10072020 TEM UM ERRO AQUI
    """ Carrega uma lista de tarefas e pode mudar para Interface Principal, em sua informacao existe uma lista de tarefas """
    def __init__(self, filename, dad_ref, main_obj, txt_dir):
        brainWasherInterface.__init__(self, filename, dad_ref, main_obj, txt_dir)
        # self.states['exist dict'] = False
        # self.states['dict'] = {}
        #self.states['content'] = ''
        self.desc = 'RANDOM TASK MANAGER'
        self.title = '# LISTA DE TAREFAS : { ' + str(date.today()) + ' } '
        self.old_title = None
        #self.states['day guard'] = False
    def content2dict(self): # calmala
        D = {}
        #self.states['dict'] = {}
        for i in self.content2list():
            idx = count_ast(i)
            if idx<len(i) and try_substr(i,0,1)!='#':
                if idx == 0 :
                    D.update( { i[idx:] : idx } )
                else:
                    D.update( { i[idx+1:] : idx } )
            elif try_substr(i,0,1)=='#':
                self.old_title = i
        return D    
    def save(self): ##
        os.chdir(self.txt_dir)
        try:
            for i in self.states['dict'].keys():
                self.states['dict'][i] = 0
        except:
            print(flag, 'erro!')
        Interface.save(self)
        
        if self.states['exist text filename'] and self.states['exist dict']:
            self.dict2content( self.states['dict'] )
            #self.states['dict'] = {}
            fhandle = open( self.states['text filename'] ,'w')
            fhandle.write( self.states['content'] )
            fhandle.close()
            
        #Interface.save(self)
        
        os.chdir(project_dr)    
    def random_info(self,nivel): ##
        if self.states['exist dict']:
            K = list( self.states['dict'].keys() )
            L = len( K )
            idx = int(randint(0,L-1))
            counter = 0
            while self.states['dict'][ K[idx] ] >= nivel and counter < 50:
                idx = int(randint(0,L-1))
                counter = counter + 1
            if counter == 50 : return None
            #print(2*'\n')
            #print(4*' ' + K[ idx ] )
            #print(2*'\n')
            return K[ idx ]
        print('retornando none')
        return None    
    def uniform_study(self,repetition_number=50,nivel=20):
    
        # Guarda de Dia
        if self.old_title == self.title:
            self.states['day guard'] = True
            
        else:
            self.states['day guard'] = False
            
        if self.states['day guard']:
            
            return None
            
        guard = True
        for i in range(repetition_number):
            
            if guard:
                N = self.random_info(nivel)
            if N == None:
                print(red ('\n\t ja fez as tarefas do dia !\n') )
                #print( self.states['dict'] )
                break    
            print('\nTAREFA ['+yellow(' SORTEIO UNIFORME ')+'] :\n'+LINE_str)    
            print(2*'\n')
            print(4*' ',N)    
            print(2*'\n')    
                
            print( 'MODO [ ' + green('TAREFA')+' ] : { ', yellow('Nro de Sorteios :'), red(str(repetition_number-i))  ,' }'  )
            print(white(LINE_str))
            INP = input(' [ G ou "Enter" ] >>>>> ')
            os.system('CLS')
            if INP == 'G':
                self.states['dict'][N] = self.states['dict'][N] + 1
                guard = True
            else: # Guarda de Mudanca
                guard = False
            X = self.states['dict']
            
            print()
            
            self.print_dict_info()
            # print_dict(self.states['dict'])
        #print( self.states['dict'] )
        self.dict2content( self.states['dict'] )
        #print(self.states['content'])
        #Wself.save()    
    def print_dict_info(self):
        D = self.states['dict']
        K = D.keys()
        print()
        for i in K:
            if D[i]==0:
                print(i,':',red(' ... '))
            else:
                print(i, ':', green( ' - OK - ' ))
        print()
    def commands(self, input_str, main_obj):
        if input_str=='@teste':
            try:
                self.teste()
            except:
                print(flag, 'teste errado')
            return False
        elif input_str == '@start':
            try:
                self.uniform_study(100,1)
            except:
                print('Eis aqui um erro')
            return False
        elif try_substr(input_str,0,len('@create')) == '@create':
            if try_substr( input_str, len('@create')+1,'all' )!='':
                self.comm_create_text_file( try_substr( input_str, len('@create')+1,'all' ) )
                #self.states.update( {'content':' ... '} )
                return False
            else:
                return False
        elif input_str=='@save':
            self.save()
        elif try_substr( input_str, 0,len('@load=') ) == '@load=':
            os.chdir(self.txt_dir)
            for i in range( len( os.listdir() ) ):
                print(i,' : ' ,green( os.listdir()[i] ) )
            print()
            try:
                X = try_substr(input_str, len('@load='), 'all')
                Y = os.listdir()
                self.comm_load_text_file( Y[ int(X) ] )
                os.chdir(project_dr)
                return False
            except:
                print(red( ' Escolha um Numero ') )
                os.chdir(project_dr)
                return False
            os.chdir(project_dr)
        elif try_substr(input_str,0,len('@load')) == '@load':
            os.chdir(self.txt_dir)
            if try_substr( input_str, len('@load')+1,'all' )!='':
                self.comm_load_text_file( try_substr( input_str, len('@load')+1,'all' ) )
            else:
                print()
                for i in os.listdir():
                    print(i)
                print()
                if self.states['exist text filename']:
                    try:
                        self.comm_load_text_file( self.states['text filename'] )
                    except:
                        print(flag)
            os.chdir(project_dr)            
            return False
        elif input_str=='@reset task list':
            try:
                for i in self.states['dict'].keys():
                    self.states['dict'][i] = 0
                self.dict2content( self.states['dict'] )
                    #self.save()
            except:
                print(flag, 'erro!')
            return False
        elif input_str=='@help':
            self.help_c()
            print(green("""
Comandos [ Interface de Tarefas Randomicas ] :
            
    1 - Esta interface adiciona informacoes em arquivo de texto formatado. 
    2 - Estas informacoes sao linhas que representam uma tarefa
    
        Exemplo de uso, se digitar :
        
            Tarefa [ Estudo ] { 1 hora } !
    
            'Tarefa [ Estudo ] { 1 hora }' ira ser adicionado
                no inventario
            
    3 - O proposito desta inteface eh criar um inventario de tarefas 
        de forma que usando o comando @start as tarefas sao sorteadas
        de maneira uniforme
    4 - As tarefas somente podem ser feitas uma vez ao dia, se quiser 
        repetir a tarefa, va no arquivo de save e mude a primeira linhas
        mantendo o caractere # no inicio
        
1 -     @origem : Retorna para Origem
2 -     @network : Mostra as opcoes da rede de Navegacao de Interfaces
3 -     @content : mostra o conteudo do arquivo de texto selecionado

1 -     @load : Mostra uma lista de nomes de arquivos na pasta corrente
2 -     @load NOME : Abre o arquivo NOME
3 -     @load= : Mostra uma lista numerada dos arquivos na pasta corrente
4 -     @load=NUMERO : Abre o arquivo correspondente ao numero
5 -     @select NOME: Apenas muda o nome do arquivo texto, 
                nao muda o conteudo, requer @load
                
1 -     @start : Inicia um estudo com um loop de 50 iteracoes
2 -     @start=NUMERO : Inicia um estudo com loop de NUMERO iteracoes
3 -     @start=(NUMERO,NIVEL) : Inicia um estudo com NUMERO de iteracoes
            e apenas as informacoes com acertos menor ou igual a NIVEL
            sao selecionadas para estudo.
4 -     @reset task list : reinicia a pontuacao das informacoes do inventario           
            """))
            return False
        else:
            return inventoryTextInterface.commands(self,input_str, main_obj)

class rpgBrainwasher(brainWasherInterface):
    def __init__(self, filename, dad_ref, main_obj, txt_dir):
        brainWasherInterface.__init__(self,filename, dad_ref, main_obj, txt_dir)
    def rpg_status_update(self,main_obj):
        if POMO_MIN_SEC - main_obj.time_shift <0: # SP BAIXO ~ Comida
            while input('\n\t Seu SP esta baixo, deveria comer alguma coisa, deveria correr um pouco, deveria relaxar um pouco ...')!='ja fiz tudo isso':
                print('\n \t \t Coma algo ! (digite : ja fiz tudo isso)')
            main_obj.time_shift = 0
            main_obj.time_init = time()
        elif self.HP_it<=0: # HP BAIXO ~ Heal de MP
            while input('\n\t WASTED, voce morreu, para ressucitar deveria comer alguma coisa, deveria correr um pouco, deveria relaxar um pouco ...')!='ja fiz tudo isso':
                print('\n \t \t Coma algo ! (digite : ja fiz tudo isso)')
            self.HP_it = HP
        elif False: # MP BAIXO ~ Comida
            pass
        else:
            main_obj.time_shift = time() - main_obj.time_init
            if POMO_MIN_SEC - main_obj.time_shift>=0:
                print()
                print( status( self.HP_it ,HP,'HP '+'('+ str(HP) + ')', red) )
                print( status(POMO_MIN_SEC - main_obj.time_shift, POMO_MIN_SEC,'SP '+POMO_MIN_SEC_desc, green) )
                print( status( self.MP_it ,MP,'MP '+'('+ str(MP) + ')',cyan) )
    def healing(self):
        change = 0.5*self.MP_it
        self.MP_it = change
        self.HP_it = min( self.HP_it + change, HP )
        
    def uniform_study(self,repetition_number=100,nivel=20):
        self.HP_it = HP
        self.MP_it = 0.2*MP
        for i in range(repetition_number):
            try:
                self.rpg_status_update(self.main_obj)
            except:
                pass
            print('\nPERGUNTA ['+yellow(' SORTEIO UNIFORME ')+'] :\n'+LINE_str)
            N = self.random_info(nivel)
            if N == None: break
            print( 'MODO [ ' + green('ESTUDO')+' ] : { ', yellow('Nro de Sorteios :'), red(str(repetition_number-i))  ,' }'  )
            print(white(LINE_str))
            INP = input(' [ ?, G, @heal ] >>>>> ')
            os.system('CLS')
            if self.states['dict'][N]!=0:
                if INP == '?':
                    self.states['dict'][N] = self.states['dict'][N] - 1
                    self.HP_it = self.HP_it - 1
                elif INP == 'G':
                    self.states['dict'][N] = self.states['dict'][N] + 1
                    self.MP_it = min( self.MP_it + 1, MP )
                elif INP == '@heal':
                    self.healing()
            else:
                if INP == 'G':
                    self.states['dict'][N] = self.states['dict'][N] + 1
                    self.MP_it = min( self.MP_it + 1, MP )
                elif INP == '?':
                    #self.states['dict'][N] = self.states['dict'][N] - 1
                    self.HP_it = self.HP_it - 1    
                elif INP == '@heal':
                    self.healing()
            X = self.states['dict']
            
            print()
            
            self.print_dict_info()
            # print_dict(self.states['dict'])
        self.save()

class cell_book(TextInterface): # UNFINISHED
    def __init__(self,filename,dad_ref,main_obj):
        TextInterface.__init__(self,filename,dad_ref,main_obj)
    
    # cell_book > funcoes > auxiliares
    def append_cell(self):
        pass
    def help_cell_format(self):
        pass
    def random_cell(self):
        pass
    def read_cell(self,position):
        pass
    def cells2index_projection(self):
        pass
    
    # cell_book > funcoes > comandos
    def commands(self, input_str):
        if False:
            pass
        else:
            return TextInterface.commands(self,input_str)
        

class selectionInterface(VerticalOrientedInterface):
    """ Eh uma interface que cria uma lista dos arquivos correntes no diretorio e eh possivel apontar um dos arquivos
    usando o teclado. """
    def __init__(self,filename,dad_ref,main_obj):
        VerticalOrientedInterface.__init__(self,filename,dad_ref,main_obj)
        self.listdir = os.listdir()
        self.len_listdir = len( self.listdir )
        self.pos = 0 # Must sent a message to dad
    # Funcoes Auxiliares
    def print_dir(self):
        os.system('CLS')
        print('\n[ Selecao de Arquivo ] :\n')
        c = 0
        for i in self.listdir:
            if c==self.pos:
                print( yellow('---> '+i) )
            else:
                print( 4*' ',white(i) )
            c = c+1
        #os.system('pause')
    
    # callbacks de input de keyboard
    def up_callback(self,head,X):
        if self.pos >0 :
            self.pos = self.pos - 1
            self.print_dir()
        
        #if w32.GetWindowText( w32.GetForegroundWindow() )=='C:\Python\Python38\python.exe': 
        #    kbd.press('enter')
    def down_callback(self,head,X):
        if self.pos < self.len_listdir-1:
            self.pos = self.pos + 1
            self.print_dir()
        #if w32.GetWindowText( w32.GetForegroundWindow() )=='C:\Python\Python38\python.exe': 
        #    kbd.press('enter')
    def right_callback(self,head,X):
        pass
        #print( 'este arquivo foi selecionado' ,self.listdir[ self.pos ] )
        #if w32.GetWindowText( w32.GetForegroundWindow() )=='C:\Python\Python38\python.exe': 
        #    kbd.press('enter')


class roguelikeInterface(VerticalOrientedInterface):
    def __init__(self,filename=None,dad_ref=None,main_obj=None):
        VerticalOrientedInterface.__init__(self,filename,dad_ref,main_obj)
        self.field = [ [ '.' for i in range(40) ] for j in range(20) ]
        self.char_pos = [0,0]
    def up(self):
        X = self.char_pos
        try:
            self.field[ self.char_pos[0] ] [ self.char_pos[1] ] = '.'
            self.char_pos[0] = self.char_pos[0] - 1
        except:
            self.char_pos = X
    def down(self):
        X = self.char_pos
        try:
            self.field[ self.char_pos[0] ] [ self.char_pos[1] ] = '.'
            self.char_pos[0] = self.char_pos[0] + 1
        except:
            self.char_pos = X        
    def left(self):
        X = self.char_pos
        try:
            self.field[ self.char_pos[0] ] [ self.char_pos[1] ] = '.'
            self.char_pos[1] = self.char_pos[1] - 1
        except:
            self.char_pos = X        
    def right(self):
        X = self.char_pos
        try:
            self.field[ self.char_pos[0] ] [ self.char_pos[1] ] = '.'
            self.char_pos[1] = self.char_pos[1] + 1
        except:
            self.char_pos = X                
    def up_callback(self,head,X):
        self.up()
        self.loop_callback()
        if w32.GetWindowText( w32.GetForegroundWindow() )=='C:\Python\Python38\python.exe': 
            #kbd.press('enter')
            pass
    def down_callback(self,head,X):
        self.down()
        self.loop_callback()
        if w32.GetWindowText( w32.GetForegroundWindow() )=='C:\Python\Python38\python.exe': 
            #kbd.press('enter')
            pass
    def left_callback(self,head,X):
        self.left()
        self.loop_callback()
        if w32.GetWindowText( w32.GetForegroundWindow() )=='C:\Python\Python38\python.exe': 
            #kbd.press('enter')
            pass
    def right_callback(self,head,X):
        self.right()
        self.loop_callback()
        if w32.GetWindowText( w32.GetForegroundWindow() )=='C:\Python\Python38\python.exe': 
            #kbd.press('enter')
            pass
    def loop_callback(self):
        os.system('CLS')
        self.print_char()
        self.print_field()
    def print_field(self):
        for i in self.field:
            S = ''
            for j in i:
                S = S+j
            print(S)
    def print_char(self):
        self.field[self.char_pos[0]][ self.char_pos[1]] = '@'

# -------------------------------------------------------------------------------------------------------
# MAIN LOOP
# -------------------------------------------------------------------------------------------------------

class MainInterface(VerticalOrientedInterface): # FINALIZADO NA VERSAO
    def __init__(self,filename='main06072020',dad_ref=None):
        VerticalOrientedInterface.__init__(self,filename,dad_ref,None)
        
        self.time_shift = None
        self.time_init = None

        self.states['default pdf reader'] = ''
        self.states['default ebooks folder'] = 'C:'
        self.states['default text editor'] = 'start notepad'
        
        VerticalOrientedInterface.load(self)
        
        self.network['Interface de Origem'] = self
        self.desc = 'INTERFACE PRINCIPAL'
        
        self.network['TASK MANAGER'] = randomTaskInterface('rndTask09072020',self,self,project_dr)
        self.network['TASK MANAGER'].states['text filename'] = 'rnd_tasks'
        self.network['TASK MANAGER'].load()
        self.network['TASK MANAGER'].comm_load_text_file('rnd_tasks')
        
        
        self.network['TEXT INTERFACE'] = TextInterface('text_file06072020',self,self,project_dr+'text')
        self.network['ADD CELL INFO'] = add_cell_header_TextInterface('add_cell07072020',self,self,project_dr+'text')
        self.network['BRAINWASHER INTERFACE'] = rpgBrainwasher('brainWasher_08072020',self, self, project_dr+'brainWashers09072020')
        self.network['INVENTORY TEXT INTERFACE'] = inventoryTextInterface('inv_cell07072020',self,self, project_dr+'information_inventory')
        
        self.network['BOOKSHELF INTERFACE'] = bookshelfInterface('bookshelf_09072020',self,self, project_dr+'books')
        self.network['BOOKSHELF INTERFACE'].desc = 'BOOKSHELF'
        self.network['BOOKSHELF INTERFACE'].title = '# Inventario de Shortcuts de Enderecos e Nomes de Livros: { ' + str(date.today()) + ' }\n# ... SHORTCUT : "ENDERECO" '
        self.network['BOOKSHELF INTERFACE'].states['text filename'] = 'books_shortcuts09072020'
        self.network['BOOKSHELF INTERFACE'].comm_load_text_file('books_shortcuts09072020')
        #print_dict(self.network['BOOKSHELF INTERFACE'].states['dict'])
        
        #self.network['ROGUELIKE'] = roguelikeInterface('rogue14072020',self, self)
        #self.network['ROGUELIKE'].desc = 'RPG ROGUELIKE'
        
        #self.network['SELECTION'] = selectionInterface( 'selectionTeste',self, self )
        #self.network['SELECTION'].desc = 'SELECTION'
        
        self.states['auto interface info']=True
        
        os.system('CLS')
        
        #self.states.update( { 'return?' : True } )
        
        #self.message = { 'return to dad by exit':  False }
    def up_callback(self,head,X):
        try:
            head.head = self.network['TASK MANAGER']
        except:
            pass
        if w32.GetWindowText( w32.GetForegroundWindow() )=='C:\Python\Python38\python.exe': 
            kbd.press('enter')
    def down_callback(self,head,X):
        try:
            head.head = self.network['BOOKSHELF INTERFACE']
        except:
            pass
        if w32.GetWindowText( w32.GetForegroundWindow() )=='C:\Python\Python38\python.exe': 
            kbd.press('enter')
    def left_callback(self,head,X):
        head.head = self.network['Interface de Origem']
        if w32.GetWindowText( w32.GetForegroundWindow() )=='C:\Python\Python38\python.exe': 
            kbd.press('enter')
    def right_callback(self,head,X):
        try:
            head.head = self.network['BRAINWASHER INTERFACE']
        except:
            pass
        if w32.GetWindowText( w32.GetForegroundWindow() )=='C:\Python\Python38\python.exe': 
            kbd.press('enter')
    def print_dict(self):
        print()
        print('filename :',self.states['filename'])
        print('pdf reader :', self.states['default pdf reader'])
        print('txt editor :', self.states['default text editor'])
        print()
    def commands(self, input_str, main_obj):
        if input_str == '@help':
            self.help_c()
            print(green("""
        Comandos [ de Navegacao ] :
        
        @network   : Mostra as opcoes da rede de Navegacao de Interfaces
        @origem    : Retorna para Origem
        @task      : Vai para Interface de Tarefas Randomicas
        @text      : Vai para a Interface de Manipucacao de Texto
        @add       : Vai para a Interface de Adicionar Celulas de Informacao
        @inv       : Vai para Inteface de Inventarios
        @brain     : Vai para interface de estudo brainWasher
        @goto NOME : Vai para uma interface cujo nome e NOME
        @goto : Mostra as Opcoes de Navegacao
        @set pdf reader : Configura o leitor de pdf, coloque o endereco 
            ou digite start NOME_DO_PROGRAMA
        @set text editor : Configura o editor de texto, coloque o endereco
            ou digite start NOME_DO_PROGRAMA
        @pdf : abre o leitor de pdf
            """))
        else:
            return VerticalOrientedInterface.commands(self,input_str,main_obj)
        
class MainHeadInterface(HeadInterface): # FINALIZADO NA VERSAO
    """
    """
    def __init__(self,filename, oriented_interface,main_obj):
        HeadInterface.__init__(self,filename, oriented_interface,main_obj)
        self.head = oriented_interface
    # callbacks de keyboard input    
    def up_callback(self,X):
        self.head.up_callback(self,X)
    def down_callback(self,X):
        self.head.down_callback(self,X)
    def left_callback(self,X):
        self.head.left_callback(self,X)
    def right_callback(self,X):
        self.head.right_callback(self,X)
    
    def commands(self,input_str,main_obj):
        if input_str == '@origem':
            save_head = self.head
            self.head = self.head.network['Interface de Origem']
        elif try_substr(input_str,0,len('@goto') ) == '@goto':
            try:
                self.head = self.head.network[ try_substr(input_str,len('@goto')+1, 'all' ) ]
            except:
                self.head.comm_show_network()
            return False
        elif input_str == '@testeiro':
            try:
                teste()
            except:
                print(red('ERRO') )
            return False
        elif input_str == '@books' and self.head.desc =='INTERFACE PRINCIPAL':
            self.head = self.head.network[ 'BOOKSHELF INTERFACE' ]
            return False
        elif input_str == '@add' and self.head.desc =='INTERFACE PRINCIPAL':
            self.head = self.head.network[ 'ADD CELL INFO' ]
            return False
        elif input_str == '@text' and self.head.desc =='INTERFACE PRINCIPAL':
            self.head = self.head.network[ 'TEXT INTERFACE' ]
            return False
        elif input_str == '@inv' and self.head.desc =='INTERFACE PRINCIPAL':
            self.head = self.head.network[ 'INVENTORY TEXT INTERFACE' ]
            return False
        elif input_str == '@brain' and self.head.desc =='INTERFACE PRINCIPAL':
            self.head = self.head.network[ 'BRAINWASHER INTERFACE' ]
            return False
        elif input_str == '@task' and self.head.desc =='INTERFACE PRINCIPAL':
            self.head = self.head.network[ 'TASK MANAGER' ]
            return False    
        elif input_str =='@set pdf reader':
            main_obj.states['default pdf reader'] = input(' Endereco Completo ou [start NOME_DO_PROG] : ')
            return False
        elif input_str =='@pdf':
            os.system('"'+main_obj.states['default pdf reader']+'"')
            return False
        elif try_substr( input_str, 0, len('@pdf=')  ) == '@pdf=':
            X = try_substr( input_str, len('@pdf='), 'all'  )
            try:
                if X in main_obj.network['BOOKSHELF INTERFACE'].states['dict']:
                    Y = main_obj.network['BOOKSHELF INTERFACE'].states['dict'][X]
                    Z = main_obj.states['default pdf reader']+' '+Y
                    print(Z)
                    os.system( Z )
            except:
                try:
                    os.system( '"'+main_obj.states['default pdf reader']+'" '+X)
                except:
                    print('Nao Foi Possivel Carregar o Arquivo')
            return False
        elif input_str =='@set ebooks folder':
            main_obj.states['default ebooks folder'] = input( ' Endereco Completo ou [start NOME_DO_PROG] : ' )
            return False
        elif input_str =='@set text editor':
            main_obj.states['default text editor'] = input( ' Endereco Completo ou [start NOME_DO_PROG] : '  )
            return False
        else:
            return self.head.commands(input_str,main_obj)        
        

def teste(): # lixo
    print('\n',flag, ': Para ser usado no comando @teste do HeadInterface')
    #import tkinter as tk
    #top = tk.Tk()
    #top.mainloop()
    #OBJ = coloredPrintRGB("EITA PORRA",[0,0,0],[255,255,255])
    #OBJ.rangerPrint(number=70,maxNumber=100,iniColor='r',endColor='b',returnString=True)
    #print( progress_bar(0.5) )
    #print( hp_status(number = 1.4,desc='HP') )
    #print(TIME_SHIFT)
    import keyboard as kbd
    print( kbd.KEY_UP )
    
    
def main(): # FINALIZADO NA VERSAO

    # Main Objects
    pos_0 = MainInterface()
    head = MainHeadInterface(filename='head06072020',oriented_interface=pos_0,main_obj=pos_0)
    
    # Main Loop
    count = 0
    print( yellow(COM_str0) )
    
    # Pomodoro 
    pos_0.time_init = time()
    pos_0.time_shift = 0
    
    # keys callback registers : Faz sentido colocar os callbacks no HeadInterface
       
    
    while True:
        #kbd.unhook_all()
        #kbd.on_press_key(kbd.KEY_UP, head.up_callback)
        #kbd.on_press_key(kbd.KEY_DOWN, head.down_callback )
        #kbd.on_press_key('left', head.left_callback )
        #kbd.on_press_key('right', head.right_callback )
    
        print( white(LINE_str)+white(PROG_NAME_str)+'\n'+white(LINE_str))
        
        print(green("""
    Comandos [ de Navegacao ] :
        
    1 - @network   : Mostra as opcoes da rede de Navegacao de Interfaces
    2 - @origem    : Retorna para Origem
    3 - @task      : Vai para Interface de Tarefas Randomicas
    4 - @text      : Vai para a Interface de Manipucacao de Texto
    5 - @add       : Vai para a Interface de Adicionar Celulas de Informacao
    6 - @inv       : Vai para Inteface de Inventarios
    7 - @brain     : Vai para interface de estudo brainWasher
    8 - @goto NOME : Vai para uma interface cujo nome e NOME
        """))
        
        
        print( white(LINE_str) )
        if head.head.desc=='INTERFACE PRINCIPAL':
            print( white('[ ') + red(str(count)) + white(' : ') + head.head.short_desc() + white(' ]') )
        else:
            print( white('[ ') + red(str(count)) + white(' : ') + white( head.head.network['Interface de Origem'].desc ) + white(' > ') + head.head.short_desc() + white(' ]') )
        
        if head.head.states['auto interface info']:
           head.head.print_dict()
        
        os.system('doskey /listsize=0')
        inp = input(' >>> ')
        inp = inp.lstrip()
        inp = inp.rstrip()
        os.system('CLS')
        
        # ACOES DE ITERACAO
        if head.commands(inp,pos_0): # Condicao de Saida de Loop
            head.states.update({'count' : count })
            head.head.save()
            break
        if head.head.states['return?']: # Condicao de Retorno para Interface Principal
            head.head.states['return?']=False
            head.head = pos_0
        os.chdir(project_dr)
        
        # ATUALIZACAO DE ITERACAO
        count = count + 1 
       
        # Pomodoro update
        # pos_0.rpg_status_update()
                
        
main()
os.chdir(dir_origem)

