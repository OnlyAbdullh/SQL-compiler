from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from sql_ast.ast_nodes.basic_nodes import CursorUpdateColumnsList, FetchIntoClauseList, UserVariable
from sql_ast.ast_nodes.cursor_nodes import DeclareCursorNode, CursorDefinitionNode, CursorUpdateClause, \
    DeallocateCursor, CloseCursor, OpenCursor, FetchRow


class CursorVisitor(SQLParserVisitor):

    def visitDeclare_cursor(self, ctx:SQLParser.Declare_cursorContext):
        cursor_name = ctx.cursor_name().getText()
        pre_cursor_option = ctx.pre_cursor_options().getText() if ctx.pre_cursor_options() else None
        cursor_definition = self.visit(ctx.cursor_definition())


        return DeclareCursorNode(cursor_name,pre_cursor_option, cursor_definition)


    def visitCursor_definition(self, ctx:SQLParser.Cursor_definitionContext):
        cursor_scope = ctx.cursor_scope().getText() if ctx.cursor_scope() else None
        cursor_scroll = ctx.cursor_scroll().getText() if ctx.cursor_scroll() else None
        cursor_type = ctx.cursor_type().getText() if ctx.cursor_type() else None
        cursor_concurrency = ctx.cursor_concurrency().getText() if ctx.cursor_concurrency() else None
        cursor_warning= ctx.cursor_warning().getText() if ctx.cursor_warning() else None
        cursor_for_clause = self.visit(ctx.cursor_for_clause())
        cursor_update_clause = self.visit(ctx.cursor_update_clause()) if ctx.cursor_update_clause() else None

        return CursorDefinitionNode(
            cursor_scope,
            cursor_scroll,
            cursor_type,
            cursor_concurrency,
            cursor_warning,
            cursor_for_clause,
            cursor_update_clause
        )

    def visitCursor_update_clause(self, ctx:SQLParser.Cursor_update_clauseContext):
        is_read_only = True if ctx.READ_ONLY() else False
        can_update = True if ctx.UPDATE() else False
        columns = self.visit(ctx.cursor_update_columns()) if ctx.cursor_update_columns() else None
        return CursorUpdateClause(is_read_only,can_update,columns)

    def visitCursor_update_columns(self, ctx:SQLParser.Cursor_update_columnsContext):
        return CursorUpdateColumnsList([self.visit(column) for column in ctx.full_column_name()])

    def visitOpen_cursor(self, ctx:SQLParser.Open_cursorContext):
        cursor_name = ctx.cursor_name().getText()
        return OpenCursor(cursor_name)

    def visitClose_cursor(self, ctx:SQLParser.Close_cursorContext):
        cursor_name = ctx.cursor_name().getText()
        return CloseCursor(cursor_name)

    def visitDeallocate_cursor(self, ctx:SQLParser.Deallocate_cursorContext):
        cursor_name = ctx.cursor_name().getText()
        return DeallocateCursor(cursor_name)

    def visitFetch_row(self, ctx:SQLParser.Fetch_rowContext):
        if ctx.fetch_direction():
            fd = ctx.fetch_direction()

            if fd.ABSOLUTE():
                direction = f"ABSOLUTE {fd.fetch_offset().getText()}"
            elif fd.RELATIVE():
                direction = f"RELATIVE {fd.fetch_offset().getText()}"
            else:
                direction = fd.getText()
        else:
            direction = None
        cursor_name = ctx.cursor_name().getText()
        fetch_into_clause_list = self.visit(ctx.fetch_into_clause()) if ctx.fetch_into_clause() else None
        return FetchRow(
            direction,
            cursor_name,
            fetch_into_clause_list
        )

    def visitFetch_into_clause(self, ctx:SQLParser.Fetch_into_clauseContext):
        return FetchIntoClauseList([UserVariable(var.getText()) for var in ctx.user_variable_list().USER_VARIABLE()])

