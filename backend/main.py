from interpreter.abstract.environment import Environment
from interpreter.analyzer import grammar


if __name__ == "__main__":
    input_text = '''for(var i : number = 1; i <= 5; i++) {\n    console.log(i)\n}'''
    resultado = grammar.parse(input_text)

    GlobalEnvironment = Environment(None, 'Global')

    for instruction in resultado:
        instruction.Eject(GlobalEnvironment)
