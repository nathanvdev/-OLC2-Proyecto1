from ..abstract.instruction import instruction
from ..abstract.environment import Environment
from ..abstract.variables import Variables


class DeclareInterface_(instruction):
    def __init__(self, line, column, id_, id2_, attributes):
        super().__init__(line, column)
        self.id_ = id_
        self.id2_ = id2_
        self.attributes = attributes


    def Eject(self, env: Environment):
        interface = env.GetInterface(self.id2_)
        if interface == None:
            print(f'Error: Interface {self.id2_} not found \n column: {self.column} line: {self.line}')
            return
        newEnv = Environment(None, 'INTERFACE_'+self.id_)

        for i in range(len(self.attributes)):
            id_param = list(interface.attributes[i].keys())[0]
            type_param = list(interface.attributes[i].values())[0]
            id_exp = list(self.attributes[i].keys())[0]
            valExp = list(self.attributes[i].values())[0].Eject(env)

            if type_param == valExp.Type and id_param == id_exp:

                newVar = Variables(id_param, type_param, valExp.value, False)
                newEnv.SaveVariable(newVar)

            else:
                print(f'Error: Type mismatch \n column: {self.column} line: {self.line}')
                return None
        
        newVar2 = Variables(self.id_, 'interface', newEnv, False)
        env.SaveVariable(newVar2)
