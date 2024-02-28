import ply.lex as lex
import ply.yacc as yacc

from ..environment.types import ExpressionType
from ..expression.primitive import Primitive
from ..instruction.Print import Print
from ..expression.aritmetic import Aritmetic
from ..expression.relational import Relational
from ..expression.logica import Logica


#palabras reservadas
reserved = {
    'console': 'CONSOLE',
    'log': 'LOG',
    'true': 'TRUE',
    'false': 'FALSE'
}

#lista de tokens
tokens = ['PARA', 'PARC', 'DOT', 'NUMBER', 'FLOAT', 'STRING', 
          'PLUS', 'LESS', 'BY', 'DIVIDED', 'MODUL',
          'EQUAL', 'DIFERENT','MINOR','MINOREQUAL','GREATER','GREATEREQUAL',
          'AND','OR','NOT'] + list(reserved.values())


#-----------------------------------------------------definicion de tokens
t_PARA = r'\('
t_PARC = r'\)'
t_DOT = r'\.'

###Aritmetica
t_PLUS = r'\+'
t_LESS = r'\-'
t_BY = r'\*'
t_DIVIDED = r'\/'
t_MODUL = r'\%'

##Relacionales
t_EQUAL = r'\=\='
t_DIFERENT = r'\!\='
t_MINOR = r'\<'
t_MINOREQUAL = r'\<\='
t_GREATER = r'\>'
t_GREATEREQUAL = r'\>\='

##Logicas
t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'\!'


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
    
##precedencia
precedence = (  
                ('left', 'OR'),
                ('left', 'AND'),
                ('left', 'NOT'),
                ('left', 'EQUAL', 'DIFERENT', 'MINOR', 'MINOREQUAL', 'GREATER', 'GREATEREQUAL'),
                ('left', 'PLUS', 'LESS'), 
                ('left', 'BY','DIVIDED', 'MODUL'), 
                ('right', 'UMENOS')
            )
    


##definicion de la gramatica
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
    '''expression : primitivo 
                  | aritmetica
                  | relacional
                  | logica'''

    p[0] = p[1]

def p_aritmetica(p):
    '''aritmetica : expression PLUS expression
                  | expression LESS expression
                  | expression BY expression
                  | expression DIVIDED expression
                  | expression MODUL expression
                  | LESS expression %prec UMENOS'''
    
    tmp = get_params(p)
    if p.slice[1].type == 'LESS':
        p[0] = Aritmetic(tmp.line, tmp.column, p[2], p[2], p[1])

    elif p.slice[2].type == 'PLUS':
        p[0] = Aritmetic(tmp.line, tmp.column, p[1], p[3], p[2])


    elif p.slice[2].type == 'LESS':
        p[0] = Aritmetic(tmp.line, tmp.column, p[1], p[3], p[2])

    elif p.slice[2].type == 'BY':
        p[0] = Aritmetic(tmp.line, tmp.column, p[1], p[3], p[2])

    elif p.slice[2].type == 'DIVIDED':
        p[0] = Aritmetic(tmp.line, tmp.column, p[1], p[3], p[2])

    elif p.slice[2].type == 'MODUL':
        p[0] = Aritmetic(tmp.line, tmp.column, p[1], p[3], p[2])

    elif p.slice[1].type == 'LESS':
        p[0] = Aritmetic(tmp.line, tmp.column, p[2], 0, p[1])


def p_relacional(p):
    '''relacional : expression EQUAL expression
                    | expression DIFERENT expression
                    | expression MINOR expression
                    | expression MINOREQUAL expression
                    | expression GREATER expression
                    | expression GREATEREQUAL expression'''
    
    tmp = get_params(p)

    if p.slice[2].type == 'EQUAL':
        p[0] = Relational(tmp.line, tmp.column, p[1], p[3], p[2])

    elif p.slice[2].type == 'DIFERENT':
        p[0] = Relational(tmp.line, tmp.column, p[1], p[3], p[2])

    elif p.slice[2].type == 'MINOR':
        p[0] = Relational(tmp.line, tmp.column, p[1], p[3], p[2])

    elif p.slice[2].type == 'MINOREQUAL':
        p[0] = Relational(tmp.line, tmp.column, p[1], p[3], p[2])

    elif p.slice[2].type == 'GREATER':
        p[0] = Relational(tmp.line, tmp.column, p[1], p[3], p[2])

    elif p.slice[2].type == 'GREATEREQUAL':
        p[0] = Relational(tmp.line, tmp.column, p[1], p[3], p[2])


def p_logica(p):
    '''logica : boolean AND boolean
              | boolean OR boolean
              | NOT boolean'''
    tmp = get_params(p)

    if p.slice[2].type == 'AND':
        p[0] = Logica(tmp.line, tmp.column, p[1], p[3], p[2])

    elif p.slice[2].type == 'OR':
        p[0] = Logica(tmp.line, tmp.column, p[1], p[3], p[2])

    elif p.slice[1].type == 'NOT':
        p[0] = Logica(tmp.line, tmp.column, p[2], p[2], p[1])

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
        p[0] = p[1]
    elif p[1] == 'false':
        p[0] = p[1]


def p_boolean(p):
    '''boolean : TRUE
               | FALSE'''

    tmp = get_params(p)

    if p[1] == 'true':
        p[0] = Primitive(tmp.line, tmp.column, True, ExpressionType.BOOLEAN)
    elif p[1] == 'false':
        p[0] = Primitive(tmp.line, tmp.column, False, ExpressionType.BOOLEAN)


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


