from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor
from ..ast_nodes.statements import *
from ..ast_nodes.expressions import *
from ..ast_nodes.basic_nodes import *
from ..ast_nodes.cursor_nodes import CursorName


class CursorVisitor(SQLParserVisitor):

    def visitCursor_name(self, ctx: SQLParser.Cursor_nameContext):
        if ctx.user_variable():
            return CursorName(name=self.visit(ctx.user_variable()).getText())

        return CursorName(
            name=self.visit(ctx.identifier()),
            is_global=ctx.GLOBAL() is not None
        )
