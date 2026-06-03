class Update:
    def __init__(self, rule_name, explanation="", eliminations=None, cages=None, virtual_cages=None):
        self.rule_name = rule_name
        self.explanation = explanation
        self.eliminations = eliminations
        self.cages = cages
        self.virtual_cages = virtual_cages