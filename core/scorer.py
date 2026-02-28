import math

class Scorer:
    def update_score(self, board, update):
        ms = self.get_move_score(board, update)
        board.scores.append(ms)
        return ms

    def get_move_score(self, board, update):
        sc = sum([len(c.candidates) for c in board])
        f = sc * 20 / 727  # Not python 2 compatible
        score = update.score * update.score * update.score * f
        return score

    def get_overall_score(self, board):
        # Assumes 9x9
        top10 = sorted(board.scores)[-10:]
        return math.log(sum(top10), 10)