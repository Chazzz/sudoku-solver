# sudoku-solver
Solver for sudoku and killer sudoku using human-style methods. As of Feb 2026, this is the best publicly available solver for killer sudoku using human-style methods.

Test:
```
python3 -m unittest discover
```

Example usage:
```
$ python3 main.py
Enter puzzle json:{"cells": [{"x": 1, "y": 1, "candidates": [2, 3]}, {"x": 0, "y": 1, "candidates": [2, 3]}]}
[...lots of output...]
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
| 1   | 1   | 1   | 123 | 123 | 123 | 123 | 123 | 123 |
| 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 |
| 789 | 789 | 789 | 789 | 789 | 789 | 789 | 789 | 789 |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
|  23 |  23 | 1   | 1   | 1   | 1   | 1   | 1   | 1   |
|     |     | 456 | 456 | 456 | 456 | 456 | 456 | 456 |
|     |     | 789 | 789 | 789 | 789 | 789 | 789 | 789 |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
| 1   | 1   | 1   | 123 | 123 | 123 | 123 | 123 | 123 |
| 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 |
| 789 | 789 | 789 | 789 | 789 | 789 | 789 | 789 | 789 |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
| 123 | 123 | 123 | 123 | 123 | 123 | 123 | 123 | 123 |
| 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 |
| 789 | 789 | 789 | 789 | 789 | 789 | 789 | 789 | 789 |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
| 123 | 123 | 123 | 123 | 123 | 123 | 123 | 123 | 123 |
| 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 |
| 789 | 789 | 789 | 789 | 789 | 789 | 789 | 789 | 789 |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
| 123 | 123 | 123 | 123 | 123 | 123 | 123 | 123 | 123 |
| 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 |
| 789 | 789 | 789 | 789 | 789 | 789 | 789 | 789 | 789 |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
| 123 | 123 | 123 | 123 | 123 | 123 | 123 | 123 | 123 |
| 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 |
| 789 | 789 | 789 | 789 | 789 | 789 | 789 | 789 | 789 |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
| 123 | 123 | 123 | 123 | 123 | 123 | 123 | 123 | 123 |
| 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 |
| 789 | 789 | 789 | 789 | 789 | 789 | 789 | 789 | 789 |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
| 123 | 123 | 123 | 123 | 123 | 123 | 123 | 123 | 123 |
| 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 |
| 789 | 789 | 789 | 789 | 789 | 789 | 789 | 789 | 789 |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
Unsolved puzzle, candidates remaining: 689/729
```

```
python3 main.py
Enter puzzle json:{"cages": [{"coordinates": [{"x": 0, "y": 0}, {"x": 0, "y": 1}], "sum": 3}, {"coordinates": [{"x": 1, "y": 0}, {"x": 1, "y": 1}], "sum": 17}]}
[...lots of output...]
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
| 12  |     |   3 | 123 | 123 | 123 | 123 | 123 | 123 |
|     |     | 456 | 456 | 456 | 456 | 456 | 456 | 456 |
|     |  89 | 7   | 789 | 789 | 789 | 789 | 789 | 789 |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
| 12  |     |   3 | 123 | 123 | 123 | 123 | 123 | 123 |
|     |     | 456 | 456 | 456 | 456 | 456 | 456 | 456 |
|     |  89 | 7   | 789 | 789 | 789 | 789 | 789 | 789 |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
|   3 |   3 |   3 | 123 | 123 | 123 | 123 | 123 | 123 |
| 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 |
| 7   | 7   | 7   | 789 | 789 | 789 | 789 | 789 | 789 |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
|   3 | 123 | 123 | 123 | 123 | 123 | 123 | 123 | 123 |
| 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 |
| 789 | 7   | 789 | 789 | 789 | 789 | 789 | 789 | 789 |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
|   3 | 123 | 123 | 123 | 123 | 123 | 123 | 123 | 123 |
| 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 |
| 789 | 7   | 789 | 789 | 789 | 789 | 789 | 789 | 789 |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
|   3 | 123 | 123 | 123 | 123 | 123 | 123 | 123 | 123 |
| 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 |
| 789 | 7   | 789 | 789 | 789 | 789 | 789 | 789 | 789 |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
|   3 | 123 | 123 | 123 | 123 | 123 | 123 | 123 | 123 |
| 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 |
| 789 | 7   | 789 | 789 | 789 | 789 | 789 | 789 | 789 |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
|   3 | 123 | 123 | 123 | 123 | 123 | 123 | 123 | 123 |
| 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 |
| 789 | 7   | 789 | 789 | 789 | 789 | 789 | 789 | 789 |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
|   3 | 123 | 123 | 123 | 123 | 123 | 123 | 123 | 123 |
| 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 | 456 |
| 789 | 7   | 789 | 789 | 789 | 789 | 789 | 789 | 789 |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
Unsolved puzzle, candidates remaining: 657/729
```

```
python main.py < puzzle.json
Solving puzzle, candidates remaining: 729/729
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
|     |   3 | 1   |     |     |     |     |  2  |     |
|     |     |     |  5  |     |     | 4   |     |   6 |
| 7   |     |     |     |  8  |   9 |     |     |     |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
|     |     |     |     |  2  |     |   3 | 1   |     |
|  5  |     |     |   6 |     | 4   |     |     |     |
|     |  8  |   9 |     |     |     |     |     | 7   |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
|  2  |     |     |   3 | 1   |     |     |     |     |
|     | 4   |   6 |     |     |     |  5  |     |     |
|     |     |     |     |     | 7   |     |  8  |   9 |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
|     |  2  |     |     |     |   3 |     |     | 1   |
| 4   |     |  5  |     |   6 |     |     |     |     |
|     |     |     | 7   |     |     |  8  |   9 |     |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
| 1   |     |     |     |     |     |  2  |   3 |     |
|     |   6 |     | 4   |     |     |     |     |  5  |
|     |     | 7   |     |   9 |  8  |     |     |     |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
|   3 |     |     |  2  |     | 1   |     |     |     |
|     |     |     |     |  5  |     |   6 |     | 4   |
|     |   9 |  8  |     |     |     |     | 7   |     |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
|     | 1   |  2  |     |     |     |     |     |   3 |
|   6 |     |     |     |     |  5  |     | 4   |     |
|     |     |     |  8  | 7   |     |   9 |     |     |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
|     |     |   3 |     |     |     | 1   |     |  2  |
|     |     |     |     | 4   |   6 |     |  5  |     |
|  8  | 7   |     |   9 |     |     |     |     |     |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
|     |     |     | 1   |   3 |  2  |     |     |     |
|     |  5  | 4   |     |     |     |     |   6 |     |
|   9 |     |     |     |     |     | 7   |     |  8  |
·-----·-----·-----·-----·-----·-----·-----·-----·-----·
solved puzzle
```

## Grading

Killer Sudoku: Easy 0-5.5, Hard 5.5-6, Expert 6+ (max 8+) 

Inividual rules: Easy 1-5, Hard 10-20, Expert 25+ (max 100)

### Goals

Rules and puzzles should have a spread of graded difficulties that accurately express how difficult they are.

Despite how solve time tends to be much longer for harder rules and puzzles, difficulty should be roughly linear.

### Implementation

Grading is done in a two-stage process:

Individual updates are scored as the cubed difficulty of the solving rule used multiplied by a linear factor based on the number of candidates remaining. 

$$Update\ score = Rule\ difficulty^3 * Factor\ F$$

Recall that an unsolved board has 727 candidates and a solved board has 81 candidates.

$$Factor\ F = Candidates\ C / 727 * 20$$

A factor of 10 would mean 50% of the board's candidates have been eliminated, for example.

In the second step, the final grade is calculated by using a log of the sum of the 10 biggest update scores to linearize the difficulty.

$$9x9: Log_{10}(sum(top10\_scores)) * 2$$

### Reasoning

In order to adequately differentiate easy puzzles and hard puzzles, rule difficulty is the dominating factor, and then secondarily quantity.

Capping grading to the top 10 scores removes most of the "routine solve" steps from the overall grade, allowing a larger spread between easy and difficult puzzles.

### Rule scoring scheme

Rules are scored on how many lines of code (LOC) are taken to implement them. The idea here is that the more complex it is to express each rule, the more difficult it is for a human to apply them.

Rule scoring follows the approximate formula:

$$Rule\ difficulty = (LOC - 50) / 5$$

For human readability and consistency with Andrew Stuart's rankings, difficulties are rounded to the nearest 5 (or rounded down to 1 in the case of the easiest algorithms).

One critique is that lines of code doesn't account for rules that are simple to express but take a long time to calculate. In practice this is not true, because rules that are simple to express but take a long time to calculate are optimized, which increases the lines of code (as done with hard combinations in [Pull #25](https://github.com/Chazzz/sudoku-solver/pull/25)). Thus you can be confident that the rules take into account both complexity and performance.

In cases where a rule takes a long time to compute relative to its difficulty, but an optimization has not been implemented, the assessed rule difficulty has been preemptively increased.

### Comparison to Andrew Stuart's rating system.

Andrew Stuart discusses his rating system at [https://www.sudokuwiki.org/Grading_Puzzles](https://www.sudokuwiki.org/Grading_Puzzles). Contrary to documentation, his system sets a large number of algorthms to 1 difficulty, and this helps spread puzzle difficulty in a more usably exponential fashion. This has upsides (better puzzle difficulty spread) and downsides (compressing rule difficulty).

While many rules are equal or lower in difficulty using the LOC heuristic, the Killer Innie/Outie rules are dramatically higher in score (and take similarly long to execute). This creates a strong preference with LOC difficulty to use normal Sudoku rules whenever possible, as well as increases the assessed difficulty of Killer Sudoku puzzles.

### Known issues

In human solving, any amount of chaining can often advance puzzles outside the "intended" path. The flexibility of solves should, but doesn't currently, reduce graded difficulty.