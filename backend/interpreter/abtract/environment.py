from ..abtract.variables import Variables


class Environment():
    def __init__(self, previus, name):  
        self.previus = previus
        self.name = name
        self.varibles = {}
        self.functions = {}
        self.envsCount = 0

    def SaveVariable(self, newVar: Variables):

        if newVar.id in self.varibles:
            if self.varibles[newVar.id].type != newVar.Type:
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
                return None
            self.varibles[newVar.id] = newVar
            print(f'Variable updated: {newVar.id}')
        else:
            self.varibles[newVar.id] = newVar
            print(f'Variable saved: {newVar.id} tipo de variable: {newVar.Type} valor: {newVar.value.value} tipo de valor: {newVar.value.Type} Es Constante: {newVar.const}')

    def AssignVariable(self, name, op, value):

        if name in self.varibles:
            if self.varibles[name].const:
                print(f'Error: Cannot assign a value to a constant variable \n column: {self.column} line: {self.line}')
                return
            
            if self.varibles[name].Type != value.Type:
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
                return
            
            if op == '=':
                self.varibles[name].value = value

            elif op == '+=':
                self.varibles[name].value.value += value.value

            elif op == '-=':
                self.varibles[name].value.value -= value.value
            
            print(f'Variable updated: {name}')

    def Get_Variable(self, name):
        env = self
        while env != None:
            if name in env.varibles:
                return env.varibles[name]
            env = env.previus
        print(f'Error: Variable {name} not found \n column: {self.column} line: {self.line}')
        return None