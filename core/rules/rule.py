from core.board import Board
from core.update import Update

class Rule:
    rule_name = "Parent"
    
    def find_update(self, board):
        return Update(self.rule_name)
    
    def dedupe_eliminations(self, eliminations):
        deduped = []
        for i in range(len(eliminations)):
            dupe = False
            for j in range(i+1, len(eliminations)):
                if eliminations[i] == eliminations[j]:
                    dupe = True
            if not dupe:
                deduped.append(eliminations[i])
        return deduped

