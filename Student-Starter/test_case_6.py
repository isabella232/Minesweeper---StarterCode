"""
Test Case 6
Note that user input is always after the prompt 'Enter your move (for help enter "H"): '
"""

"""
Description: Just showing cells, eventual loss
SIZE = 10, MINES = 10, random.seed(1)
"""

"""
Test Case 1: Results
Mines: 10
  0123456789
0 XXXXXXXXXX 0
1 XXXXXXXXXX 1
2 XXXXXXXXXX 2
3 XXXXXXXXXX 3
4 XXXXXXXXXX 4
5 XXXXXXXXXX 5
6 XXXXXXXXXX 6
7 XXXXXXXXXX 7
8 XXXXXXXXXX 8
9 XXXXXXXXXX 9
  0123456789
Enter your move (for help enter "H"): 55
Mines: 10
  0123456789
0 XXXXXXXXXX 0
1 XXXXXXXXXX 1
2 XXXXXXXXXX 2
3 XXXXXXXXXX 3
4 XXXXXXXXXX 4
5 XXXXX1XXXX 5
6 XXXXXXXXXX 6
7 XXXXXXXXXX 7
8 XXXXXXXXXX 8
9 XXXXXXXXXX 9
  0123456789
Enter your move (for help enter "H"): 33
Mines: 10
  0123456789
0 XXXXXXXXXX 0
1 XXXXXXXXXX 1
2 XXXXXXXXXX 2
3 XXX1XXXXXX 3
4 XXXXXXXXXX 4
5 XXXXX1XXXX 5
6 XXXXXXXXXX 6
7 XXXXXXXXXX 7
8 XXXXXXXXXX 8
9 XXXXXXXXXX 9
  0123456789
Enter your move (for help enter "H"): 66
Mines: 10
  0123456789
0 XXXXXXXXXX 0
1 XXXXXXXXXX 1
2 XXXXXXXXXX 2
3 XXX1XXXXXX 3
4 XXXXXXXXXX 4
5 XXXXX1XXXX 5
6 XXXXXX2XXX 6
7 XXXXXXXXXX 7
8 XXXXXXXXXX 8
9 XXXXXXXXXX 9
  0123456789
Enter your move (for help enter "H"): 47
Mines: 10
  0123456789
0 XXXXXXXXXX 0
1 XXXXXXXXXX 1
2 XXXXXXXXXX 2
3 XXX1XXXXXX 3
4 XXXXXXXXXX 4
5 XXXXX1XXXX 5
6 XXXXXX2XXX 6
7 XXXX2XXXXX 7
8 XXXXXXXXXX 8
9 XXXXXXXXXX 9
  0123456789
Enter your move (for help enter "H"): 89
Mines: 10
  0123456789
0 XXXXXXXXXX 0
1 XXXXXXXXXX 1
2 XXXXX2222X 2
3 XXX1X1  11 3
4 XXXXX1     4
5 XXXXX1211  5
6 XXXXXX2X1  6
7 112X21211  7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 30
Mines: 10
  0123456789
0      1XXXX 0
1      1XXXX 1
2    112222X 2
3    1X1  11 3
4  112X1     4
5 12XXX1211  5
6 XXXXXX2X1  6
7 112X21211  7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 26
Mines: 10
  0123456789
0      1XXXX 0
1      1XXXX 1
2    112222X 2
3    1X1  11 3
4  112X1     4
5 12XXX1211  5
6 XX3XXX2X1  6
7 112X21211  7
8   111      8
9            9
  0123456789
Enter your move (for help enter "H"): 71
Mines: 10
  0123456789
0      1XXXX 0
1      1XMXX 1
2    112222X 2
3    1X1  11 3
4  112X1     4
5 12XXX1211  5
6 XX3XXX2X1  6
7 112X21211  7
8   111      8
9            9
  0123456789
Uh oh! You blew up!
"""
