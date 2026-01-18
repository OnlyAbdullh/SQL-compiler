from .ast_node import ASTNode
from .basic_nodes import ItemsList


class DeclareVariableNode(ASTNode):
    def __init__(self, var_list: ASTNode):
        self.var_list = var_list

    def print(self, spacer="  ", level=0):
        print(spacer*level + "Declared Variables List:") # this is data i want to print for my node
        self.var_list.print(spacer , level)


class ScalarVariableNode(ASTNode):
    def __init__(self, user_var , data_type , expression = None):
        self.user_var = user_var
        self.data_type = data_type
        self.expression = expression

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Scalar Variable:")
        self.user_var.print(spacer , level + 1)
        self.data_type.print(spacer , level + 1)
        if self.expression:
            self.expression.print(spacer , level + 1)

class CursorVariableNode(ASTNode):
    def __init__(self, user_var):
        self.user_var = user_var

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Cursor Variable:")
        self.user_var.print(spacer , level + 1)


class TableVariableNode(ASTNode):
    def __init__(self, user_var , table_type):
        self.user_var = user_var
        self.table_type = table_type

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Table Variable:")
        self.user_var.print(spacer , level + 1)
        self.table_type.print(spacer , level + 1)