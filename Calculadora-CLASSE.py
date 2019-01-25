class Calculadora:

    @staticmethod
    def soma(n1, n2):
        return n1 + n2

    @staticmethod
    def subtracao(n1, n2):
        return n1 - n2

    @staticmethod
    def multiplicacao(n1, n2):
        return n1 * n2

    @staticmethod
    def divisao(n1, n2):
        return n1 / n2


resultado = Calculadora()


def main():
    print('\n' * 50)
    while True:
        print('')
        print('CALCULADORA\n')
        try:
            print()
            a = int(input('\nDigite o \033[32m' + 'PRIMEIRO' + '\033[0;0m' ' número: '))
        except ValueError:
            print('APENAS NÚMEROS')
            continue
        print()
        operador = input('Digite um NÚMERO e scolha o operador: '
                         '\n1 - Soma(+) '
                         '\n2 - Subtração(-)' ''
                         '\n3 - Multiplicação(x) '''
                         '\n4 - Divisão(/) '''
                         '\n\n5 - SAIR(\033[31m'+'s''\033[0;0m) '
                         '\n\n|--> ')
        op = operador
        if op == 's' or op == 'S':
            break
        if op != '1' and op != '2' and op != '3' and op != '4':
            continue

        try:
            b = int(input('\nDigite o \033[31m'+'SEGUNDO' + '\033[0;0m' ' número: '))
        except ValueError:
            print('APENAS NÚMERO')
            continue

        if op == '1':
            print('\nO resultado da SOMA é: ', resultado.soma(a, b))
        elif op == '2':
            print('\nO resultado da SUBTRAÇÃO é: ', resultado.subtracao(a, b))
        elif op == '3':
            print('\nO resultado da  MULTIPLICAÇÃO é: ', resultado.multiplicacao(a, b))
        elif op == '4':
            print('\nO resultado da DIVISÃO é: ', resultado.divisao(a, b))

main()
