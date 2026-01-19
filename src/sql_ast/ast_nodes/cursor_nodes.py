from typing import Optional

from sql_ast.ast_nodes.ast_node import ASTNode


class DeclareCursorNode(ASTNode):

    def __init__(self, cursor_name, pre_cursor_option: Optional, cursor_definition):
        self.cursor_name = cursor_name
        self.pre_cursor_option = pre_cursor_option
        self.cursor_definition = cursor_definition

    def print(self, spacer="  ", level=0):
        print(spacer*level+"Declare Cursor:")
        print(spacer*(level+1)+"Cursor Name:",self.cursor_name)

        if  self.pre_cursor_option:
            print(spacer*(level+1)+"Cursor Option:", self.pre_cursor_option)

        if self.cursor_definition:
            self.cursor_definition.print(spacer, level+1)



class CursorDefinitionNode(ASTNode):
    def __init__(self,
                 cursor_scope: Optional,
                 cursor_scroll: Optional,
                 cursor_type: Optional,
                 cursor_concurrency: Optional,
                 cursor_warning: Optional,
                 cursor_for_clause,
                 cursor_update_clause: Optional
                 ):
        self.cursor_scope = cursor_scope
        self.cursor_scroll = cursor_scroll
        self.cursor_type = cursor_type
        self.cursor_concurrency = cursor_concurrency
        self.cursor_warning = cursor_warning
        self.cursor_for_clause = cursor_for_clause
        self.cursor_update_clause = cursor_update_clause

    def print(self, spacer="  ", level=0):
        print(spacer*level+"Definition:")
        if self.cursor_scope:
            print(spacer*(level+1)+"Scope:", self.cursor_scope)
        if self.cursor_scroll:
            print(spacer*(level+1)+"Scroll:", self.cursor_scroll)
        if self.cursor_type:
            print(spacer*(level+1)+"Type:" ,self.cursor_type)
        if self.cursor_concurrency:
            print(spacer*(level+1)+"Concurrency:", self.cursor_concurrency)
        if self.cursor_warning:
            print(spacer*(level+1)+"Warning:", self.cursor_warning)

        print(spacer*(level+1)+"For:")
        self.cursor_for_clause.print(spacer,level+2)

        if self.cursor_update_clause:
            self.cursor_update_clause.print(spacer, level+1)

class CursorUpdateClause(ASTNode):
    def __init__(self,is_read_only,can_update,columns : Optional):
        self.is_read_only = is_read_only
        self.can_update = can_update
        self.columns = columns

    def print(self, spacer="  ", level=0):
        print(spacer*level+"Update:")
        print(spacer*(level+1)+"Read Only:" ,self.is_read_only)
        if self.can_update:
            print(spacer*(level+1)+"For UPDATE:",self.can_update)
            if self.columns:
                print(spacer*(level+2)+"Columns:")
                self.columns.print(spacer,level+3)


class OpenCursor(ASTNode):
    def __init__(self, cursor_name):
        self.cursor_name = cursor_name

    def print(self, spacer="  ", level=0):
        print(spacer*level+"Open:")
        print(spacer*(level+1)+"Cursor:", self.cursor_name)

class CloseCursor(ASTNode):
    def __init__(self, cursor_name):
        self.cursor_name = cursor_name

    def print(self, spacer="  ", level=0):
        print(spacer*level+"Close:")
        print(spacer*(level+1)+"Cursor:", self.cursor_name)


class DeallocateCursor(ASTNode):
    def __init__(self, cursor_name):
        self.cursor_name = cursor_name

    def print(self, spacer="  ", level=0):
        print(spacer*level+"Deallocate:")
        print(spacer*(level+1)+"Cursor:", self.cursor_name)

class FetchRow(ASTNode):
    def __init__(self, direction: Optional, cursor_name, fetch_into_clause_list: Optional):
        self.direction = direction
        self.cursor_name = cursor_name
        self.fetch_into_clause_list = fetch_into_clause_list

    def print(self, spacer="  ", level=0):
        print(spacer*level+"Fetch Cursor:")
        if self.direction:
            print(spacer*(level+1)+"Direction:", self.direction)
        print(spacer*(level+1)+"Cursor name:", self.cursor_name)
        if self.fetch_into_clause_list:
            print(spacer*(level+1)+"Fetch into:")
            self.fetch_into_clause_list.print(spacer, level+2)









