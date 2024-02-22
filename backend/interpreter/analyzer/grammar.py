import ply.lex as lex
import ply.yacc as yacc


#palabras reservadas
reserved = {
    'console': 'CONSOLE',
    'log': 'LOG',
}

#lista de tokens
tokens = ['PARA', 'PARC', 'DOT', 'STRING', 'NUMBER', 'FLOAT', 'BOOLEAN', 'CHAR'] + list(reserved.values())


#-----------------------------------------------------definicion de tokens
t_PARA = r'\('
t_PARC = r'\)'
t_CONSOLE = r'console'
t_LOG = r'log'
t_DOT = r'\.'

def t_CHAR(t):
    r'[^\t\n\r\f ]'
    t.type = reserved.get(t.value, 'CHAR')
    return 


def t_BOOLEAN(t):
    r'true|false'
    print(f'valor booleano: {t.value}')
    if t.value == 'true':
        t.value = True
    else:
        t.value = False
    return t


def t_STRING(t):
    r'\"(.+?)\"'
    try:
        t.value = str(t.value)
    except ValueError:
        print(f'error al parsear el valor: {t.value}')
        t.value = None
    return t

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


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(f'Error lexico {t.value}')
    t.lexer.skip(1) # recuperacion del error



#--------------------------------------------------definicion de la gramatica

def p_start(p):
    '''start : instrucciones '''

def p_instrucciones(p):
    '''instrucciones : instrucciones instruccion
                     | instruccion '''
    
def p_instruccion(p):
    '''instruccion : print '''

def p_print(p):
    '''print : CONSOLE DOT LOG PARA EXPRESSION PARC'''
    print(p[5])

def p_expression(p):
    '''EXPRESSION : PRIMITIVO '''

    p[0] = p[1]

def p_primitivo(p):
    '''PRIMITIVO : STRING 
                 | NUMBER 
                 | FLOAT
                 | BOOLEAN
                 | CHAR'''

    p[0] = p[1]


def p_error(p):
    if p:
        print(f'Error sintactico linea:{p.lineno}, col: {p.lexpos}: Token {p.value}')
    else:
        print('Error de sintaxis')


def parse(input_text):
    lexer = lex.lex() #lexico
    parser = yacc.yacc() #sintactico

    print(f'texto de entrada: {input_text}')
    result = parser.parse(input_text)
    return result