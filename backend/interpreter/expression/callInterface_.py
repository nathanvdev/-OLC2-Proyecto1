from ..abstract.expression import expression
from ..expression.primitive import Primitive
from ..abstract.types import ExpressionType


class callInterface_(expression):
    def __init__(self, line, column, id, params):
        super().__init__(line, column)
        self.id = id
        self.params = params

    def Eject(self, env):
        Interface = env.Get_Variable(self.line, self.column, self.id)

        if self.params == 'keys':
            strtmp = "["
            for key in Interface.value.varibles:
                strtmp += key.id_ + ", "
            strtmp = strtmp[:-2] + "]"
            return Primitive(self.line, self.column, strtmp, ExpressionType.STRING)




        tmp = Interface.value.varibles
        if tmp[self.params] == None:
            return None
        return tmp[self.params]
        