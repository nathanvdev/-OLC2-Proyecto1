
class Environment():
    def __init__(self, previus, name):  
        self.previus = previus
        self.name = name
        self.varibles = {}
        self.functions = {}
        self.envsCount = 0

    def SaveVariable(self, name, value):

        if name in self.varibles:
            if self.varibles[name].type != value.Type:
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
                return None
            self.varibles[name] = value
        else:
            self.varibles[name] = value

    def GetVariable(self, name):
        env = self
        while env != None:
            if name in env.varibles:
                return env.varibles[name]
            env = env.previus
        print(f'Variable not found {name} \n column: {self.column} line: {self.line}')
        return None
    
