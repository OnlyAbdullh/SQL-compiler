from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from sql_ast.ast_nodes.delete_nodes import DeleteStatementNode


class DeleteVisitor(SQLParserVisitor):
    def visitDelete_statement(self, ctx:SQLParser.Delete_statementContext):
        with_cte = self.visit(ctx.with_cte()) if ctx.with_cte() else None
        top_clause = self.visit(ctx.top_clause()) if ctx.top_clause() else None
        table_source = self.visit(ctx.table_source())
        output_clause = self.visit(ctx.output_clause()) if ctx.output_clause() else None
        table_source_list = self.visit(ctx.table_source_list()) if ctx.table_source_list() else None
        delete_and_delete_where_clause = self.visit(ctx.delete_and_update_where_clause()) if ctx.delete_and_update_where_clause() else None

        return DeleteStatementNode(with_cte, top_clause, table_source, output_clause, table_source_list, delete_and_delete_where_clause)