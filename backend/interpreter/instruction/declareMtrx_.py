from ..abstract.instruction import instruction

class declareMtrx_(instruction):
    def __init__(self, line, column, id_, Type, size, value):
        super().__init__(line, column)
        self.id_ = id_
        self.Type = Type
        self.size = size
        self.value = value

    def Eject(self, env):
        pass