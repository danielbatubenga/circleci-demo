# Importe a função Add e confirme que ela funciona corretamente. 
from main import Add 

def TestAdd():
         assert Add(5,5) == 10
         assert Add(2,3) == 5 
         print( "Adicionar função funciona corretamente" ) 
if __name__ == '__main__' : 
        TestAdd()

