# sudoku_solver
Sudoku solver code in C language. It can solve every valid sudoku.



```
    Sudoku Representation
    
  *****************************
  *****************************
  ** Box 1 ** Box 2 ** Box 3 **
  *****************************
  *****************************
  ** Box 4 ** Box 5 ** Box 6 **
  *****************************
  *****************************
  ** Box 7 ** Box 8 ** Box 9 **
  *****************************
  *****************************
```

Follow the below rules for entries.
  1. For blank entries use spaces
  2. For filled entries use numbers.
  3. Write all entries in one line as given below.
  For example:-
  
    5 0 0  0 0 0  0 7 0
    0 1 0  3 0 9  8 0 0
    0 0 0  0 4 0  0 0 0

    0 0 1  0 0 0  0 0 9
    0 0 0  0 0 6  0 0 0
    0 9 0  2 0 8  3 0 0

    0 0 7  4 0 2  0 8 0
    0 2 0  0 6 0  0 0 0
    0 0 0  0 1 0  4 0 0
  
  The above sudoku can be written as:-
```
"5      7  1 3 98      4      1     9     6    9 2 83    74 2 8  2  6        1 4  "
```