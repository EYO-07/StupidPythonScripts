# PROGRAMAS ESTUPIDOS EM PYTHON [ FILE EXPLORER ESTUPIDO TOSCO ]

# SABER : Basico da Linguagem Python, Basico da Orientacao a Objeto em Python, Importar Modulos

# 1) Display no Terminal/Standart Output Colorido ~ colorama feito por terceiros

# 2) Controle atraves dos botoes de setas do Teclado ~ keyboard feito por terceiros 

# 3) Memoriza a ultima posicao de selecao de diretorios ja visitados ~ memory_object

# 4) Fecha o programa quando aperta o botao escape ~ living_object

# 5) UNICA FUNCIONALIDADE ESTUPIDA : copia para o clipboard (control C) o endereco da selecao ~ pyperclip

# GLOBAL IMPORTS
import keyboard as kbd # permite criar escutas/listeners de inputs de botoes do teclado
from time import sleep # 
import threading as thr # Paradigma Threading threads ~ processos
import os # operational system 
import win32gui as w32 # 
import colorama # 
import pyperclip as ppc

# GLOBAL VARS [ os ]
isdir = os.path.isdir

# GLOBAL VARS [ colorama ]
colorama.init()
CY = colorama.Fore.CYAN
RD = colorama.Fore.RED
BL = colorama.Fore.BLUE
GR = colorama.Fore.GREEN
YL = colorama.Fore.YELLOW
WT = colorama.Fore.WHITE

# GLOBAL FUNCTIONS [ colorama ]
def print_long_pointed_list(container = [0,1,2], description = 'item :', position = 0, list_size = 10):
    count = 0
    for i in container:
        if count > position+ list_size or count < position -list_size:
            if count == position + list_size + 1 or count == position - list_size - 1:
                print('...')
        elif count == position:
            print( CY, description, i)
        else:
            print( WT, description, i)
        count = count + 1
        
def is_dirXfile(x):
    if isdir(x):
        return CY + '[-]'
    else:
        return GR + ' * '
        
def is_python_in_focus():
    return w32.GetWindowText( w32.GetForegroundWindow() )=='C:\\Python\\Python38\\python.exe'

# GLOBAL CLASSES
class memory_object(object):
    def __init__(self):
        self.states = {}
        self.memory = {}
    def default_states(self):
        self.states = {}
    def memorization(self,key):
        self.memory.update( { key: self.states } )
    def remembering(self,key):
        try:
            self.states = self.memory[ key ]
        except:
            self.default_states()
            
class living_object(object):
    def __init__(self):
        self.life = True
    def esc_call(self,x): 
        if not is_python_in_focus(): return None
        self.life = False
    def in_control(self):
        kbd.on_press_key('esc', self.esc_call)
        
class arrow_keys_interface_object(object):
    def __init__(self): 
        pass
    def display(self):
        os.system('cls')
        print('key pressed')
    def in_control(self):
        kbd.on_press_key('up', self.up_call)
        kbd.on_press_key('down', self.down_call)
        kbd.on_press_key('left', self.left_call)
        kbd.on_press_key('right', self.right_call)
    def up_call(self,x): 
        if not is_python_in_focus(): return None
        # do something
        self.display()
    def down_call(self,x): 
        if not is_python_in_focus(): return None
        # do something
        self.display()
    def left_call(self,x): 
        if not is_python_in_focus(): return None
        # do something
        self.display()
    def right_call(self,x): 
        if not is_python_in_focus(): return None
        # do something
        self.display()

# --------------------------------- START FROM HERE -----------------------------------

class file_explorer_estupido(living_object, memory_object, arrow_keys_interface_object):
    def __init__(self):
        living_object.__init__(self)
        memory_object.__init__(self)
        arrow_keys_interface_object.__init__(self)
        self.states = { 'current_dir' : os.getcwd(), 'pos': 0, 'list_dir': os.listdir() }
        self.memory = { self.states['current_dir'] : self.states }
        ppc.copy( self.states['current_dir'] + '\\' + self.states['list_dir'][ self.states['pos'] ] )
    def print_long_pointed_list(self): 
        container = self.states['list_dir']
        position = self.states['pos']
        list_size = 15
        count = 0
        for i in container:
            if count > position+ list_size or count < position -list_size:
                if count == position + list_size + 1 or count == position - list_size - 1:
                    print('...')
            elif count == position:
                print( is_dirXfile(i), YL, '>', i , '<')
            else:
                print( is_dirXfile(i), ' ', WT, i, ' ')
            count = count + 1
    def display(self):  
        os.system('cls')
        print(WT + 'Diretorio :', self.states['current_dir'], '\nTamanho :', len( self.states['list_dir'] ),'\n')
        self.print_long_pointed_list()
    def in_control(self):
        kbd.unhook_all()
        living_object.in_control(self)
        arrow_keys_interface_object.in_control(self)
    def up_call(self,x): 
        if not is_python_in_focus(): return None
        if self.states['pos'] > 0:
            self.states['pos'] = self.states['pos'] - 1
        self.display()
        ppc.copy( self.states['current_dir'] + '\\' + self.states['list_dir'][ self.states['pos'] ] )
    def down_call(self,x): 
        if not is_python_in_focus(): return None
        if self.states['pos'] + 1 < len( self.states['list_dir'] ) :
            self.states['pos'] = self.states['pos'] + 1
        self.display()
        ppc.copy( self.states['current_dir'] + '\\' + self.states['list_dir'][ self.states['pos'] ] )
    def left_call(self,x): 
        if not is_python_in_focus(): return None
        OLD_DIR = self.states['current_dir']
        self.memorization( OLD_DIR )
        os.chdir('..')
        self.update()
        self.display()
    def right_call(self,x): 
        if not is_python_in_focus(): return None
        OLD_DIR = self.states['current_dir']
        self.memorization( OLD_DIR )
        try:
            os.chdir( self.states['list_dir'][ self.states['pos'] ] )
            self.update()
        except:
            os.chdir(OLD_DIR)
            self.update()
        self.display()    
    def update(self):
        self.remembering( os.getcwd() )
    def default_states(self):
        self.states = { 'current_dir' : os.getcwd(), 'pos': 0, 'list_dir': os.listdir() }
        
def main_thread(obj):
    obj.in_control()
    obj.display()
    while obj.life:
        sleep(1)

def main():
    E = file_explorer_estupido()
    THR_obj = thr.Thread( target = main_thread, args=(E,) )
    THR_obj.start()
main()


