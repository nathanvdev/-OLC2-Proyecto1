from ..abstract.variables import Variables


class Environment():
    def __init__(self, previus, name):  
        self.previus = previus
        self.name = name
        self.varibles = {}
        self.functions = {}
        self.arrays = {}
        self.interfaces = {}
        self.envsCount = 0

    def SaveVariable(self, newVar: Variables):
        if newVar.id_ in self.varibles:
            if self.varibles[newVar.id_].type != newVar.Type:
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
                return None
            self.varibles[newVar.id_] = newVar
            print(f'Variable updated: {newVar.id_}')
        else:
            self.varibles[newVar.id_] = newVar
            print(f'Variable saved: {newVar.id_}')

    def AssignVariable(self, name, op, value):
        env = self
        while env != None:
            if name in env.varibles:
                if env.varibles[name].const:
                    print(f'Error: Variable {name} is constant \n column: {self.column} line: {self.line}')
                    return
                if env.varibles[name].Type != value.Type:
                    print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
                    return
                if op == '=':
                    env.varibles[name].value = value
                    return
                elif op == '+=':
                    env.varibles[name].value.value += value.value
                    return
                elif op == '-=':
                    env.varibles[name].value.value -= value.value
                    return
                elif op == '*=':
                    env.varibles[name].value.value *= value.value
                    return
                elif op == '/=':
                    env.varibles[name].value.value /= value.value
                    return
            env = env.previus
        print(f'Error: Variable {name} not found \n column: {self.column} line: {self.line}')

    def ForceAssignVariable(self, name, op, value):
        env = self
        while env != None:
            if name in env.varibles:
                if env.varibles[name].Type != value.Type:
                    print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
                    return
                if op == '=':
                    env.varibles[name].value = value
                    return
                elif op == '+=':
                    env.varibles[name].value.value += value.value
                    return
                elif op == '-=':
                    env.varibles[name].value.value -= value.value
                    return
                elif op == '*=':
                    env.varibles[name].value.value *= value.value
                    return
                elif op == '/=':
                    env.varibles[name].value.value /= value.value
                    return
            env = env.previus
        print(f'Error: Variable {name} not found \n column: {self.column} line: {self.line}')


    def Get_Variable(self, name):
        env = self
        while env != None:
            if name in env.varibles:
                return env.varibles[name]
            env = env.previus
        print(f'Error: Variable {name} not found \n column: {self.column} line: {self.line}')
        return None
    
    def SaveArray(self, newArray):
        if newArray.id in self.arrays:
            print(f'Error: Array {newArray.id} already exists \n column: {self.column} line: {self.line}')
            return
        self.arrays[newArray.id] = newArray
        print(f'Array saved: {newArray.id}')

    def GetArray(self, name):
        env = self
        while env != None:
            if name in env.arrays:
                return env.arrays[name]
            env = env.previus
        print(f'Error: Array {name} not found \n column: {self.column} line: {self.line}')
        return None
    
    def SaveInterface(self, newInterface):
        if newInterface.id_ in self.interfaces:
            print(f'Error: Interface {newInterface.id_} already exists \n column: {self.column} line: {self.line}')
            return
        self.interfaces[newInterface.id_] = newInterface
        print(f'Interface saved: {newInterface.id_}')

    def  GetInterface(self, name):
        env = self
        while env != None:
            if name in env.interfaces:
                return env.interfaces[name]
            env = env.previus
        print(f'Error: Interface {name} not found \n column: {self.column} line: {self.line}')
        return None
