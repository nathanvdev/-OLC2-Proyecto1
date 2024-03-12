from interpreter.abstract.environment import Environment
from interpreter.analyzer import grammar
import json

if __name__ == "__main__":
    input_text = '''const vec1:number[] = [10,20,30,40,50]\nvec1[1] = vec1[0]'''

    resultado = grammar.parse(input_text)

    GlobalEnvironment = Environment(None, 'Global')

    for instruction in resultado:
        instruction.Eject(GlobalEnvironment)

