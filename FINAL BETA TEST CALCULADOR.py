def calculadora ():
    print("calculadora Beta Test")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")

    operacao = input("(+, -, *, /):")
    if operacao not in ['+','-','*','/']:
        return "operação invalida."
    num1 = float(input("número 1 : "))
    num2 = float(input("número 2 : "))

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 == 0:
            return "Ocorreu um erro: Divisão por zero."
        resultado = num1 / num2
    else:
        return " a Operação é inválida."
        resultado = {
            '+': num1 + num2, 
            '-': num1 - num2,
            '*': num1 * num2,
            '/': num1 / num2 
            }[operacao] 
    return f"Resultado: {resultado}"
   
    # loop ➰ de execução
    while True: 
        calculadora() 
        continuar = input("Deseja fazer outro cálculo? (s/n):  ") 
        if continuar.lower () != 's': 
            print("Encerrando o sistema. obg!")
            break  
            
# Executar a calculadora
print(calculadora())