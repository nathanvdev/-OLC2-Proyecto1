from interpreter.analyzer import grammar


if __name__ == "__main__":
    input_text = 'console.log("hola mundo")'
    resultado = grammar.parse(input_text)