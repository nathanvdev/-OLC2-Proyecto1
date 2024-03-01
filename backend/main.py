from interpreter.abstract.environment import Environment
from interpreter.analyzer import grammar


if __name__ == "__main__":
    input_text = '''var valor1 : number = 50\nvar valor2 : number = 10\nif (valor1 < valor2) {\n     console.log(valor1*valor2)\n     valor1 += 1\n} else if (valor1 == valor2) {\n     console.log("son iguales")\n     valor1 -= 1\n console.log(valor1)\n} else {\n     console.log(valor1+valor2)\n     valor1 = 1}'''
    resultado = grammar.parse(input_text)

    GlobalEnvironment = Environment(None, 'Global')

    for instruction in resultado:
        instruction.Eject(GlobalEnvironment)
