def func_1(a, b):
    soma = a + b


    # 1. Se chamarmos uma função dentro de outra função...
    resultado = func_2(a, b)
    # 3. E assim, quando retornar o resultado dela, a primeira função, que foi quem a chamou, pode mostrar ele
    return soma, resultado


def func_2(c, d):
    
    resultado_2 = c * d
    # 2. A segunda função pode retornar o resultado da suas ações à primeira
    return resultado_2
    


chamando_func = func_1(3,4)

print(chamando_func)