from ..abstract.instruction import instruction
from ..abstract.environment import Environment
from ..abstract.types import ExpressionType
from ..abstract.variables import Variables

class CallFunction_(instruction):   
    def __init__(self, line, column, id_, params):
        super().__init__(line, column)
        self.id_ = id_
        self.params = params
        
    def Eject(self, env):
        globalenv = env.GetGlobal()
        function = env.GetFunction(self.id_)
        if function is None:
            return None
        
        if len(function.params) != len(self.params):
            newError = {
                "Tipo": "Semantico",
                "Linea": self.line,
                "Columna": self.column,
                "Ambito": env.name,
                "Descricion": "Error en la cantidad de parametros"
            }
            globalenv.Errors.append(newError)
            print(f'Error: Number of parameters does not match \n column: {self.column} line: {self.line}')
            return None
        
        env.envsCount += 1
        newEnv = Environment(env, f'{env.envsCount}-{self.id_}-Function')
        for i in range(len(self.params)):
            param = function.params[i]
            paramValue = self.params[i].Eject(env)
            if param['Type'] != paramValue.Type:
                newError = {
                    "Tipo": "Semantico",
                    "Linea": self.line,
                    "Columna": self.column,
                    "Ambito": env.name,
                    "Descricion": "Error de tipo en los parametros"
                }
                globalenv.Errors.append(newError)
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
                return None
            if isinstance(paramValue.value, list):
                newArray = paramValue
                newArray.id = param['id_']
                newEnv.SaveArray(self.line, self.column, newArray)
            else:
                newVar = Variables(self.line, self.column, param['id_'], param['Type'], paramValue.value, False)
                newEnv.SaveVariable(newVar)
        
        for instruction in function.instructions:
            result = instruction.Eject(newEnv)
            if result != None and hasattr(result, 'tmpType'):
                if result.tmpType == ExpressionType.BREAK:
                    break
                elif result.tmpType == ExpressionType.CONTINUE:
                    break
                elif result.tmpType == ExpressionType.RETURN:
                    return result

        if result != None and hasattr(result, 'tmpType'):
            if result.tmpType == ExpressionType.BREAK:
                return
            elif result.tmpType == ExpressionType.RETURN:
                return result
        return None