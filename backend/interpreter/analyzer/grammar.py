import ply.lex as lex
import ply.yacc as yacc

from ..environment.types import ExpressionType
from ..expression.primitive import Primitive
from ..instruction.Print import Print


#palabras reservadas
reserved = {
    'console': 'CONSOLE',
    'log': 'LOG',
    'true': 'TRUE',
    'false': 'FALSE'
}

#lista de tokens
tokens = ['PARA', 'PARC', 'DOT', 'NUMBER', 'FLOAT', 'STRING'] + list(reserved.values())


#-----------------------------------------------------definicion de tokens
t_PARA = r'\('
t_PARC = r'\)'
t_DOT = r'\.'

t_CONSOLE = r'console'
t_LOG = r'log'
t_TRUE = r'true'
t_FALSE = r'false'

def t_FLOAT(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print(f'error al parsear el valor: {t.value}')
        t.value = None
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print(f'error al parsear el valor: {t.value}')
        t.value = None
    return t

def t_STRING(t):
    r'\"(.+?)\"'
    try:
        t.value = str(t.value).replace('"', '')
    except ValueError:
        print(f'error al parsear el valor: {t.value}')
        t.value = None
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(f'Error lexico {t.value}')
    t.lexer.skip(1) # recuperacion del error



#--------------------------------------------------definicion de la gramatica

def p_start(p):
    '''start : instrucciones '''
    p[0] = p[1]
    return p[0]
    


def p_instrucciones(p):
    '''instrucciones : instrucciones instruccion
                     | instruccion '''
    if 2 < len(p):
        p[1].append(p[2])
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    
def p_instruccion(p):
    '''instruccion : print '''
    p[0] = p[1]
    

def p_print(p):
    '''print : CONSOLE DOT LOG PARA expression PARC'''
    tmp = get_params(p)
    p[0] = Print(tmp.line, tmp.column, p[5])
    

def p_expression(p):
    '''expression : primitivo '''

    p[0] = p[1]

def p_primitivo(p):
    '''primitivo : NUMBER
                 | FLOAT
                 | STRING
                 | boolean'''

    tmp = get_params(p)

    if p.slice[1].type == 'NUMBER':
        p[0] = Primitive(tmp.line, tmp.column, p[1], ExpressionType.INTEGER)
    elif p.slice[1].type == 'FLOAT':
        p[0] = Primitive(tmp.line, tmp.column, p[1], ExpressionType.FLOAT)
    elif p.slice[1].type == 'STRING':
        p[0] = Primitive(tmp.line, tmp.column, p[1], ExpressionType.STRING)
    elif p[1] == 'true':
        p[0] = Primitive(tmp.line, tmp.column, True, ExpressionType.BOOLEAN)
    elif p[1] == 'false':
        p[0] = Primitive(tmp.line, tmp.column, False, ExpressionType.BOOLEAN)


def p_boolean(p):
    '''boolean : TRUE
               | FALSE'''

    p[0] = p[1]


def p_error(p):
    if p:
        print(f'Error sintactico linea:{p.lineno}, col: {p.lexpos}: Token {p.value}')
    else:
        print('Error de sintaxis')

class codeParams:
    def __init__(self, line, column):
        self.line = line
        self.column = column
        
def get_params(t):
    line = t.lexer.lineno  # Obtener la línea actual desde el lexer
    lexpos = t.lexpos if isinstance(t.lexpos, int) else 0  # Verificar si lexpos es un entero
    column = lexpos - t.lexer.lexdata.rfind('\n', 0, lexpos) 
    return codeParams(line, column)


def parse(input_text):
    lexer = lex.lex() #lexico
    parser = yacc.yacc() #sintactico

    print(f'-----------------------\ntexto de entrada:\n{input_text}\n-----------------------\n')
    result = parser.parse(input_text)
    return result


