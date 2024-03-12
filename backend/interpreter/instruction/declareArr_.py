from ..abstract.instruction import instruction
from ..abstract.array_ import Array_

class DeclareArr_(instruction):
    def __init__(self, line, column, id_, Type, expression_list, const):
        super().__init__(line, column)
        self.id_ = id_
        self.Type = Type
        self.expression_list = expression_list
        self.const = const

    def Eject(self, env):
        Array = []
        count = 0
        for expression in self.expression_list:
            result = expression.Eject(env)
            if result.Type != self.Type:
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
                continue
            Array.append(result)
            count += 1
            

        newArray = Array_(self.id_, self.Type, Array, self.const)
        newArray.size = count

        env.SaveArray(newArray)
        