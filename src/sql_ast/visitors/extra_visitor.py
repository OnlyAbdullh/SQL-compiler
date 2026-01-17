
from generated.SQLParser import SQLParser
from generated.SQLParserVisitor import SQLParserVisitor

class ExtraVisitor(SQLParserVisitor):
    def visitUser_variable(self, ctx:SQLParser.User_variableContext):
        return ctx.USER_VARIABLE().getText()

    def visitIdentifier(self, ctx:SQLParser.IdentifierContext):
        return ctx.IDENTIFIER().getText()