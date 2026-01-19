
from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from ..ast_nodes.basic_nodes import ItemsList
from ..ast_nodes.cte_nodes import *

class CteVisitor(SQLParserVisitor):

    def visitWith_cte(self, ctx:SQLParser.With_cteContext):
        return self.visit(ctx.common_table_expression_list())

    def visitCommon_table_expression_list(self, ctx:SQLParser.Common_table_expression_listContext):
        return ItemsList([self.visit(item_ctx) for item_ctx in ctx.common_table_expression()])

    def visitCommon_table_expression(self, ctx: SQLParser.Common_table_expressionContext):
        name = ctx.IDENTIFIER().getText()
        column_list = self.visit(ctx.column_list()) if ctx.column_list() else None
        query = self.visit(ctx.cte_query_definition_list())

        return CommonTableExpression(
            name=name,
            column_list=column_list,
            query=query
        )

    def visitCte_set_operators_select_statement(self, ctx:SQLParser.Cte_set_operators_select_statementContext):

        lst = []
        for i, st_op in enumerate(ctx.set_operators()):
            se = self.visit(ctx.select_statement(i))
            lst.append(SetSelectStatement(self.visit(st_op), se))
        return SetSelectStatementList(lst)