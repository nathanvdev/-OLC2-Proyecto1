from ..abstract.instruction import instruction

class ModifyInterface_(instruction):
    def __init__(self, line, column, id_, id2_, expression):
        super().__init__(line, column)
        self.id_ = id_
        self.id2_ = id2_
        self.expression = expression

    def Eject(self, env):
        globalenv = env.GetGlobal()
        Object = env.Get_Variable(self.line, self.column, self.id_)
        if Object == None:
            newError = {
                "Tipo": "Semantico",
                "Linea": self.line,
                "Columna": self.column,
                "Ambito": env.name,
                "Descricion": "Error en la modificacion de la interfaz"
            }
            globalenv.Errors.append(newError)
            print(f'Error: Object {self.id_} not found \n column: {self.column} line: {self.line}')
            return
        if Object.Type != 'interface':
            newError = {
                "Tipo": "Semantico",
                "Linea": self.line,
                "Columna": self.column,
                "Ambito": env.name,
                "Descricion": "Error en la modificacion de la interfaz"
            }
            globalenv.Errors.append(newError)
            print(f'Error: {self.id_} is not an interface \n column: {self.column} line: {self.line}')
            return
        
        Attributes = Object.value
        Attributes = Attributes.varibles

        if self.id2_ not in Attributes:
            newError = {
                "Tipo": "Semantico",
                "Linea": self.line,
                "Columna": self.column,
                "Ambito": env.name,
                "Descricion": "Error en la modificacion de la interfaz"
            }
            globalenv.Errors.append(newError)
            print(f'Error: Attribute {self.id2_} not found \n column: {self.column} line: {self.line}')
            return
        self.expression = self.expression.Eject(env)
        
        if Attributes[self.id2_].Type != self.expression.Type:
            newError = {
                "Tipo": "Semantico",
                "Linea": self.line,
                "Columna": self.column,
                "Ambito": env.name,
                "Descricion": "Error en la modificacion de la interfaz"
            }
            globalenv.Errors.append(newError)
            print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
            return
        
        Attributes[self.id2_].value = self.expression.value
        print(f'Attribute {self.id2_} modified successfully')
        return
            


    