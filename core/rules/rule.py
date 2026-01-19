from core.board import Board
from core.update import Update

class Rule:
    rule_name = "Parent"
    
    def find_update(self, board):
        return Update(self.rule_name)
