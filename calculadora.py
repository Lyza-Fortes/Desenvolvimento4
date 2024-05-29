
#Faça uma função calculadora de dois números com três parâmetros: 
#os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. 
#Considera a seguinte definição:
#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 !=0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return 0
    
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
print("Digite qual operação quer fazer (1 - adicao; 2 - subtracao; 3 - multiplicação; 4 - divisão )")
operacao = int(input())

resultado = calculadora(num1, num2, operacao)
print(f"Resultado da operação escolhida: {resultado}")     