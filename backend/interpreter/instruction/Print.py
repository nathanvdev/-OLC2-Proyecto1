from ..abstract.instruction import instruction
from ..abstract.array_ import Array_


class Print(instruction):
    def __init__(self, line, column, expression):
        super().__init__(line, column)
        self.expression = expression
        

    def Eject(self, env):
        
        globalenv = env.GetGlobal()
        toPrint = ""
        for exp in self.expression:
            result = exp.Eject(env)
            if isinstance(result, Array_):
                toPrint += "["
                for i in result.value:
                    toPrint += str(i.value) + ", "
                toPrint = toPrint[:-2]
                toPrint += "] "
                continue
            while hasattr(result.value, 'Eject'):
                result = result.value.Eject(env)
            while not isinstance(result.value, (int, float, str, bool)) and result.value != None:
                result = result.value
            toPrint += str(result.value) + str(result.Type) + " "

        globalenv.console += toPrint + "\n"
        return 