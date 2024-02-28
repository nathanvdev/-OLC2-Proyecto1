from interpreter.analyzer import grammar


if __name__ == "__main__":
    input_text = '''console.log(-6)'''
    resultado = grammar.parse(input_text)

    for instruction in resultado:
        instruction.Eject(None)
