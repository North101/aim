# adapted from Alice Miller's social golfer page at http://breakoutroom.pythonanywhere.com/allocate/
seats = [
	[
		[68, 1, 9, 63],
		[7, 19, 29, 43],
		[17, 21, 26, 45],
		[3, 18, 38, 64],
		[46, 47, 49, 55],
		[11, 35, 41, 48],
		[2, 25, 51, 57],
		[4, 27, 52, 59],
		[5, 6, 8, 20],
		[10, 24, 37, 54],
		[30, 40, 56, 61],
		[23, 39, 58, 62],
		[15, 22, 33, 60],
		[16, 31, 44, 65],
		[13, 32, 42, 50],
		[12, 28, 53, 67],
		[14, 34, 36, 66]
	],

	[
		[68, 3, 4, 12],
		[10, 22, 32, 46],
		[20, 24, 29, 48],
		[1, 6, 21, 41],
		[49, 50, 52, 58],
		[14, 38, 44, 51],
		[5, 28, 54, 60],
		[7, 30, 55, 62],
		[8, 9, 11, 23],
		[13, 27, 40, 57],
		[33, 43, 59, 64],
		[26, 42, 61, 65],
		[18, 25, 36, 63],
		[2, 19, 34, 47],
		[16, 35, 45, 53],
		[15, 31, 56, 67],
		[17, 37, 39, 66]
	],

	[
		[3, 6, 7, 15],
		[13, 25, 35, 49],
		[23, 27, 32, 51],
		[4, 9, 24, 44],
		[52, 53, 55, 61],
		[17, 41, 47, 54],
		[8, 31, 57, 63],
		[10, 33, 58, 65],
		[11, 12, 14, 26],
		[16, 30, 43, 60],
		[1, 36, 46, 62],
		[2, 29, 45, 64],
		[68, 21, 28, 39],
		[5, 22, 37, 50],
		[19, 38, 48, 56],
		[18, 34, 59, 67],
		[20, 40, 42, 66]
	],

	[
		[6, 9, 10, 18],
		[16, 28, 38, 52],
		[26, 30, 35, 54],
		[7, 12, 27, 47],
		[55, 56, 58, 64],
		[20, 44, 50, 57],
		[68, 11, 34, 60],
		[2, 13, 36, 61],
		[14, 15, 17, 29],
		[19, 33, 46, 63],
		[4, 39, 49, 65],
		[1, 5, 32, 48],
		[3, 24, 31, 42],
		[8, 25, 40, 53],
		[22, 41, 51, 59],
		[21, 37, 62, 67],
		[23, 43, 45, 66]
	],

	[
		[9, 12, 13, 21],
		[19, 31, 41, 55],
		[29, 33, 38, 57],
		[10, 15, 30, 50],
		[1, 58, 59, 61],
		[23, 47, 53, 60],
		[3, 14, 37, 63],
		[5, 16, 39, 64],
		[17, 18, 20, 32],
		[68, 22, 36, 49],
		[2, 7, 42, 52],
		[4, 8, 35, 51],
		[6, 27, 34, 45],
		[11, 28, 43, 56],
		[25, 44, 54, 62],
		[24, 40, 65, 67],
		[26, 46, 48, 66]
	],

	[
		[12, 15, 16, 24],
		[22, 34, 44, 58],
		[32, 36, 41, 60],
		[13, 18, 33, 53],
		[4, 61, 62, 64],
		[26, 50, 56, 63],
		[68, 6, 17, 40],
		[1, 8, 19, 42],
		[20, 21, 23, 35],
		[3, 25, 39, 52],
		[5, 10, 45, 55],
		[7, 11, 38, 54],
		[9, 30, 37, 48],
		[14, 31, 46, 59],
		[28, 47, 57, 65],
		[2, 27, 43, 67],
		[29, 49, 51, 66]
	],

	[
		[15, 18, 19, 27],
		[25, 37, 47, 61],
		[35, 39, 44, 63],
		[16, 21, 36, 56],
		[1, 7, 64, 65],
		[68, 29, 53, 59],
		[3, 9, 20, 43],
		[4, 11, 22, 45],
		[23, 24, 26, 38],
		[6, 28, 42, 55],
		[8, 13, 48, 58],
		[10, 14, 41, 57],
		[12, 33, 40, 51],
		[17, 34, 49, 62],
		[2, 31, 50, 60],
		[5, 30, 46, 67],
		[32, 52, 54, 66]
	],

	[
		[18, 21, 22, 30],
		[28, 40, 50, 64],
		[68, 38, 42, 47],
		[19, 24, 39, 59],
		[1, 2, 4, 10],
		[3, 32, 56, 62],
		[6, 12, 23, 46],
		[7, 14, 25, 48],
		[26, 27, 29, 41],
		[9, 31, 45, 58],
		[11, 16, 51, 61],
		[13, 17, 44, 60],
		[15, 36, 43, 54],
		[20, 37, 52, 65],
		[5, 34, 53, 63],
		[8, 33, 49, 67],
		[35, 55, 57, 66]
	],

	[
		[21, 24, 25, 33],
		[1, 31, 43, 53],
		[3, 41, 45, 50],
		[22, 27, 42, 62],
		[4, 5, 7, 13],
		[6, 35, 59, 65],
		[9, 15, 26, 49],
		[10, 17, 28, 51],
		[29, 30, 32, 44],
		[12, 34, 48, 61],
		[14, 19, 54, 64],
		[16, 20, 47, 63],
		[18, 39, 46, 57],
		[2, 23, 40, 55],
		[68, 8, 37, 56],
		[11, 36, 52, 67],
		[38, 58, 60, 66]
	],

	[
		[24, 27, 28, 36],
		[4, 34, 46, 56],
		[6, 44, 48, 53],
		[25, 30, 45, 65],
		[7, 8, 10, 16],
		[2, 9, 38, 62],
		[12, 18, 29, 52],
		[13, 20, 31, 54],
		[32, 33, 35, 47],
		[15, 37, 51, 64],
		[1, 17, 22, 57],
		[68, 19, 23, 50],
		[21, 42, 49, 60],
		[5, 26, 43, 58],
		[3, 11, 40, 59],
		[14, 39, 55, 67],
		[41, 61, 63, 66]
	],

	[
		[27, 30, 31, 39],
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
		[68, 44, 64, 66]
	],

	[
		[30, 33, 34, 42],
		[10, 40, 52, 62],
		[12, 50, 54, 59],
		[5, 31, 36, 51],
		[13, 14, 16, 22],
		[2, 8, 15, 44],
		[18, 24, 35, 58],
		[19, 26, 37, 60],
		[38, 39, 41, 53],
		[4, 21, 43, 57],
		[7, 23, 28, 63],
		[6, 25, 29, 56],
		[68, 27, 48, 55],
		[11, 32, 49, 64],
		[9, 17, 46, 65],
		[20, 45, 61, 67],
		[1, 3, 47, 66]
	],

	[
		[33, 36, 37, 45],
		[13, 43, 55, 65],
		[15, 53, 57, 62],
		[8, 34, 39, 54],
		[16, 17, 19, 25],
		[5, 11, 18, 47],
		[21, 27, 38, 61],
		[22, 29, 40, 63],
		[41, 42, 44, 56],
		[7, 24, 46, 60],
		[68, 10, 26, 31],
		[9, 28, 32, 59],
		[3, 30, 51, 58],
		[1, 14, 35, 52],
		[2, 12, 20, 49],
		[23, 48, 64, 67],
		[4, 6, 50, 66]
	],

	[
		[36, 39, 40, 48],
		[2, 16, 46, 58],
		[18, 56, 60, 65],
		[11, 37, 42, 57],
		[19, 20, 22, 28],
		[8, 14, 21, 50],
		[24, 30, 41, 64],
		[68, 25, 32, 43],
		[44, 45, 47, 59],
		[10, 27, 49, 63],
		[3, 13, 29, 34],
		[12, 31, 35, 62],
		[6, 33, 54, 61],
		[4, 17, 38, 55],
		[5, 15, 23, 52],
		[1, 26, 51, 67],
		[7, 9, 53, 66]
	],

	[
		[39, 42, 43, 51],
		[5, 19, 49, 61],
		[2, 21, 59, 63],
		[14, 40, 45, 60],
		[22, 23, 25, 31],
		[11, 17, 24, 53],
		[1, 27, 33, 44],
		[3, 28, 35, 46],
		[47, 48, 50, 62],
		[68, 13, 30, 52],
		[6, 16, 32, 37],
		[15, 34, 38, 65],
		[9, 36, 57, 64],
		[7, 20, 41, 58],
		[8, 18, 26, 55],
		[4, 29, 54, 67],
		[10, 12, 56, 66]
	],

	[
		[42, 45, 46, 54],
		[8, 22, 52, 64],
		[68, 5, 24, 62],
		[17, 43, 48, 63],
		[25, 26, 28, 34],
		[14, 20, 27, 56],
		[4, 30, 36, 47],
		[6, 31, 38, 49],
		[50, 51, 53, 65],
		[3, 16, 33, 55],
		[9, 19, 35, 40],
		[2, 18, 37, 41],
		[1, 12, 39, 60],
		[10, 23, 44, 61],
		[11, 21, 29, 58],
		[7, 32, 57, 67],
		[13, 15, 59, 66]
	],

	[
		[45, 48, 49, 57],
		[1, 11, 25, 55],
		[3, 8, 27, 65],
		[68, 20, 46, 51],
		[28, 29, 31, 37],
		[17, 23, 30, 59],
		[7, 33, 39, 50],
		[9, 34, 41, 52],
		[2, 53, 54, 56],
		[6, 19, 36, 58],
		[12, 22, 38, 43],
		[5, 21, 40, 44],
		[4, 15, 42, 63],
		[13, 26, 47, 64],
		[14, 24, 32, 61],
		[10, 35, 60, 67],
		[16, 18, 62, 66]
	],

	[
		[48, 51, 52, 60],
		[4, 14, 28, 58],
		[2, 6, 11, 30],
		[3, 23, 49, 54],
		[31, 32, 34, 40],
		[20, 26, 33, 62],
		[10, 36, 42, 53],
		[12, 37, 44, 55],
		[5, 56, 57, 59],
		[9, 22, 39, 61],
		[15, 25, 41, 46],
		[8, 24, 43, 47],
		[68, 7, 18, 45],
		[1, 16, 29, 50],
		[17, 27, 35, 64],
		[13, 38, 63, 67],
		[19, 21, 65, 66]
	],

	[
		[51, 54, 55, 63],
		[7, 17, 31, 61],
		[5, 9, 14, 33],
		[6, 26, 52, 57],
		[34, 35, 37, 43],
		[23, 29, 36, 65],
		[13, 39, 45, 56],
		[15, 40, 47, 58],
		[8, 59, 60, 62],
		[12, 25, 42, 64],
		[18, 28, 44, 49],
		[11, 27, 46, 50],
		[3, 10, 21, 48],
		[4, 19, 32, 53],
		[1, 20, 30, 38],
		[68, 16, 41, 67],
		[2, 22, 24, 66]
	],

	[
		[68, 54, 57, 58],
		[10, 20, 34, 64],
		[8, 12, 17, 36],
		[9, 29, 55, 60],
		[37, 38, 40, 46],
		[2, 26, 32, 39],
		[16, 42, 48, 59],
		[18, 43, 50, 61],
		[11, 62, 63, 65],
		[1, 15, 28, 45],
		[21, 31, 47, 52],
		[14, 30, 49, 53],
		[6, 13, 24, 51],
		[7, 22, 35, 56],
		[4, 23, 33, 41],
		[3, 19, 44, 67],
		[5, 25, 27, 66]
	],

	[
		[3, 57, 60, 61],
		[1, 13, 23, 37],
		[11, 15, 20, 39],
		[12, 32, 58, 63],
		[40, 41, 43, 49],
		[5, 29, 35, 42],
		[19, 45, 51, 62],
		[21, 46, 53, 64],
		[68, 2, 14, 65],
		[4, 18, 31, 48],
		[24, 34, 50, 55],
		[17, 33, 52, 56],
		[9, 16, 27, 54],
		[10, 25, 38, 59],
		[7, 26, 36, 44],
		[6, 22, 47, 67],
		[8, 28, 30, 66]
	],

	[
		[6, 60, 63, 64],
		[4, 16, 26, 40],
		[14, 18, 23, 42],
		[68, 15, 35, 61],
		[43, 44, 46, 52],
		[8, 32, 38, 45],
		[22, 48, 54, 65],
		[1, 24, 49, 56],
		[2, 3, 5, 17],
		[7, 21, 34, 51],
		[27, 37, 53, 58],
		[20, 36, 55, 59],
		[12, 19, 30, 57],
		[13, 28, 41, 62],
		[10, 29, 39, 47],
		[9, 25, 50, 67],
		[11, 31, 33, 66]
	]
]