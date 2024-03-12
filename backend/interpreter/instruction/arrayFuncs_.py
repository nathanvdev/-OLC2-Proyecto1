from ..abstract.instruction import instruction

class ArrayFuncs_(instruction):
    def __init__(self, line, column, id_, FuncType, expression):
        super().__init__(line, column)
        self.id_ = id_
        self.FuncType = FuncType
        self.expression = expression

    def Eject(self, env):
        tmp = env.GetArray(self.id_)
        if tmp == None:
            return
        
        elif tmp.const:
            print(f'Error: Array {self.id_} is constant \n column: {self.column} line: {self.line}')
            return
        
        elif self.FuncType == 'push':
            tmp.Push(self.expression.Eject(env))
            return

        elif self.FuncType == 'pop':
            return tmp.Pop()
        
        if self.FuncType == 'atoll':
            return tmp.IndexOf(self.expression.Eject(env))
        
        elif self.FuncType == 'join':
            return tmp.Join()
        
        elif self.FuncType == 'length':
            return tmp.Length()
        
        elif self.FuncType == 'Find':
            return tmp.Find(self.expression.Eject(env))
            