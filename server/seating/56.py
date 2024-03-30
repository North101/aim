# adapted from Alice Miller's social golfer page at http://breakoutroom.pythonanywhere.com/allocate/
seats = [
	[
		[56, 1, 28, 30],
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
		[3, 26, 29, 39]
	],

	[
		[1, 2, 29, 31],
		[3, 8, 34, 44],
		[5, 6, 33, 35],
		[7, 12, 38, 48],
		[9, 10, 37, 39],
		[11, 16, 42, 52],
		[13, 14, 41, 43],
		[15, 20, 28, 46],
		[17, 18, 45, 47],
		[19, 24, 32, 50],
		[21, 22, 49, 51],
		[56, 23, 36, 54],
		[25, 26, 53, 55],
		[4, 27, 30, 40]
	],

	[
		[2, 3, 30, 32],
		[4, 9, 35, 45],
		[6, 7, 34, 36],
		[8, 13, 39, 49],
		[10, 11, 38, 40],
		[12, 17, 43, 53],
		[14, 15, 42, 44],
		[16, 21, 29, 47],
		[18, 19, 46, 48],
		[20, 25, 33, 51],
		[22, 23, 50, 52],
		[1, 24, 37, 55],
		[26, 27, 28, 54],
		[56, 5, 31, 41]
	],

	[
		[3, 4, 31, 33],
		[5, 10, 36, 46],
		[7, 8, 35, 37],
		[9, 14, 40, 50],
		[11, 12, 39, 41],
		[13, 18, 44, 54],
		[15, 16, 43, 45],
		[17, 22, 30, 48],
		[19, 20, 47, 49],
		[21, 26, 34, 52],
		[23, 24, 51, 53],
		[2, 25, 28, 38],
		[56, 27, 29, 55],
		[1, 6, 32, 42]
	],

	[
		[56, 2, 17, 20],
		[3, 6, 14, 16],
		[31, 32, 39, 54],
		[40, 45, 46, 53],
		[1, 25, 36, 47],
		[11, 15, 33, 50],
		[4, 23, 38, 42],
		[9, 18, 28, 52],
		[5, 12, 37, 49],
		[19, 26, 35, 51],
		[7, 13, 30, 55],
		[21, 27, 41, 44],
		[8, 24, 29, 48],
		[10, 22, 34, 43]
	],

	[
		[1, 3, 18, 21],
		[4, 7, 15, 17],
		[32, 33, 40, 55],
		[41, 46, 47, 54],
		[2, 26, 37, 48],
		[12, 16, 34, 51],
		[5, 24, 39, 43],
		[10, 19, 29, 53],
		[6, 13, 38, 50],
		[20, 27, 36, 52],
		[8, 14, 28, 31],
		[56, 22, 42, 45],
		[9, 25, 30, 49],
		[11, 23, 35, 44]
	],

	[
		[2, 4, 19, 22],
		[5, 8, 16, 18],
		[28, 33, 34, 41],
		[42, 47, 48, 55],
		[3, 27, 38, 49],
		[13, 17, 35, 52],
		[6, 25, 40, 44],
		[11, 20, 30, 54],
		[7, 14, 39, 51],
		[56, 21, 37, 53],
		[9, 15, 29, 32],
		[1, 23, 43, 46],
		[10, 26, 31, 50],
		[12, 24, 36, 45]
	],

	[
		[3, 5, 20, 23],
		[6, 9, 17, 19],
		[29, 34, 35, 42],
		[28, 43, 48, 49],
		[56, 4, 39, 50],
		[14, 18, 36, 53],
		[7, 26, 41, 45],
		[12, 21, 31, 55],
		[8, 15, 40, 52],
		[1, 22, 38, 54],
		[10, 16, 30, 33],
		[2, 24, 44, 47],
		[11, 27, 32, 51],
		[13, 25, 37, 46]
	],

	[
		[4, 6, 21, 24],
		[7, 10, 18, 20],
		[30, 35, 36, 43],
		[29, 44, 49, 50],
		[1, 5, 40, 51],
		[15, 19, 37, 54],
		[8, 27, 42, 46],
		[13, 22, 28, 32],
		[9, 16, 41, 53],
		[2, 23, 39, 55],
		[11, 17, 31, 34],
		[3, 25, 45, 48],
		[56, 12, 33, 52],
		[14, 26, 38, 47]
	],

	[
		[5, 7, 22, 25],
		[8, 11, 19, 21],
		[31, 36, 37, 44],
		[30, 45, 50, 51],
		[2, 6, 41, 52],
		[16, 20, 38, 55],
		[56, 9, 43, 47],
		[14, 23, 29, 33],
		[10, 17, 42, 54],
		[3, 24, 28, 40],
		[12, 18, 32, 35],
		[4, 26, 46, 49],
		[1, 13, 34, 53],
		[15, 27, 39, 48]
	],

	[
		[6, 8, 23, 26],
		[9, 12, 20, 22],
		[32, 37, 38, 45],
		[31, 46, 51, 52],
		[3, 7, 42, 53],
		[17, 21, 28, 39],
		[1, 10, 44, 48],
		[15, 24, 30, 34],
		[11, 18, 43, 55],
		[4, 25, 29, 41],
		[13, 19, 33, 36],
		[5, 27, 47, 50],
		[2, 14, 35, 54],
		[56, 16, 40, 49]
	],

	[
		[7, 9, 24, 27],
		[10, 13, 21, 23],
		[33, 38, 39, 46],
		[32, 47, 52, 53],
		[4, 8, 43, 54],
		[18, 22, 29, 40],
		[2, 11, 45, 49],
		[16, 25, 31, 35],
		[12, 19, 28, 44],
		[5, 26, 30, 42],
		[14, 20, 34, 37],
		[56, 6, 48, 51],
		[3, 15, 36, 55],
		[1, 17, 41, 50]
	],

	[
		[56, 8, 10, 25],
		[11, 14, 22, 24],
		[34, 39, 40, 47],
		[33, 48, 53, 54],
		[5, 9, 44, 55],
		[19, 23, 30, 41],
		[3, 12, 46, 50],
		[17, 26, 32, 36],
		[13, 20, 29, 45],
		[6, 27, 31, 43],
		[15, 21, 35, 38],
		[1, 7, 49, 52],
		[4, 16, 28, 37],
		[2, 18, 42, 51]
	],

	[
		[1, 9, 11, 26],
		[12, 15, 23, 25],
		[35, 40, 41, 48],
		[34, 49, 54, 55],
		[6, 10, 28, 45],
		[20, 24, 31, 42],
		[4, 13, 47, 51],
		[18, 27, 33, 37],
		[14, 21, 30, 46],
		[56, 7, 32, 44],
		[16, 22, 36, 39],
		[2, 8, 50, 53],
		[5, 17, 29, 38],
		[3, 19, 43, 52]
	],

	[
		[2, 10, 12, 27],
		[13, 16, 24, 26],
		[36, 41, 42, 49],
		[28, 35, 50, 55],
		[7, 11, 29, 46],
		[21, 25, 32, 43],
		[5, 14, 48, 52],
		[56, 19, 34, 38],
		[15, 22, 31, 47],
		[1, 8, 33, 45],
		[17, 23, 37, 40],
		[3, 9, 51, 54],
		[6, 18, 30, 39],
		[4, 20, 44, 53]
	],

	[
		[56, 3, 11, 13],
		[14, 17, 25, 27],
		[37, 42, 43, 50],
		[28, 29, 36, 51],
		[8, 12, 30, 47],
		[22, 26, 33, 44],
		[6, 15, 49, 53],
		[1, 20, 35, 39],
		[16, 23, 32, 48],
		[2, 9, 34, 46],
		[18, 24, 38, 41],
		[4, 10, 52, 55],
		[7, 19, 31, 40],
		[5, 21, 45, 54]
	],

	[
		[1, 4, 12, 14],
		[56, 15, 18, 26],
		[38, 43, 44, 51],
		[29, 30, 37, 52],
		[9, 13, 31, 48],
		[23, 27, 34, 45],
		[7, 16, 50, 54],
		[2, 21, 36, 40],
		[17, 24, 33, 49],
		[3, 10, 35, 47],
		[19, 25, 39, 42],
		[5, 11, 28, 53],
		[8, 20, 32, 41],
		[6, 22, 46, 55]
	],

	[
		[2, 5, 13, 15],
		[1, 16, 19, 27],
		[39, 44, 45, 52],
		[30, 31, 38, 53],
		[10, 14, 32, 49],
		[56, 24, 35, 46],
		[8, 17, 51, 55],
		[3, 22, 37, 41],
		[18, 25, 34, 50],
		[4, 11, 36, 48],
		[20, 26, 40, 43],
		[6, 12, 29, 54],
		[9, 21, 33, 42],
		[7, 23, 28, 47]
	]
]