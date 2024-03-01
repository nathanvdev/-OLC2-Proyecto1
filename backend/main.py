from interpreter.abtract.environment import Environment
from interpreter.analyzer import grammar


if __name__ == "__main__":
    input_text = '''var valor1 : number = 1\nvalor1 = valor1 + 5\nconsole.log(valor1)\nvar valor2 : string = "hola mundo"\nvalor2 += " desde python" \nconsole.log(valor2)'''
    resultado = grammar.parse(input_text)

    GlobalEnvironment = Environment(None, 'Global')

    for instruction in resultado:
        instruction.Eject(GlobalEnvironment)
