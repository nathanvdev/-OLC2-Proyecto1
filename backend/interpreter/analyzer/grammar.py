import ply.lex as lex
import ply.yacc as yacc

from ..abstract.types import ExpressionType
from ..expression.primitive import Primitive
from ..instruction.Print import Print
from ..expression.aritmetic import Aritmetic
from ..expression.relational import Relational
from ..expression.logica import Logica
from ..instruction.declarate import Declarate
from ..instruction.assign import Assign
from ..instruction.find_variable import FindVariable
from ..instruction.if_else import If_else

#palabras reservadas
reserved = {
    'console': 'CONSOLE',
    'log': 'LOG',
    'true': 'TRUE',
    'false': 'FALSE',
    'var': 'RVAR',
    'const': 'RCONST',
    'number': 'RNUMBER',
    'float': 'RFLOAT',
    'string': 'RSTRING',
    'boolean': 'RBOOLEAN',
    'if' : 'RIF',
    'else' : 'RELSE',
}

#lista de tokens
tokens = ['PARA', 'PARC', 'DOT', 'DOUBLEDOT', 'LLAVEA', 'LLAVEC',
          'NUMBER', 'FLOAT', 'STRING', 'ID',
          'PLUS', 'LESS', 'BY', 'DIVIDED', 'MODUL',
          'EQUAL','DEQUAL','DIFERENT','MINOR','MINOREQUAL','GREATER','GREATEREQUAL',
          'AND','OR','NOT'] + list(reserved.values())


#-----------------------------------------------------definicion de tokens
t_PARA = r'\('
t_PARC = r'\)'
t_DOT = r'\.'
t_DOUBLEDOT = r'\:'
t_LLAVEA = r'\{'
t_LLAVEC = r'\}'

###Aritmetica
t_PLUS = r'\+'
t_LESS = r'\-'
t_BY = r'\*'
t_DIVIDED = r'\/'
t_MODUL = r'\%'

##Relacionales
t_DEQUAL = r'\=\='
t_EQUAL = r'\='
t_DIFERENT = r'\!\='
t_MINOR = r'\<'
t_MINOREQUAL = r'\<\='
t_GREATER = r'\>'
t_GREATEREQUAL = r'\>\='

##Logicas
t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'\!'




def t_FLOAT(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print(f'error al parsear el valor: {t.value} \n column: {t.lexpos} line: {t.lineno}')
        t.value = None
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print(f'error al parsear el valor: {t.value} \n column: {t.lexpos} line: {t.lineno}')
        t.value = None
    return t

def t_STRING(t):
    r'\"(.+?)\"'
    try:
        t.value = str(t.value).replace('"', '')
    except ValueError:
        print(f'error al parsear el valor: {t.value} \n column: {t.lexpos} line: {t.lineno}')
        t.value = None
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(),'ID')
    return t

t_ignore = " \t"

t_ignore_COMMENTLINE = r'\/\/.*'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(f'Error lexico {t.value} \n column: {t.lexpos} line: {t.lineno}')
    t.lexer.skip(1) # recuperacion del error



#--------------------------------------------------definicion de la gramatica
    
##precedencia
precedence = (  
                ('left', 'OR'),
                ('left', 'AND'),
                ('left', 'NOT'),
                ('left', 'DEQUAL', 'DIFERENT', 'MINOR', 'MINOREQUAL', 'GREATER', 'GREATEREQUAL'),
                ('left', 'PLUS', 'LESS'), 
                ('left', 'BY','DIVIDED', 'MODUL'), 
                ('right', 'UMENOS')
            )
    


##definicion de la gramatica
def p_start(p):
    '''start    : instrucciones '''
    p[0] = p[1]
    return p[0]
    


def p_instrucciones(p):
    '''instrucciones    : instrucciones instruccion
                        | instruccion '''
    if len(p) > 2:
        p[1].append(p[2])
        p[0] = p[1]
    else:
        p[0] = [p[1]]

    
def p_instruccion(p):
    '''instruccion  : print
                    | declare
                    | declareConst
                    | assignVar
                    | if_else'''
    p[0] = p[1]


def p_print(p):
    '''print    : CONSOLE DOT LOG PARA expression PARC'''
    tmp = get_params(p)
    p[0] = Print(tmp.line, tmp.column, p[5])

def p_declare(p):
    
    '''declare  : RVAR ID DOUBLEDOT type EQUAL expression
                | RVAR ID EQUAL expression
                | RVAR ID DOUBLEDOT type'''
    
    tmp = get_params(p)
    if len(p) == 7:
        p[0] = Declarate(tmp.line, tmp.column, p[2], p[4], p[6], False)

    elif p[3] =="=" :
        p[0] = Declarate(tmp.line, tmp.column, p[2], None, p[4], False)

    elif p[3] ==":" : 
        p[0] = Declarate(tmp.line, tmp.column, p[2], p[4], None, False)

def p_declareConst(p):
    '''declareConst : RCONST ID DOUBLEDOT type EQUAL expression
                    | RCONST ID EQUAL expression
                    | RCONST ID DOUBLEDOT type'''
    
    tmp = get_params(p)
    if len(p) == 7:
        p[0] = Declarate(tmp.line, tmp.column, p[2], p[4], p[6], True)

    elif p[3] =="=" :
        p[0] = Declarate(tmp.line, tmp.column, p[2], None, p[4], True)

    elif p[3] ==":" : 
        p[0] = Declarate(tmp.line, tmp.column, p[2], p[4], None, True)

def p_assignVar(p):
    '''assignVar    : ID EQUAL expression
                    | ID PLUS EQUAL expression
                    | ID LESS EQUAL expression'''
    
    tmp = get_params(p)
    if p[2] == '=':
        p[0] = Assign(tmp.line, tmp.column, p[1], '=', p[3])
    elif p[2] == '+':
        p[0] = Assign(tmp.line, tmp.column, p[1], '+=', p[4])
    elif p[2] == '-':
        p[0] = Assign(tmp.line, tmp.column, p[1], '-=', p[4])

def p_if_else(p):
    '''if_else  : RIF PARA expression PARC LLAVEA instrucciones LLAVEC else'''

    tmp = get_params(p)
    p[0] = If_else(tmp.line, tmp.column, p[3], p[6], p[8])
    
def p_else(p):
    '''else : RELSE LLAVEA instrucciones LLAVEC
            | RELSE if_else
            |'''
    
    if len(p) == 5:
        p[0] = p[3]
    elif len(p) == 3:
        p[0] = [p[2]]
    else:
        p[0] = None


    # if len(p) == 5:
    #     p[0] = [p[1]]
    # elif len(p) == 3:
    #     p[1].append(p[2])
    #     p[0] = p[1]
    # else:


def p_expression(p):
    '''expression   : primitivo 
                    | aritmetica
                    | relacional
                    | logica
                    | ID'''
    
    tmp = get_params(p)
    if p.slice[1].type == 'ID':
        p[0] = FindVariable(tmp.line, tmp.column, p[1])
    else:
        p[0] = p[1]


def p_aritmetica(p):
    '''aritmetica   : expression PLUS expression
                    | expression BY expression
                    | expression DIVIDED expression
                    | expression LESS expression
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
    '''relacional   : expression DEQUAL expression
                    | expression DIFERENT expression
                    | expression MINOR expression
                    | expression MINOREQUAL expression
                    | expression GREATER expression
                    | expression GREATEREQUAL expression'''
    
    tmp = get_params(p)

    if p.slice[2].type == 'DEQUAL':
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
    '''logica   : boolean AND boolean
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
    '''primitivo    : NUMBER
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
    else:
        p[0] = p[1]


def p_boolean(p):
    '''boolean  : TRUE
                | FALSE'''

    tmp = get_params(p)

    if p[1] == 'true':
        tmp = Primitive(tmp.line, tmp.column, True, ExpressionType.BOOLEAN)
        p[0] = Primitive(tmp.line, tmp.column, True, ExpressionType.BOOLEAN)
    elif p[1] == 'false':
        p[0] = Primitive(tmp.line, tmp.column, False, ExpressionType.BOOLEAN)

def p_type(p):
    '''type     : RNUMBER
                | RFLOAT
                | RSTRING
                | RBOOLEAN'''
    
    if p[1] == 'number':
        p[0] = ExpressionType.INTEGER
    elif p[1] == 'float':
        p[0] = ExpressionType.FLOAT
    elif p[1] == 'string':
        p[0] = ExpressionType.STRING
    elif p[1] == 'boolean':
        p[0] = ExpressionType.BOOLEAN



def p_error(p):
    if p:
        print(f'Error sintactico linea:{p.lineno}, col: {p.lexpos}: Token {p.value}')
    else:
        print(f'Error de sintaxis  \n column: {p.lexpos} line: {p.lineno}')

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


