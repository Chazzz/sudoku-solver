# sudoku-solver
Solver for sudoku and killer sudoku

Example usage:
```
$ python3 main.py
Enter puzzle json:{"cells": [{"x": 1, "y": 1, "candidates": [2, 3]}, {"x": 0, "y": 1, "candidates": [2, 3]}]}
Solving puzzle, candidates remaining: 715/729
Unsolved puzzle, candidates remaining: 689/729
```

```
python3 main.py
Enter puzzle json:{"cages": [{"coordinates": [{"x": 0, "y": 0}, {"x": 0, "y": 1}], "sum": 3}, {"coordinates": [{"x": 1, "y": 0}, {"x": 1, "y": 1}], "sum": 18}]}
Solving puzzle, candidates remaining: 729/729
Unsolved puzzle, candidates remaining: 729/729
```

Test:
```
$ python3 -m unittest discover
```
