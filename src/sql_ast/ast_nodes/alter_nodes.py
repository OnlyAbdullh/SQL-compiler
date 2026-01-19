from symtable import Class

from .ast_node import ASTNode
from .basic_nodes import SingleValueNode, SingleExpressionNode


class AlterTableStatement(ASTNode):
    def __init__(self, table, action, alter_table=None):
        self.table = table
        self.action = action
        self.alter_table = alter_table

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Alter Table Statement:")
        self.table.print(spacer, level + 1)
        if self.alter_table:
            self.alter_table.print(spacer, level + 1)
        print(spacer * level + "Action : ")
        self.action.print(spacer, level + 1)


class AlterTableWithClause(ASTNode):
    def __init__(self, check=False):
        self.check = check

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Alter Table With Clause:")
        print(spacer * (level + 1) + f"Check: {self.check}")


class TableChangeTracking(ASTNode):
    def __init__(self, enabled, change_with=None):
        self.enabled = enabled
        self.change_with = change_with

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Table Change Tracking:")
        print(spacer * (level + 1) + f"Enabled: {self.enabled}")
        if self.change_with:
            print(spacer * (level + 1) + "Change With:")
            self.change_with.print(spacer, level + 2)


class OptionOnOff(ASTNode):
    def __init__(self, on):
        self.on = on

    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Option {"ON" if self.on else "OFF"}")


class ChangeTrackingWithClause(OptionOnOff):
    def print(self, spacer="  ", level=0):
        # TODO : FORMAT
        print(spacer * level + f"WITH TRACK COLUMNS UPDATED : {"ON" if self.on else "OFF"}")


class SetTableOption(ASTNode):
    def __init__(self, options_list):
        self.options_list = options_list

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Set Table Options:")
        self.options_list.print(spacer, level + 1)


class TableOptionLeaf(SingleValueNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Lock Escalation : {self.value}")


class AlterTableColumn(ASTNode):
    def __init__(self, column, action):
        self.column = column
        self.action = action

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Alter Table Column:", end="")
        self.column.print("", 0)
        print()
        self.action.print(spacer, level + 1)


class AlterColumnType(ASTNode):
    def __init__(self, col_type, collate, encrypted_with, nullable, sparse, alter_with_clause):
        self.col_type = col_type
        self.collate = collate
        self.encrypted_with = encrypted_with
        self.nullable = nullable
        self.sparse = sparse
        self.alter_with_clause = alter_with_clause

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Alter :")
        self.col_type.print(spacer, level + 2)
        if self.collate:
            print(spacer * (level + 1) + "Collate:")
            self.collate.print(spacer, level + 2)
        if self.encrypted_with:
            print(spacer * (level + 1) + "Encrypted With:")
            self.encrypted_with.print(spacer, level + 2)
        self.nullable.print(spacer, level + 1)
        print(spacer * (level + 1) + f"Sparse: {self.sparse}")
        if self.alter_with_clause:
            print(spacer * (level + 1) + "Alter With Clause:")
            self.alter_with_clause.print(spacer, level + 2)


class CollateClause(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Collate :")
        self.expression.print("", 0)
        print()


class AlterColumnOptionAction(ASTNode):
    def __init__(self, add_or_drop, option):
        self.option = option
        self.add_or_drop = add_or_drop

    def print(self, spacer="  ", level=0):
        print(spacer * level + self.add_or_drop + " Option: ")
        self.option.print(spacer, level + 1)


class AlterColumnOptionLeaf(SingleValueNode):
    pass


class TableAddItem(SingleExpressionNode):
    def print(self, spacer="  ", level=0):
        print(spacer * level + "Add To Table:")
        self.expression.print(spacer, level + 1)


class TableRenameColumn(ASTNode):
    def __init__(self, old_column_name, new_column_name):
        self.old_column_name = old_column_name
        self.new_column_name = new_column_name

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Rename Column:")
        print(spacer * (level + 1) + f"Old Column Name:")
        self.old_column_name.print(spacer, level + 1)
        print(spacer * (level + 1) + f"New Column Name: {self.new_column_name}")


class TableCheckConstraint(ASTNode):
    def __init__(self, constraint_target, check=True, ):
        self.constraint_target = constraint_target
        self.check = check

    def print(self, spacer="  ", level=0):
        print(spacer * level + ("Check:" if self.check else "No Check:") + f" {self.constraint_target}")


class DropTableConstraintWith(ASTNode):
    def __init__(self, constraint_name, drop_with=None):
        self.constraint_name = constraint_name
        self.drop_with = drop_with

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Drop From Table:")
        print(spacer * (level + 1) + f"Constraint Name: {self.constraint_name}")
        if self.drop_with:
            print(spacer * (level + 1) + "Drop With:")
            self.drop_with.print(spacer, level + 2)


class DropTableItems(ASTNode):
    def __init__(self, items=None):
        self.items = items

    def print(self, spacer="  ", level=0):
        print(spacer * level + "Drop ")
        if self.items:
            self.items.print(spacer, level + 1)


class DropConstraintSpec(ASTNode):
    def __init__(self, constraint_list, if_exists, drop_with_clause):
        self.constraint_list = constraint_list
        self.if_exists = if_exists
        self.drop_with_clause = drop_with_clause

    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Drop Constraints{" If Exists" if self.if_exists else ""}:")
        self.constraint_list.print(spacer, level + 1)
        if self.drop_with_clause:
            print(spacer * (level + 1) + "Drop With:")
            self.drop_with_clause.print(spacer, level + 2)

class DropColumnSpec(ASTNode):
    def __init__(self, column_list, if_exists):
        self.column_list = column_list
        self.if_exists = if_exists


    def print(self, spacer="  ", level=0):
        print(spacer * level + f"Drop Columns{" If Exists" if self.if_exists else ""}:")
        self.column_list.print(spacer, level + 1)