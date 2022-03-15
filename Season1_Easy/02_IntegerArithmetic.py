try: 
    a_input = int(input())
    b_input = int(input())
    operator_input = input()
    if operator_input== '+':
        result = a_input + b_input
    elif operator_input== '-':
        result = a_input - b_input
    elif operator_input== '*':
        result = a_input * b_input
    elif operator_input== '/':
        result = int(a_input / b_input)
    elif operator_input== '//':
        result = a_input // b_input
    elif operator_input== '%':
        result = a_input % b_input
    else:
        result = a_input ** b_input
    strings = f'{a_input}{operator_input}{b_input}={result}'
    print(strings)
except ZeroDivisionError:
    print('ERROR')