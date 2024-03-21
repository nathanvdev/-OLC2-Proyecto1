from ..abstract.instruction import instruction
import main


class Print(instruction):
    def __init__(self, line, column, expression):
        super().__init__(line, column)
        self.expression = expression
        

    def Eject(self, env):
        toPrint = ""
        for exp in self.expression:
            result = exp.Eject(env)
            toPrint += str(result.value)

        main.response += toPrint + "\n"
        return 