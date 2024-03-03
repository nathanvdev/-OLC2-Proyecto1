from ..abstract.instruction import instruction
from ..abstract.environment import Environment
from ..instruction.assign import Assign
from ..expression.primitive import Primitive
from ..abstract.types import ExpressionType
import copy

class for_(instruction):
    def __init__(self, line, column, assignment, condition, evalue, op, instructions):
        super().__init__(line, column)
        self.assignment = assignment
        self.condition = condition
        self.evalue = evalue
        self.op = op
        self.instructions = instructions

        
                # for (var i: number = 1; i <= 5; i++) {
                #       var                cnd    evl  inc
  
                #   console.log(i);
                # }

    def Eject(self, env:Environment):
        env.envsCount += 1
        newEnv = Environment(env, f'{env.envsCount}-for')

        self.assignment.const = True
        self.assignment.Eject(newEnv)

        cycleCount = 0
        while True:
            cycleCount += 1
            if self.condition.Eject(newEnv).value != True:
                return
            
            if cycleCount > 1000:
                print('Error: Infinite loop')
                return
            
            for instruction in self.instructions:
                instruction.Eject(newEnv)

            if self.op == '+':
                newEnv.ForceAssignVariable(self.evalue.name, '+=', Primitive(self.line, self.column, 1, ExpressionType.INTEGER))
            elif self.op == '-':
                newEnv.ForceAssignVariable(self.evalue.name, '-=', Primitive(self.line, self.column, 1, ExpressionType.INTEGER))
            




        