import ply.lex as lex
import ply.yacc as yacc


#palabras reservadas
reserved = {
    'console': 'CONSOLE',
    'log': 'LOG',
}

#lista de tokens
tokens = ['PARA', 'PARC', 'DOT', 'STRING'] + list(reserved.values())


#definicion de tokens
t_CONSOLE = r'console'
t_LOG = r'log'
t_DOT = r'\.'
t_PARA = r'\('
t_PARC = r'\)'


def t_STRING(t):
    r'\"(.+?)\"'
    try:
        t.value = str(t.value)
    except ValueError:
        print(f'error al parsear el valor: {t.value}')
        t.value = ''
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(f'Error lexico {t.value}')
    t.lexer.skip(1) # recuperacion del error


def p_start(p):
    '''start : instrucciones '''

def p_instrucciones(p):
    '''instrucciones : instrucciones instruccion
                     | instruccion '''
    
def p_instruccion(p):
    '''instruccion : print '''

def p_print(p):
    '''print : CONSOLE DOT LOG PARA STRING PARC'''

    print(p[5])


def p_error(p):
    if p:
        print(f'Error sintactico linea:{p.lineno}, col: {p.lexpos}: Token {p.value}')
    else:
        print('Error de sintaxis')


def parse(input_text):
    lexer = lex.lex() #lexico
    parser = yacc.yacc() #sintactico

    print(input_text)
    result = parser.parse(input_text)
    return result