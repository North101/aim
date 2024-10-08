"""
*** imperfect allocations:
+-----------+---------+--------+---------+--------+------------+
|   players |   total | wind   | table   | meet   | indirect   |
|-----------+---------+--------+---------+--------+------------|
|        16 |       0 |        |         |        |            |
|        20 |       0 |        |         |        |            |
|        24 |       0 |        |         |        |            |
|        28 |       0 |        |         |        |            |
|        32 |       0 |        |         |        |            |
|        36 |       0 |        |         |        |            |
|        40 |       0 |        |         |        |            |
|        44 |       0 |        |         |        |            |
|        48 |       0 |        |         |        |            |
|        52 |       0 |        |         |        |            |
|        56 |       0 |        |         |        |            |
|        60 |       0 |        |         |        |            |
|        64 |       0 |        |         |        |            |
|        68 |       0 |        |         |        |            |
|        72 |       0 |        |         |        |            |
|        76 |       0 |        |         |        |            |
|        80 |       0 |        |         |        |            |
|        84 |       0 |        |         |        |            |
|        88 |       0 |        |         |        |            |
|        92 |       0 |        |         |        |            |
|        96 |       0 |        |         |        |            |
|       100 |       0 |        |         |        |            |
|       104 |       0 |        |         |        |            |
+-----------+---------+--------+---------+--------+------------+
***
"""

seats = {
    16: [[[7, 10, 13, 16],
     [3, 4, 9, 14],
     [2, 5, 8, 15],
     [1, 6, 11, 12]],
     [[4, 16, 12, 8],
     [5, 13, 1, 9],
     [6, 2, 14, 10],
     [11, 15, 7, 3]]],

    20: [[[6, 13, 19, 20],
     [3, 4, 10, 17],
     [1, 7, 8, 14],
     [5, 11, 12, 18],
     [2, 9, 15, 16]],
     [[4, 1, 18, 15],
     [8, 2, 5, 19],
     [9, 3, 6, 12],
     [7, 16, 13, 10],
     [17, 20, 14, 11]]],

    24: [[[3, 12, 22, 24],
     [6, 8, 11, 20],
     [4, 14, 16, 19],
     [1, 5, 7, 18],
     [2, 9, 13, 15],
     [10, 17, 21, 23]],
     [[11, 15, 10, 4],
     [19, 23, 18, 12],
     [7, 20, 3, 2],
     [9, 21, 6, 16],
     [5, 24, 14, 17],
     [8, 22, 1, 13]]],

    28: [[[7, 9, 12, 28],
     [1, 17, 23, 26],
     [2, 8, 18, 21],
     [3, 10, 15, 24],
     [4, 11, 14, 25],
     [5, 16, 20, 27],
     [6, 13, 19, 22]],
     [[8, 6, 26, 20],
     [15, 4, 22, 18],
     [11, 5, 24, 17],
     [9, 2, 27, 14],
     [13, 3, 7, 16],
     [12, 1, 25, 19],
     [10, 28, 21, 23]]],

    32: [[[11, 18, 24, 32],
     [1, 10, 19, 25],
     [3, 9, 17, 26],
     [5, 15, 22, 30],
     [6, 14, 21, 31],
     [2, 8, 16, 27],
     [4, 12, 23, 29],
     [7, 13, 20, 28]],
     [[14, 17, 25, 22],
     [13, 27, 18, 23],
     [10, 28, 15, 24],
     [26, 31, 12, 8],
     [29, 11, 7, 2],
     [9, 30, 6, 1],
     [19, 5, 32, 20],
     [16, 3, 4, 21]]],

    36: [[[5, 6, 31, 34],
     [7, 10, 17, 18],
     [19, 22, 29, 30],
     [1, 3, 8, 24],
     [13, 15, 20, 36],
     [12, 25, 27, 32],
     [9, 14, 23, 28],
     [4, 21, 26, 35],
     [2, 11, 16, 33]],
     [[29, 35, 13, 7],
     [6, 4, 36, 27],
     [17, 23, 1, 31],
     [11, 19, 25, 5],
     [3, 18, 12, 16],
     [28, 30, 24, 15],
     [10, 2, 21, 20],
     [32, 33, 22, 14],
     [8, 9, 34, 26]]],

    40: [[[1, 12, 18, 21],
     [4, 9, 19, 20],
     [3, 10, 15, 24],
     [14, 25, 31, 34],
     [17, 22, 32, 33],
     [16, 23, 28, 37],
     [5, 8, 27, 38],
     [6, 7, 30, 35],
     [2, 11, 29, 36],
     [13, 26, 39, 40]],
     [[24, 17, 38, 29],
     [12, 3, 37, 30],
     [19, 40, 22, 2],
     [10, 20, 21, 5],
     [7, 36, 8, 31],
     [15, 13, 35, 32],
     [18, 34, 33, 23],
     [27, 1, 14, 39],
     [9, 6, 26, 28],
     [11, 16, 25, 4]]],

    44: [[[2, 10, 11, 44],
     [4, 14, 26, 39],
     [7, 21, 29, 40],
     [13, 22, 37, 42],
     [12, 16, 24, 25],
     [6, 23, 27, 33],
     [8, 19, 28, 36],
     [9, 15, 41, 43],
     [1, 17, 20, 38],
     [3, 18, 32, 34],
     [5, 30, 31, 35]],
     [[22, 8, 30, 41],
     [10, 43, 16, 28],
     [11, 12, 3, 1],
     [18, 2, 39, 21],
     [31, 6, 36, 32],
     [14, 7, 34, 24],
     [42, 44, 38, 23],
     [17, 13, 25, 26],
     [19, 33, 35, 4],
     [15, 5, 40, 27],
     [20, 29, 9, 37]]],

    48: [[[1, 5, 18, 48],
     [16, 17, 21, 34],
     [2, 32, 33, 37],
     [8, 19, 41, 44],
     [9, 12, 24, 35],
     [3, 25, 28, 40],
     [4, 6, 13, 27],
     [20, 22, 29, 43],
     [11, 36, 38, 45],
     [7, 15, 26, 46],
     [14, 23, 31, 42],
     [10, 30, 39, 47]],
     [[23, 16, 37, 29],
     [24, 4, 47, 33],
     [13, 7, 48, 21],
     [27, 14, 10, 9],
     [15, 20, 40, 1],
     [17, 8, 36, 31],
     [25, 43, 30, 26],
     [28, 2, 35, 38],
     [12, 34, 19, 22],
     [5, 45, 32, 39],
     [6, 3, 44, 18],
     [41, 46, 42, 11]]],

    52: [[[8, 10, 19, 33],
     [1, 21, 31, 52],
     [5, 13, 20, 32],
     [7, 11, 23, 29],
     [25, 27, 36, 50],
     [17, 18, 38, 48],
     [22, 30, 37, 49],
     [24, 28, 40, 46],
     [2, 16, 42, 44],
     [4, 14, 34, 35],
     [3, 15, 39, 47],
     [6, 12, 41, 45],
     [9, 26, 43, 51]],
     [[31, 22, 46, 41],
     [20, 33, 49, 38],
     [10, 9, 30, 23],
     [26, 47, 27, 40],
     [12, 7, 48, 39],
     [14, 24, 29, 5],
     [13, 6, 44, 43],
     [15, 4, 50, 37],
     [35, 51, 18, 1],
     [16, 3, 32, 21],
     [28, 52, 25, 2],
     [11, 36, 8, 34],
     [19, 17, 45, 42]]],

    56: [[[1, 28, 30, 56],
     [2, 7, 33, 43],
     [4, 5, 32, 34],
     [6, 11, 37, 47],
     [8, 9, 36, 38],
     [10, 15, 41, 51],
     [12, 13, 40, 42],
     [14, 19, 45, 55],
     [16, 17, 44, 46],
     [18, 23, 31, 49],
     [20, 21, 48, 50],
     [22, 27, 35, 53],
     [24, 25, 52, 54],
     [3, 26, 29, 39]],
     [[49, 22, 51, 21],
     [32, 24, 50, 19],
     [15, 20, 46, 28],
     [34, 3, 8, 44],
     [25, 53, 55, 26],
     [27, 40, 4, 30],
     [9, 39, 10, 37],
     [11, 16, 42, 52],
     [7, 12, 38, 48],
     [13, 43, 14, 41],
     [17, 47, 18, 45],
     [23, 54, 56, 36],
     [29, 1, 2, 31],
     [5, 35, 6, 33]]],

    60: [[[5, 11, 14, 60],
     [3, 6, 8, 13],
     [2, 7, 9, 12],
     [15, 20, 26, 29],
     [18, 21, 23, 28],
     [17, 22, 24, 27],
     [30, 35, 41, 44],
     [33, 36, 38, 43],
     [32, 37, 39, 42],
     [45, 50, 56, 59],
     [48, 51, 53, 58],
     [47, 52, 54, 57],
     [1, 16, 31, 46],
     [4, 19, 34, 49],
     [10, 25, 40, 55]],
     [[50, 55, 57, 48],
     [60, 45, 30, 15],
     [19, 17, 28, 26],
     [7, 14, 1, 8],
     [35, 33, 42, 40],
     [11, 13, 4, 2],
     [6, 36, 21, 51],
     [46, 59, 52, 53],
     [49, 47, 58, 56],
     [34, 32, 43, 41],
     [20, 18, 27, 25],
     [16, 29, 22, 23],
     [12, 10, 5, 3],
     [9, 54, 39, 24],
     [31, 38, 44, 37]]],

    64: [[[16, 32, 48, 64],
     [1, 17, 33, 49],
     [2, 18, 34, 50],
     [3, 19, 35, 51],
     [4, 20, 36, 52],
     [5, 21, 37, 53],
     [6, 22, 38, 54],
     [7, 23, 39, 55],
     [8, 24, 40, 56],
     [9, 25, 41, 57],
     [10, 26, 42, 58],
     [11, 27, 43, 59],
     [12, 28, 44, 60],
     [13, 29, 45, 61],
     [14, 30, 46, 62],
     [15, 31, 47, 63]],
     [[31, 12, 61, 46],
     [21, 6, 55, 36],
     [26, 9, 56, 43],
     [23, 4, 53, 38],
     [27, 8, 57, 42],
     [33, 50, 16, 3],
     [17, 2, 51, 32],
     [28, 15, 62, 45],
     [30, 13, 60, 47],
     [29, 14, 63, 44],
     [20, 7, 54, 37],
     [22, 5, 52, 39],
     [25, 10, 59, 40],
     [18, 48, 1, 35],
     [19, 64, 49, 34],
     [24, 11, 58, 41]]],

    68: [[[27, 30, 31, 39],
     [7, 37, 49, 59],
     [9, 47, 51, 56],
     [2, 28, 33, 48],
     [10, 11, 13, 19],
     [5, 12, 41, 65],
     [15, 21, 32, 55],
     [16, 23, 34, 57],
     [35, 36, 38, 50],
     [1, 18, 40, 54],
     [4, 20, 25, 60],
     [3, 22, 26, 53],
     [24, 45, 52, 63],
     [8, 29, 46, 61],
     [6, 14, 43, 62],
     [17, 42, 58, 67],
     [44, 64, 66, 68]],
     [[43, 63, 48, 17],
     [30, 4, 47, 36],
     [31, 38, 6, 49],
     [22, 8, 64, 52],
     [32, 67, 57, 7],
     [23, 44, 61, 10],
     [18, 2, 37, 41],
     [13, 15, 59, 66],
     [33, 55, 16, 3],
     [11, 58, 21, 29],
     [19, 9, 35, 40],
     [62, 68, 24, 5],
     [12, 39, 60, 1],
     [50, 65, 53, 51],
     [25, 34, 28, 26],
     [14, 56, 20, 27],
     [42, 54, 45, 46]]],

    72: [[[4, 17, 30, 37],
     [28, 41, 54, 61],
     [6, 13, 52, 65],
     [5, 23, 36, 63],
     [15, 29, 47, 60],
     [12, 39, 53, 71],
     [7, 10, 35, 64],
     [16, 31, 34, 59],
     [11, 40, 55, 58],
     [8, 14, 19, 72],
     [24, 32, 38, 43],
     [48, 56, 62, 67],
     [9, 25, 69, 70],
     [21, 22, 33, 49],
     [1, 45, 46, 57],
     [18, 20, 27, 50],
     [2, 42, 44, 51],
     [3, 26, 66, 68]],
     [[51, 70, 59, 65],
     [22, 3, 17, 11],
     [42, 15, 71, 56],
     [55, 68, 16, 9],
     [45, 5, 24, 54],
     [36, 1, 2, 52],
     [49, 12, 50, 28],
     [29, 6, 48, 69],
     [31, 64, 57, 44],
     [27, 46, 41, 35],
     [19, 62, 37, 34],
     [32, 18, 63, 47],
     [58, 61, 43, 14],
     [23, 8, 39, 66],
     [26, 60, 25, 4],
     [53, 21, 72, 30],
     [10, 67, 13, 38],
     [40, 7, 20, 33]]],

    76: [[[7, 32, 57, 75],
     [6, 8, 30, 34],
     [31, 33, 55, 59],
     [5, 9, 56, 58],
     [2, 12, 42, 47],
     [27, 37, 67, 72],
     [17, 22, 52, 62],
     [14, 41, 48, 76],
     [25, 39, 66, 73],
     [16, 23, 50, 64],
     [4, 10, 43, 46],
     [29, 35, 68, 71],
     [18, 21, 54, 60],
     [15, 24, 28, 36],
     [40, 49, 53, 61],
     [3, 11, 65, 74],
     [1, 13, 44, 45],
     [26, 38, 69, 70],
     [19, 20, 51, 63]],
     [[12, 4, 70, 66],
     [13, 48, 3, 43],
     [11, 76, 47, 44],
     [41, 62, 45, 54],
     [59, 5, 6, 57],
     [58, 75, 33, 8],
     [71, 27, 39, 65],
     [20, 16, 37, 29],
     [46, 40, 14, 2],
     [36, 25, 72, 69],
     [21, 52, 64, 15],
     [55, 56, 34, 32],
     [38, 28, 73, 68],
     [22, 19, 61, 50],
     [35, 26, 74, 67],
     [23, 18, 63, 53],
     [51, 17, 60, 24],
     [9, 30, 31, 7],
     [10, 1, 49, 42]]],

    80: [[[19, 56, 71, 80],
     [2, 21, 58, 73],
     [4, 23, 60, 75],
     [6, 25, 62, 77],
     [8, 27, 64, 79],
     [10, 29, 41, 66],
     [12, 31, 43, 68],
     [14, 33, 45, 70],
     [16, 35, 47, 72],
     [18, 37, 49, 74],
     [20, 39, 51, 76],
     [1, 22, 53, 78],
     [3, 24, 40, 55],
     [5, 26, 42, 57],
     [7, 28, 44, 59],
     [9, 30, 46, 61],
     [11, 32, 48, 63],
     [13, 34, 50, 65],
     [15, 36, 52, 67],
     [17, 38, 54, 69]],
     [[57, 72, 20, 1],
     [59, 74, 22, 3],
     [61, 5, 76, 24],
     [63, 7, 78, 26],
     [28, 9, 65, 40],
     [30, 42, 67, 11],
     [32, 13, 69, 44],
     [71, 15, 34, 46],
     [36, 17, 73, 48],
     [38, 19, 75, 50],
     [21, 80, 77, 52],
     [23, 2, 79, 54],
     [25, 4, 56, 41],
     [27, 58, 6, 43],
     [29, 60, 8, 45],
     [31, 62, 10, 47],
     [33, 64, 12, 49],
     [35, 14, 66, 51],
     [37, 16, 68, 53],
     [39, 55, 70, 18]]],

    84: [[[19, 66, 80, 84],
     [10, 24, 28, 47],
     [38, 52, 56, 75],
     [2, 4, 22, 79],
     [23, 30, 32, 50],
     [51, 58, 60, 78],
     [3, 33, 36, 74],
     [18, 31, 61, 64],
     [5, 8, 46, 59],
     [6, 70, 71, 82],
     [14, 15, 26, 34],
     [42, 43, 54, 62],
     [7, 11, 17, 69],
     [13, 35, 39, 45],
     [41, 63, 67, 73],
     [9, 48, 72, 77],
     [16, 21, 37, 76],
     [20, 44, 49, 65],
     [1, 27, 53, 68],
     [12, 29, 55, 81],
     [25, 40, 57, 83]],
     [[54, 2, 69, 27],
     [21, 50, 45, 66],
     [47, 6, 9, 60],
     [24, 51, 31, 33],
     [8, 18, 12, 70],
     [17, 38, 77, 22],
     [26, 41, 83, 58],
     [30, 13, 82, 55],
     [56, 71, 7, 72],
     [49, 78, 73, 10],
     [44, 28, 63, 43],
     [15, 84, 16, 35],
     [39, 57, 76, 53],
     [32, 65, 62, 19],
     [11, 25, 29, 48],
     [80, 23, 5, 3],
     [52, 79, 59, 61],
     [64, 68, 74, 42],
     [46, 36, 14, 40],
     [4, 75, 34, 37],
     [67, 20, 81, 1]]],

    88: [[[1, 28, 41, 46],
     [2, 27, 34, 53],
     [4, 25, 39, 48],
     [8, 21, 38, 49],
     [13, 16, 40, 47],
     [3, 26, 36, 51],
     [6, 23, 43, 44],
     [30, 57, 70, 75],
     [31, 56, 63, 82],
     [33, 54, 68, 77],
     [37, 50, 67, 78],
     [42, 45, 69, 76],
     [32, 55, 65, 80],
     [35, 52, 72, 73],
     [12, 17, 59, 86],
     [5, 24, 60, 85],
     [10, 19, 62, 83],
     [9, 20, 66, 79],
     [11, 18, 71, 74],
     [7, 22, 61, 84],
     [14, 15, 64, 81],
     [29, 58, 87, 88]],
     [[20, 73, 76, 13],
     [22, 11, 81, 68],
     [15, 49, 18, 42],
     [27, 6, 50, 41],
     [43, 48, 3, 1],
     [21, 12, 85, 64],
     [26, 7, 58, 62],
     [16, 83, 17, 66],
     [28, 5, 53, 38],
     [19, 61, 14, 59],
     [39, 69, 80, 52],
     [34, 67, 82, 57],
     [56, 35, 79, 70],
     [24, 9, 86, 63],
     [65, 84, 33, 29],
     [36, 88, 55, 4],
     [72, 77, 32, 30],
     [54, 74, 75, 37],
     [23, 10, 51, 40],
     [25, 8, 46, 45],
     [60, 2, 31, 87],
     [44, 78, 47, 71]]],

    92: [[[23, 46, 69, 92],
     [1, 24, 48, 72],
     [2, 25, 50, 75],
     [3, 26, 52, 78],
     [4, 27, 54, 81],
     [5, 28, 56, 84],
     [6, 29, 58, 87],
     [7, 30, 60, 90],
     [8, 31, 62, 70],
     [9, 32, 64, 73],
     [10, 33, 66, 76],
     [11, 34, 68, 79],
     [12, 35, 47, 82],
     [13, 36, 49, 85],
     [14, 37, 51, 88],
     [15, 38, 53, 91],
     [16, 39, 55, 71],
     [17, 40, 57, 74],
     [18, 41, 59, 77],
     [19, 42, 61, 80],
     [20, 43, 63, 83],
     [21, 44, 65, 86],
     [22, 45, 67, 89]],
     [[36, 12, 83, 48],
     [54, 15, 39, 69],
     [68, 90, 23, 22],
     [25, 1, 73, 49],
     [24, 92, 70, 47],
     [42, 18, 78, 60],
     [32, 8, 71, 63],
     [45, 21, 87, 66],
     [33, 9, 74, 65],
     [40, 16, 72, 56],
     [38, 14, 89, 52],
     [41, 17, 75, 58],
     [37, 13, 86, 50],
     [43, 19, 81, 62],
     [31, 7, 91, 61],
     [28, 4, 82, 55],
     [26, 2, 76, 51],
     [30, 6, 88, 59],
     [44, 20, 84, 64],
     [29, 5, 85, 57],
     [34, 10, 77, 67],
     [27, 3, 79, 53],
     [35, 11, 80, 46]]],

    96: [[[24, 48, 72, 96],
     [1, 26, 51, 76],
     [2, 27, 58, 73],
     [3, 25, 57, 77],
     [4, 33, 59, 90],
     [5, 35, 56, 94],
     [6, 46, 64, 87],
     [7, 44, 67, 83],
     [8, 31, 61, 95],
     [9, 29, 62, 91],
     [10, 43, 70, 92],
     [11, 41, 69, 88],
     [12, 47, 49, 85],
     [13, 45, 50, 81],
     [14, 32, 53, 75],
     [15, 34, 54, 79],
     [16, 28, 68, 82],
     [17, 30, 71, 86],
     [18, 36, 65, 93],
     [19, 38, 66, 89],
     [20, 37, 55, 80],
     [21, 39, 52, 84],
     [22, 42, 60, 78],
     [23, 40, 63, 74]],
     [[37, 19, 92, 64],
     [46, 13, 84, 48],
     [26, 72, 3, 59],
     [76, 56, 2, 24],
     [25, 49, 73, 1],
     [41, 62, 75, 22],
     [33, 15, 74, 52],
     [38, 20, 85, 53],
     [42, 71, 93, 11],
     [39, 18, 88, 67],
     [80, 12, 44, 51],
     [31, 16, 87, 70],
     [28, 8, 90, 63],
     [55, 14, 78, 35],
     [29, 69, 83, 17],
     [40, 68, 89, 10],
     [30, 60, 94, 9],
     [45, 6, 82, 66],
     [61, 23, 79, 43],
     [47, 7, 86, 65],
     [32, 5, 91, 58],
     [34, 57, 95, 4],
     [36, 21, 81, 54],
     [50, 77, 96, 27]]],

    100: [[[25, 50, 75, 100],
     [1, 10, 12, 22],
     [3, 5, 6, 11],
     [28, 30, 31, 36],
     [29, 33, 40, 43],
     [54, 58, 65, 68],
     [52, 69, 70, 74],
     [77, 94, 95, 99],
     [76, 85, 87, 97],
     [9, 42, 71, 88],
     [7, 41, 73, 89],
     [15, 45, 60, 80],
     [17, 46, 63, 84],
     [16, 48, 64, 82],
     [4, 27, 51, 78],
     [20, 35, 55, 90],
     [18, 49, 62, 81],
     [21, 38, 59, 92],
     [23, 39, 57, 91],
     [8, 44, 72, 86],
     [2, 26, 53, 79],
     [24, 37, 56, 93],
     [13, 34, 67, 96],
     [14, 32, 66, 98],
     [19, 47, 61, 83]],
     [[78, 96, 90, 95],
     [50, 59, 69, 66],
     [40, 87, 9, 73],
     [65, 70, 53, 71],
     [26, 51, 76, 1],
     [11, 13, 2, 23],
     [93, 55, 22, 39],
     [35, 24, 92, 58],
     [46, 16, 81, 61],
     [47, 18, 80, 64],
     [30, 68, 97, 14],
     [43, 72, 89, 5],
     [85, 8, 74, 42],
     [27, 75, 54, 3],
     [41, 25, 44, 34],
     [6, 7, 4, 12],
     [31, 29, 32, 37],
     [45, 19, 82, 63],
     [49, 17, 83, 60],
     [48, 15, 84, 62],
     [86, 88, 98, 77],
     [38, 57, 94, 20],
     [79, 100, 52, 28],
     [10, 67, 99, 33],
     [36, 21, 91, 56]]],

    104: [[[14, 61, 71, 104],
     [4, 18, 65, 75],
     [8, 22, 69, 79],
     [12, 26, 73, 83],
     [16, 30, 77, 87],
     [20, 34, 81, 91],
     [24, 38, 85, 95],
     [28, 42, 89, 99],
     [32, 46, 93, 103],
     [3, 36, 50, 97],
     [7, 40, 54, 101],
     [1, 11, 44, 58],
     [5, 15, 48, 62],
     [9, 19, 52, 66],
     [13, 23, 56, 70],
     [17, 27, 60, 74],
     [21, 31, 64, 78],
     [25, 35, 68, 82],
     [29, 39, 72, 86],
     [33, 43, 76, 90],
     [37, 47, 80, 94],
     [41, 51, 84, 98],
     [45, 55, 88, 102],
     [2, 49, 59, 92],
     [6, 53, 63, 96],
     [10, 57, 67, 100]],
     [[63, 2, 16, 73],
     [67, 20, 6, 77],
     [71, 10, 24, 81],
     [85, 28, 75, 14],
     [89, 32, 79, 18],
     [22, 93, 83, 36],
     [87, 97, 40, 26],
     [30, 91, 101, 44],
     [95, 1, 34, 48],
     [99, 5, 38, 52],
     [103, 9, 42, 56],
     [60, 3, 13, 46],
     [50, 7, 17, 64],
     [54, 21, 11, 68],
     [72, 25, 58, 15],
     [76, 29, 62, 19],
     [80, 33, 66, 23],
     [27, 37, 70, 84],
     [31, 41, 74, 88],
     [35, 78, 92, 45],
     [39, 82, 96, 49],
     [43, 86, 100, 53],
     [47, 90, 104, 57],
     [51, 4, 94, 61],
     [55, 8, 98, 65],
     [59, 12, 102, 69]]],

}
