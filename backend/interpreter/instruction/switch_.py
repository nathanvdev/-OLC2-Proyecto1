from ..abstract.instruction import instruction
from ..abstract.types import ExpressionType

class Switch_(instruction):
    def __init__(self, line, column, expression_, cases_, default_):
        super().__init__(line, column)
        self.expression = expression_
        self.cases = cases_
        self.default = default_


    def Eject(self, env):
        globalenv = env.GetGlobal()
        for case in self.cases:
            instructions = case['instructions']
            if instructions[-1].Type != ExpressionType.BREAK:
                newError = {
                    "Tipo": "Semantico",
                    "Linea": instructions[-1].line,
                    "Columna": instructions[-1].column,
                    "Ambito": env.name,
                    "Descricion": "Error en el switch"
                }
                globalenv.Errors.append(newError)
                print(f'Error: Expected break statement \n column: {instructions[-1].column} line: {instructions[-1].line}')
                return
            
        value = self.expression.Eject(env)
        while hasattr(value.value, 'Eject'):
            value = value.value.Eject(env)
        result = None
        for case in self.cases:
            if case['expression'].Eject(env).value == value.value:
                instructions = case['instructions']
                for instruction in instructions:
                    result = instruction.Eject(env)

                    if result != None and hasattr(result, 'tmpType'):
                        if result.tmpType == ExpressionType.BREAK:
                            break
                        elif result.tmpType == ExpressionType.CONTINUE:
                            break
                        elif result.tmpType == ExpressionType.RETURN:
                            return result

            if result != None and hasattr(result, 'tmpType'):
                if result.tmpType == ExpressionType.BREAK:
                    return result
                elif result.tmpType == ExpressionType.RETURN:
                    return result
                
        for definstruct in self.default:
            result = definstruct.Eject(env)

            if result != None and hasattr(result, 'tmpType'):
                if result.tmpType == ExpressionType.BREAK:
                    break
                elif result.tmpType == ExpressionType.CONTINUE:
                    break
                elif result.tmpType == ExpressionType.RETURN:
                    return result

        if result != None and hasattr(result, 'tmpType'):
            if result.tmpType == ExpressionType.BREAK:
                return result
            elif result.tmpType == ExpressionType.RETURN:
                return result
            
        
            