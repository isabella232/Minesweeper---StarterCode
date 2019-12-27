"""
Test Case 5
Note that user input is always after the prompt 'Enter your move (for help enter "H"): '
"""

"""
Description: Flagging more than maximum number of mines and showing flagged tiles, followed by instant loss
SIZE = 10, MINES = 10, random.seed(5)
"""

"""
Test Case 6 - Results

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
Enter your move (for help enter "H"): 00f
Mines: 9
  0123456789
0 FXXXXXXXXX 0
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
Enter your move (for help enter "H"): 11f
Mines: 8
  0123456789
0 FXXXXXXXXX 0
1 XFXXXXXXXX 1
2 XXXXXXXXXX 2
3 XXXXXXXXXX 3
4 XXXXXXXXXX 4
5 XXXXXXXXXX 5
6 XXXXXXXXXX 6
7 XXXXXXXXXX 7
8 XXXXXXXXXX 8
9 XXXXXXXXXX 9
  0123456789
Enter your move (for help enter "H"): 22f
Mines: 7
  0123456789
0 FXXXXXXXXX 0
1 XFXXXXXXXX 1
2 XXFXXXXXXX 2
3 XXXXXXXXXX 3
4 XXXXXXXXXX 4
5 XXXXXXXXXX 5
6 XXXXXXXXXX 6
7 XXXXXXXXXX 7
8 XXXXXXXXXX 8
9 XXXXXXXXXX 9
  0123456789
Enter your move (for help enter "H"): 33f
Mines: 6
  0123456789
0 FXXXXXXXXX 0
1 XFXXXXXXXX 1
2 XXFXXXXXXX 2
3 XXXFXXXXXX 3
4 XXXXXXXXXX 4
5 XXXXXXXXXX 5
6 XXXXXXXXXX 6
7 XXXXXXXXXX 7
8 XXXXXXXXXX 8
9 XXXXXXXXXX 9
  0123456789
Enter your move (for help enter "H"): 44f
Mines: 5
  0123456789
0 FXXXXXXXXX 0
1 XFXXXXXXXX 1
2 XXFXXXXXXX 2
3 XXXFXXXXXX 3
4 XXXXFXXXXX 4
5 XXXXXXXXXX 5
6 XXXXXXXXXX 6
7 XXXXXXXXXX 7
8 XXXXXXXXXX 8
9 XXXXXXXXXX 9
  0123456789
Enter your move (for help enter "H"): 55f
Mines: 4
  0123456789
0 FXXXXXXXXX 0
1 XFXXXXXXXX 1
2 XXFXXXXXXX 2
3 XXXFXXXXXX 3
4 XXXXFXXXXX 4
5 XXXXXFXXXX 5
6 XXXXXXXXXX 6
7 XXXXXXXXXX 7
8 XXXXXXXXXX 8
9 XXXXXXXXXX 9
  0123456789
Enter your move (for help enter "H"): 66f
Mines: 3
  0123456789
0 FXXXXXXXXX 0
1 XFXXXXXXXX 1
2 XXFXXXXXXX 2
3 XXXFXXXXXX 3
4 XXXXFXXXXX 4
5 XXXXXFXXXX 5
6 XXXXXXFXXX 6
7 XXXXXXXXXX 7
8 XXXXXXXXXX 8
9 XXXXXXXXXX 9
  0123456789
Enter your move (for help enter "H"): 77f
Mines: 2
  0123456789
0 FXXXXXXXXX 0
1 XFXXXXXXXX 1
2 XXFXXXXXXX 2
3 XXXFXXXXXX 3
4 XXXXFXXXXX 4
5 XXXXXFXXXX 5
6 XXXXXXFXXX 6
7 XXXXXXXFXX 7
8 XXXXXXXXXX 8
9 XXXXXXXXXX 9
  0123456789
Enter your move (for help enter "H"): 88f
Mines: 1
  0123456789
0 FXXXXXXXXX 0
1 XFXXXXXXXX 1
2 XXFXXXXXXX 2
3 XXXFXXXXXX 3
4 XXXXFXXXXX 4
5 XXXXXFXXXX 5
6 XXXXXXFXXX 6
7 XXXXXXXFXX 7
8 XXXXXXXXFX 8
9 XXXXXXXXXX 9
  0123456789
Enter your move (for help enter "H"): 99f
Mines: 0
  0123456789
0 FXXXXXXXXX 0
1 XFXXXXXXXX 1
2 XXFXXXXXXX 2
3 XXXFXXXXXX 3
4 XXXXFXXXXX 4
5 XXXXXFXXXX 5
6 XXXXXXFXXX 6
7 XXXXXXXFXX 7
8 XXXXXXXXFX 8
9 XXXXXXXXXF 9
  0123456789
Enter your move (for help enter "H"): 55
Mines: 0
  0123456789
0 FXXXXXXXXX 0
1 XFXXXXXXXX 1
2 XXFXXXXXXX 2
3 XXXFXXXXXX 3
4 XXXXFXXXXX 4
5 XXXXXFXXXX 5
6 XXXXXXFXXX 6
7 XXXXXXXFXX 7
8 XXXXXXXXFX 8
9 XXXXXXXXXF 9
  0123456789
Enter your move (for help enter "H"): 33
Mines: 0
  0123456789
0 FXXXXXXXXX 0
1 XFXXXXXXXX 1
2 XXFXXXXXXX 2
3 XXXFXXXXXX 3
4 XXXXFXXXXX 4
5 XXXXXFXXXX 5
6 XXXXXXFXXX 6
7 XXXXXXXFXX 7
8 XXXXXXXXFX 8
9 XXXXXXXXXF 9
  0123456789
Enter your move (for help enter "H"): 54f
You have already flagged all your mines.
Mines: 0
  0123456789
0 FXXXXXXXXX 0
1 XFXXXXXXXX 1
2 XXFXXXXXXX 2
3 XXXFXXXXXX 3
4 XXXXFXXXXX 4
5 XXXXXFXXXX 5
6 XXXXXXFXXX 6
7 XXXXXXXFXX 7
8 XXXXXXXXFX 8
9 XXXXXXXXXF 9
  0123456789
Enter your move (for help enter "H"): 45f
You have already flagged all your mines.
Mines: 0
  0123456789
0 FXXXXXXXXX 0
1 XFXXXXXXXX 1
2 XXFXXXXXXX 2
3 XXXFXXXXXX 3
4 XXXXFXXXXX 4
5 XXXXXFXXXX 5
6 XXXXXXFXXX 6
7 XXXXXXXFXX 7
8 XXXXXXXXFX 8
9 XXXXXXXXXF 9
  0123456789
Enter your move (for help enter "H"): 22f
Mines: 1
  0123456789
0 FXXXXXXXXX 0
1 XFXXXXXXXX 1
2 XXXXXXXXXX 2
3 XXXFXXXXXX 3
4 XXXXFXXXXX 4
5 XXXXXFXXXX 5
6 XXXXXXFXXX 6
7 XXXXXXXFXX 7
8 XXXXXXXXFX 8
9 XXXXXXXXXF 9
  0123456789
Enter your move (for help enter "H"): 33f
Mines: 2
  0123456789
0 FXXXXXXXXX 0
1 XFXXXXXXXX 1
2 XXXXXXXXXX 2
3 XXXXXXXXXX 3
4 XXXXFXXXXX 4
5 XXXXXFXXXX 5
6 XXXXXXFXXX 6
7 XXXXXXXFXX 7
8 XXXXXXXXFX 8
9 XXXXXXXXXF 9
  0123456789
Enter your move (for help enter "H"): 22
Mines: 2
  0123456789
0 FXXXXXXXXX 0
1 XFXXXXXXXX 1
2 XXMXXXXXXX 2
3 XXXXXXXXXX 3
4 XXXXFXXXXX 4
5 XXXXXFXXXX 5
6 XXXXXXFXXX 6
7 XXXXXXXFXX 7
8 XXXXXXXXFX 8
9 XXXXXXXXXF 9
  0123456789
Uh oh! You blew up!
"""