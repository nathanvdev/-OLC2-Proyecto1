from interpreter.abtract.environment import Environment
from interpreter.analyzer import grammar


if __name__ == "__main__":
    input_text = '''var Variable_a : number = 5+20\nvar variable_b = 2+2\nvar _cvariable : float'''
    resultado = grammar.parse(input_text)

    GlobalEnvironment = Environment(None, 'Global')

    for instruction in resultado:
        instruction.Eject(GlobalEnvironment)
