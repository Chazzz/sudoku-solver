from core.board import Board
from core.update import Update

class Rule:
    rule_name = "Parent"
    as_score = 0
    cg_score = 0
    
    def find_update_with_score(self, board):
        update = self.find_update(board)
        if not update:
            raise Exception("Update expected; got None")
        update.rule_name = self.rule_name
        update.score = self.cg_score
        return update

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

