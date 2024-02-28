from interpreter.analyzer import grammar


if __name__ == "__main__":
    input_text = '''console.log(true&&false)\nconsole.log(false||false)\nconsole.log(!true)'''
    resultado = grammar.parse(input_text)

    for instruction in resultado:
        instruction.Eject(None)
