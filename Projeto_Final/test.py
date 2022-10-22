
    
    
def decorador(func):
    print(f'Essa função: {func}')
    
    
@decorador        
def decorado(x):
    print(x)

@decorador
def decorado_2():
    print('Estou sendo decorado')

decorado(3)
decorado_2()