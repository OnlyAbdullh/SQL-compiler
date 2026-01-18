from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from ..ast_nodes.basic_nodes import ItemsList, SingleValueNode, UserVariable
from ..ast_nodes.variable_nodes import DeclareVariableNode, ScalarVariableNode, CursorVariableNode, TableVariableNode


class VariableVisitor(SQLParserVisitor):
    def visitDeclare_var(self, ctx:SQLParser.Declare_varContext):
        var_list = self.visit(ctx.declare_var_list())
        return DeclareVariableNode(var_list)


    def visitDeclare_var_list(self, ctx:SQLParser.Declare_var_listContext):
         return ItemsList([self.visit(item) for item in ctx.declare_var_item()])

    def visitScalar_var(self, ctx:SQLParser.Scalar_varContext):
        user_var = UserVariable(ctx.USER_VARIABLE().getText())
        data_type = self.visit(ctx.datatype())
        expression = self.visit(ctx.expression()) if ctx.expression() else None
        return ScalarVariableNode(user_var, data_type, expression)


    def visitCursor_var(self, ctx:SQLParser.Cursor_varContext):
        user_var = UserVariable(ctx.USER_VARIABLE().getText())
        return CursorVariableNode(user_var)

    def visitTable_var(self, ctx:SQLParser.Table_varContext):
        user_var = UserVariable(ctx.USER_VARIABLE().getText())
        table_type = self.visit(ctx.table_type_definition())
        return TableVariableNode(user_var, table_type)










