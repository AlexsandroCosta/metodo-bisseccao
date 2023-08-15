import math
import re

def rcbPrec():
    prec = input('Precisão (Ex: 10^-3): ')

    if '^' in prec:
        x = prec.split('^')
        return float(float(x[0])**float(x[1]))
    
def lssc(func, n, op):
    if op in func:
        mod = False
        i = func.index(op[0])

        if func[i+len(op)+1] != 'x':
            n = float(func[func.index('(')+1])
            mod = True
        
        if op == 'log':
            x = math.log10(n)
        elif op == 'sqrt':
            x = math.sqrt(n)
        elif op == 'sen':
            x = math.sin(n)
        elif op == 'cos':
            x = math.cos(n)

        if func[i-1] not in '-+*/':
            if mod:
                return func.replace(f'{op}({func[i+len(op)+1]})', '*'+str(x))
            else:
                return func.replace(f'{op}(x)', '*'+str(x))
        else:
            if mod:
                return func.replace(f'{op}({func[i+len(op)+1]})', str(x))
            else:
                return func.replace(f'{op}(x)', str(x))

def resFunc(func, n):
    lista = ['log','sqrt','sen','cos']

    for i in range(len(lista)):
        if lista[i] in func:
            func = lssc(func, n, lista[i])

    func = re.split(r'\s*([-+*/])\s*', func.replace('x', '*'+str(n)))

    for i in range(0, len(func)):
        if func[i] == '':
            func[i] = '1'

        if func[i].find('^') != -1:
            exp = func[i].split('^')
            func[i] = f'{float(exp[0])**int(exp[1])}'

    return eval(''.join(map(str,func)))

def bissec(func, a, b, prec):
    if (b-a) > prec:
        cont = 1
        m = resFunc(func, a)

        print('{:^10}| {:^11} | {:^15} | {:^15}'.format('Iteração', 'x', 'f(x)', 'b-a'))

        while True:
            x = (a+b)/2
            fx = resFunc(func, x)

            if (m*fx) > 0:
                a = x
            else:
                b = x

            print(f'{cont:^10}| {x:.9f} | {fx:^15.8e} | {(b-a):^15.8e}')

            if (b-a) < prec:
                x = (a+b)/2
                break

            cont += 1
    else:
        x = (a+b)/2

    print(f'\nx = {x} em {cont} iterações.\n')
    
while True:
    func = input('Função (Ex: x^3-9x+3): ').replace(' ', '')
    a = float(input('Intervalo a: '))
    b = float(input('Intervalo b: '))
    prec = rcbPrec()

    bissec(func, a, b, prec)

    if input('Digite 0 p/ encerrar ou 1 p/ continuar: ') == '0':
        break
