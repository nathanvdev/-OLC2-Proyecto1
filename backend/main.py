from interpreter.abstract.environment import Environment
from interpreter.analyzer import grammar

import json

from flask import Flask, jsonify, request
from collections import OrderedDict
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

response = ""

@app.route('/')
def home():
    credenciales = OrderedDict()
    credenciales['Nombre'] = 'Nathan Antonio Valdez Valdez'
    credenciales['Carnet'] = '202001568'
    credenciales['Curso'] = 'Compiladores 2'
    env = json.dumps(credenciales)
    return env

@app.route('/send_command', methods=['POST'])
def send_command():


    code_in = request.json['code_in']
    print("\n\n-------------------------------------New Request-------------------------------------")
    print(code_in)
    print("_________________________________________________________________________________________")
    ast = grammar.parse(code_in)
    GlobalEnvironment = Environment(None, 'Global')

    for instruction in ast:
        instruction.Eject(GlobalEnvironment)
        
    pass


    return jsonify({'message': response})

if __name__ == "__main__":
    app.run(debug=True)













    # input_text = '''var vec1:number[] = [10,20,30,40,50]'''

    # resultado = grammar.parse(input_text)

    # GlobalEnvironment = Environment(None, 'Global')

    # for instruction in resultado:
    #     instruction.Eject(GlobalEnvironment)
    # pass

