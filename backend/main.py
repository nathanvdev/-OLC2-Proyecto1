from interpreter.analyzer import grammar


if __name__ == "__main__":
    input_text = '''console.log(7)\nconsole.log(79.99)\nconsole.log("hola mundo")\nconsole.log(true)\nconsole.log(false)'''
    resultado = grammar.parse(input_text)

    for instruction in resultado:
        instruction.Eject(None)
