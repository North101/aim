# adapted from Alice Miller's social golfer page at http://breakoutroom.pythonanywhere.com/allocate/
seats = [
	[
		[1, 28, 41, 46],
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
		[88, 29, 58, 87]
	],

	[
		[1, 3, 43, 48],
		[88, 4, 36, 55],
		[6, 27, 41, 50],
		[10, 23, 40, 51],
		[15, 18, 42, 49],
		[5, 28, 38, 53],
		[8, 25, 45, 46],
		[30, 32, 72, 77],
		[29, 33, 65, 84],
		[35, 56, 70, 79],
		[39, 52, 69, 80],
		[44, 47, 71, 78],
		[34, 57, 67, 82],
		[37, 54, 74, 75],
		[14, 19, 59, 61],
		[7, 26, 58, 62],
		[12, 21, 64, 85],
		[11, 22, 68, 81],
		[13, 20, 73, 76],
		[9, 24, 63, 86],
		[16, 17, 66, 83],
		[2, 31, 60, 87]
	],

	[
		[3, 5, 45, 50],
		[2, 6, 38, 57],
		[88, 8, 43, 52],
		[12, 25, 42, 53],
		[17, 20, 44, 51],
		[1, 7, 40, 55],
		[10, 27, 47, 48],
		[32, 34, 74, 79],
		[31, 35, 67, 86],
		[29, 37, 72, 81],
		[41, 54, 71, 82],
		[46, 49, 73, 80],
		[30, 36, 69, 84],
		[39, 56, 76, 77],
		[16, 21, 61, 63],
		[9, 28, 60, 64],
		[14, 23, 58, 66],
		[13, 24, 70, 83],
		[15, 22, 75, 78],
		[11, 26, 59, 65],
		[18, 19, 68, 85],
		[4, 33, 62, 87]
	],

	[
		[7, 9, 49, 54],
		[6, 10, 32, 42],
		[4, 12, 47, 56],
		[88, 16, 46, 57],
		[21, 24, 48, 55],
		[5, 11, 30, 44],
		[2, 14, 51, 52],
		[36, 38, 78, 83],
		[35, 39, 61, 71],
		[33, 41, 76, 85],
		[29, 45, 75, 86],
		[50, 53, 77, 84],
		[34, 40, 59, 73],
		[31, 43, 80, 81],
		[20, 25, 65, 67],
		[3, 13, 64, 68],
		[18, 27, 62, 70],
		[17, 28, 58, 74],
		[19, 26, 79, 82],
		[1, 15, 63, 69],
		[22, 23, 60, 72],
		[8, 37, 66, 87]
	],

	[
		[15, 17, 33, 57],
		[14, 18, 40, 50],
		[12, 20, 35, 55],
		[8, 24, 36, 54],
		[88, 3, 34, 56],
		[13, 19, 38, 52],
		[10, 22, 30, 31],
		[44, 46, 62, 86],
		[43, 47, 69, 79],
		[41, 49, 64, 84],
		[37, 53, 65, 83],
		[29, 32, 63, 85],
		[42, 48, 67, 81],
		[39, 51, 59, 60],
		[4, 28, 73, 75],
		[11, 21, 72, 76],
		[6, 26, 70, 78],
		[7, 25, 66, 82],
		[5, 27, 58, 61],
		[9, 23, 71, 77],
		[1, 2, 68, 80],
		[16, 45, 74, 87]
	],

	[
		[2, 4, 44, 49],
		[1, 5, 37, 56],
		[7, 28, 42, 51],
		[11, 24, 41, 52],
		[16, 19, 43, 50],
		[88, 6, 39, 54],
		[9, 26, 46, 47],
		[31, 33, 73, 78],
		[30, 34, 66, 85],
		[36, 57, 71, 80],
		[40, 53, 70, 81],
		[45, 48, 72, 79],
		[29, 35, 68, 83],
		[38, 55, 75, 76],
		[15, 20, 60, 62],
		[8, 27, 59, 63],
		[13, 22, 65, 86],
		[12, 23, 69, 82],
		[14, 21, 74, 77],
		[10, 25, 58, 64],
		[17, 18, 67, 84],
		[3, 32, 61, 87]
	],

	[
		[5, 7, 47, 52],
		[4, 8, 30, 40],
		[2, 10, 45, 54],
		[14, 27, 44, 55],
		[19, 22, 46, 53],
		[3, 9, 42, 57],
		[88, 12, 49, 50],
		[34, 36, 76, 81],
		[33, 37, 59, 69],
		[31, 39, 74, 83],
		[43, 56, 73, 84],
		[48, 51, 75, 82],
		[32, 38, 71, 86],
		[29, 41, 78, 79],
		[18, 23, 63, 65],
		[1, 11, 62, 66],
		[16, 25, 60, 68],
		[15, 26, 72, 85],
		[17, 24, 77, 80],
		[13, 28, 61, 67],
		[20, 21, 58, 70],
		[6, 35, 64, 87]
	],

	[
		[11, 13, 29, 53],
		[10, 14, 36, 46],
		[8, 16, 31, 51],
		[4, 20, 32, 50],
		[25, 28, 30, 52],
		[9, 15, 34, 48],
		[6, 18, 55, 56],
		[40, 42, 58, 82],
		[39, 43, 65, 75],
		[37, 45, 60, 80],
		[33, 49, 61, 79],
		[54, 57, 59, 81],
		[38, 44, 63, 77],
		[35, 47, 84, 85],
		[88, 24, 69, 71],
		[7, 17, 68, 72],
		[2, 22, 66, 74],
		[3, 21, 62, 78],
		[1, 23, 83, 86],
		[5, 19, 67, 73],
		[26, 27, 64, 76],
		[12, 41, 70, 87]
	],

	[
		[23, 25, 36, 41],
		[22, 26, 29, 48],
		[20, 28, 34, 43],
		[3, 16, 33, 44],
		[8, 11, 35, 42],
		[21, 27, 31, 46],
		[1, 18, 38, 39],
		[52, 54, 65, 70],
		[51, 55, 58, 77],
		[49, 57, 63, 72],
		[32, 45, 62, 73],
		[37, 40, 64, 71],
		[50, 56, 60, 75],
		[30, 47, 67, 68],
		[7, 12, 81, 83],
		[88, 19, 80, 84],
		[5, 14, 78, 86],
		[4, 15, 61, 74],
		[6, 13, 66, 69],
		[2, 17, 79, 85],
		[9, 10, 59, 76],
		[24, 53, 82, 87]
	],

	[
		[18, 20, 31, 36],
		[17, 21, 43, 53],
		[15, 23, 29, 38],
		[11, 27, 39, 57],
		[3, 6, 30, 37],
		[16, 22, 41, 55],
		[13, 25, 33, 34],
		[47, 49, 60, 65],
		[46, 50, 72, 82],
		[44, 52, 58, 67],
		[40, 56, 68, 86],
		[32, 35, 59, 66],
		[45, 51, 70, 84],
		[42, 54, 62, 63],
		[2, 7, 76, 78],
		[14, 24, 75, 79],
		[88, 9, 73, 81],
		[10, 28, 69, 85],
		[1, 8, 61, 64],
		[12, 26, 74, 80],
		[4, 5, 71, 83],
		[19, 48, 77, 87]
	],

	[
		[8, 10, 50, 55],
		[7, 11, 33, 43],
		[5, 13, 48, 57],
		[1, 17, 29, 47],
		[22, 25, 49, 56],
		[6, 12, 31, 45],
		[3, 15, 52, 53],
		[37, 39, 79, 84],
		[36, 40, 62, 72],
		[34, 42, 77, 86],
		[30, 46, 58, 76],
		[51, 54, 78, 85],
		[35, 41, 60, 74],
		[32, 44, 81, 82],
		[21, 26, 66, 68],
		[4, 14, 65, 69],
		[19, 28, 63, 71],
		[88, 18, 59, 75],
		[20, 27, 80, 83],
		[2, 16, 64, 70],
		[23, 24, 61, 73],
		[9, 38, 67, 87]
	],

	[
		[17, 19, 30, 35],
		[16, 20, 42, 52],
		[14, 22, 37, 57],
		[10, 26, 38, 56],
		[2, 5, 29, 36],
		[15, 21, 40, 54],
		[12, 24, 32, 33],
		[46, 48, 59, 64],
		[45, 49, 71, 81],
		[43, 51, 66, 86],
		[39, 55, 67, 85],
		[31, 34, 58, 65],
		[44, 50, 69, 83],
		[41, 53, 61, 62],
		[1, 6, 75, 77],
		[13, 23, 74, 78],
		[8, 28, 72, 80],
		[9, 27, 68, 84],
		[88, 7, 60, 63],
		[11, 25, 73, 79],
		[3, 4, 70, 82],
		[18, 47, 76, 87]
	],

	[
		[6, 8, 48, 53],
		[5, 9, 31, 41],
		[3, 11, 46, 55],
		[15, 28, 45, 56],
		[20, 23, 47, 54],
		[4, 10, 29, 43],
		[1, 13, 50, 51],
		[35, 37, 77, 82],
		[34, 38, 60, 70],
		[32, 40, 75, 84],
		[44, 57, 74, 85],
		[49, 52, 76, 83],
		[33, 39, 58, 72],
		[30, 42, 79, 80],
		[19, 24, 64, 66],
		[2, 12, 63, 67],
		[17, 26, 61, 69],
		[16, 27, 73, 86],
		[18, 25, 78, 81],
		[88, 14, 62, 68],
		[21, 22, 59, 71],
		[7, 36, 65, 87]
	],

	[
		[13, 15, 31, 55],
		[12, 16, 38, 48],
		[10, 18, 33, 53],
		[6, 22, 34, 52],
		[1, 27, 32, 54],
		[11, 17, 36, 50],
		[8, 20, 29, 57],
		[42, 44, 60, 84],
		[41, 45, 67, 77],
		[39, 47, 62, 82],
		[35, 51, 63, 81],
		[30, 56, 61, 83],
		[40, 46, 65, 79],
		[37, 49, 58, 86],
		[2, 26, 71, 73],
		[9, 19, 70, 74],
		[4, 24, 68, 76],
		[5, 23, 64, 80],
		[3, 25, 59, 85],
		[7, 21, 69, 75],
		[88, 28, 66, 78],
		[14, 43, 72, 87]
	],

	[
		[88, 27, 40, 45],
		[1, 26, 33, 52],
		[3, 24, 38, 47],
		[7, 20, 37, 48],
		[12, 15, 39, 46],
		[2, 25, 35, 50],
		[5, 22, 42, 43],
		[29, 56, 69, 74],
		[30, 55, 62, 81],
		[32, 53, 67, 76],
		[36, 49, 66, 77],
		[41, 44, 68, 75],
		[31, 54, 64, 79],
		[34, 51, 71, 72],
		[11, 16, 58, 85],
		[4, 23, 59, 84],
		[9, 18, 61, 82],
		[8, 19, 65, 78],
		[10, 17, 70, 73],
		[6, 21, 60, 83],
		[13, 14, 63, 80],
		[28, 57, 86, 87]
	],

	[
		[26, 28, 39, 44],
		[88, 25, 32, 51],
		[2, 23, 37, 46],
		[6, 19, 36, 47],
		[11, 14, 38, 45],
		[1, 24, 34, 49],
		[4, 21, 41, 42],
		[55, 57, 68, 73],
		[29, 54, 61, 80],
		[31, 52, 66, 75],
		[35, 48, 65, 76],
		[40, 43, 67, 74],
		[30, 53, 63, 78],
		[33, 50, 70, 71],
		[10, 15, 84, 86],
		[3, 22, 58, 83],
		[8, 17, 60, 81],
		[7, 18, 64, 77],
		[9, 16, 69, 72],
		[5, 20, 59, 82],
		[12, 13, 62, 79],
		[27, 56, 85, 87]
	],

	[
		[24, 26, 37, 42],
		[23, 27, 30, 49],
		[88, 21, 35, 44],
		[4, 17, 34, 45],
		[9, 12, 36, 43],
		[22, 28, 32, 47],
		[2, 19, 39, 40],
		[53, 55, 66, 71],
		[52, 56, 59, 78],
		[29, 50, 64, 73],
		[33, 46, 63, 74],
		[38, 41, 65, 72],
		[51, 57, 61, 76],
		[31, 48, 68, 69],
		[8, 13, 82, 84],
		[1, 20, 81, 85],
		[6, 15, 58, 79],
		[5, 16, 62, 75],
		[7, 14, 67, 70],
		[3, 18, 80, 86],
		[10, 11, 60, 77],
		[25, 54, 83, 87]
	],

	[
		[20, 22, 33, 38],
		[19, 23, 45, 55],
		[17, 25, 31, 40],
		[88, 13, 30, 41],
		[5, 8, 32, 39],
		[18, 24, 43, 57],
		[15, 27, 35, 36],
		[49, 51, 62, 67],
		[48, 52, 74, 84],
		[46, 54, 60, 69],
		[29, 42, 59, 70],
		[34, 37, 61, 68],
		[47, 53, 72, 86],
		[44, 56, 64, 65],
		[4, 9, 78, 80],
		[16, 26, 77, 81],
		[2, 11, 75, 83],
		[1, 12, 58, 71],
		[3, 10, 63, 66],
		[14, 28, 76, 82],
		[6, 7, 73, 85],
		[21, 50, 79, 87]
	],

	[
		[12, 14, 30, 54],
		[11, 15, 37, 47],
		[9, 17, 32, 52],
		[5, 21, 33, 51],
		[88, 26, 31, 53],
		[10, 16, 35, 49],
		[7, 19, 56, 57],
		[41, 43, 59, 83],
		[40, 44, 66, 76],
		[38, 46, 61, 81],
		[34, 50, 62, 80],
		[29, 55, 60, 82],
		[39, 45, 64, 78],
		[36, 48, 85, 86],
		[1, 25, 70, 72],
		[8, 18, 69, 73],
		[3, 23, 67, 75],
		[4, 22, 63, 79],
		[2, 24, 58, 84],
		[6, 20, 68, 74],
		[27, 28, 65, 77],
		[13, 42, 71, 87]
	],

	[
		[25, 27, 38, 43],
		[24, 28, 31, 50],
		[1, 22, 36, 45],
		[5, 18, 35, 46],
		[10, 13, 37, 44],
		[88, 23, 33, 48],
		[3, 20, 40, 41],
		[54, 56, 67, 72],
		[53, 57, 60, 79],
		[30, 51, 65, 74],
		[34, 47, 64, 75],
		[39, 42, 66, 73],
		[29, 52, 62, 77],
		[32, 49, 69, 70],
		[9, 14, 83, 85],
		[2, 21, 82, 86],
		[7, 16, 59, 80],
		[6, 17, 63, 76],
		[8, 15, 68, 71],
		[4, 19, 58, 81],
		[11, 12, 61, 78],
		[26, 55, 84, 87]
	],

	[
		[22, 24, 35, 40],
		[21, 25, 47, 57],
		[19, 27, 33, 42],
		[2, 15, 32, 43],
		[7, 10, 34, 41],
		[20, 26, 30, 45],
		[88, 17, 37, 38],
		[51, 53, 64, 69],
		[50, 54, 76, 86],
		[48, 56, 62, 71],
		[31, 44, 61, 72],
		[36, 39, 63, 70],
		[49, 55, 59, 74],
		[29, 46, 66, 67],
		[6, 11, 80, 82],
		[18, 28, 79, 83],
		[4, 13, 77, 85],
		[3, 14, 60, 73],
		[5, 12, 65, 68],
		[1, 16, 78, 84],
		[8, 9, 58, 75],
		[23, 52, 81, 87]
	],

	[
		[16, 18, 29, 34],
		[15, 19, 41, 51],
		[13, 21, 36, 56],
		[9, 25, 37, 55],
		[1, 4, 35, 57],
		[14, 20, 39, 53],
		[11, 23, 31, 32],
		[45, 47, 58, 63],
		[44, 48, 70, 80],
		[42, 50, 65, 85],
		[38, 54, 66, 84],
		[30, 33, 64, 86],
		[43, 49, 68, 82],
		[40, 52, 60, 61],
		[88, 5, 74, 76],
		[12, 22, 73, 77],
		[7, 27, 71, 79],
		[8, 26, 67, 83],
		[6, 28, 59, 62],
		[10, 24, 72, 78],
		[2, 3, 69, 81],
		[17, 46, 75, 87]
	],

	[
		[4, 6, 46, 51],
		[3, 7, 29, 39],
		[1, 9, 44, 53],
		[13, 26, 43, 54],
		[18, 21, 45, 52],
		[2, 8, 41, 56],
		[11, 28, 48, 49],
		[33, 35, 75, 80],
		[32, 36, 58, 68],
		[30, 38, 73, 82],
		[42, 55, 72, 83],
		[47, 50, 74, 81],
		[31, 37, 70, 85],
		[40, 57, 77, 78],
		[17, 22, 62, 64],
		[88, 10, 61, 65],
		[15, 24, 59, 67],
		[14, 25, 71, 84],
		[16, 23, 76, 79],
		[12, 27, 60, 66],
		[19, 20, 69, 86],
		[5, 34, 63, 87]
	],

	[
		[9, 11, 51, 56],
		[8, 12, 34, 44],
		[6, 14, 29, 49],
		[2, 18, 30, 48],
		[23, 26, 50, 57],
		[7, 13, 32, 46],
		[4, 16, 53, 54],
		[38, 40, 80, 85],
		[37, 41, 63, 73],
		[35, 43, 58, 78],
		[31, 47, 59, 77],
		[52, 55, 79, 86],
		[36, 42, 61, 75],
		[33, 45, 82, 83],
		[22, 27, 67, 69],
		[5, 15, 66, 70],
		[88, 20, 64, 72],
		[1, 19, 60, 76],
		[21, 28, 81, 84],
		[3, 17, 65, 71],
		[24, 25, 62, 74],
		[10, 39, 68, 87]
	],

	[
		[19, 21, 32, 37],
		[18, 22, 44, 54],
		[16, 24, 30, 39],
		[12, 28, 29, 40],
		[4, 7, 31, 38],
		[17, 23, 42, 56],
		[14, 26, 34, 35],
		[48, 50, 61, 66],
		[47, 51, 73, 83],
		[45, 53, 59, 68],
		[41, 57, 58, 69],
		[33, 36, 60, 67],
		[46, 52, 71, 85],
		[43, 55, 63, 64],
		[3, 8, 77, 79],
		[15, 25, 76, 80],
		[1, 10, 74, 82],
		[88, 11, 70, 86],
		[2, 9, 62, 65],
		[13, 27, 75, 81],
		[5, 6, 72, 84],
		[20, 49, 78, 87]
	],

	[
		[10, 12, 52, 57],
		[9, 13, 35, 45],
		[7, 15, 30, 50],
		[3, 19, 31, 49],
		[24, 27, 29, 51],
		[8, 14, 33, 47],
		[5, 17, 54, 55],
		[39, 41, 81, 86],
		[38, 42, 64, 74],
		[36, 44, 59, 79],
		[32, 48, 60, 78],
		[53, 56, 58, 80],
		[37, 43, 62, 76],
		[34, 46, 83, 84],
		[23, 28, 68, 70],
		[6, 16, 67, 71],
		[1, 21, 65, 73],
		[2, 20, 61, 77],
		[88, 22, 82, 85],
		[4, 18, 66, 72],
		[25, 26, 63, 75],
		[11, 40, 69, 87]
	],

	[
		[21, 23, 34, 39],
		[20, 24, 46, 56],
		[18, 26, 32, 41],
		[1, 14, 31, 42],
		[6, 9, 33, 40],
		[19, 25, 29, 44],
		[16, 28, 36, 37],
		[50, 52, 63, 68],
		[49, 53, 75, 85],
		[47, 55, 61, 70],
		[30, 43, 60, 71],
		[35, 38, 62, 69],
		[48, 54, 58, 73],
		[45, 57, 65, 66],
		[5, 10, 79, 81],
		[17, 27, 78, 82],
		[3, 12, 76, 84],
		[2, 13, 59, 72],
		[4, 11, 64, 67],
		[88, 15, 77, 83],
		[7, 8, 74, 86],
		[22, 51, 80, 87]
	],

	[
		[14, 16, 32, 56],
		[13, 17, 39, 49],
		[11, 19, 34, 54],
		[7, 23, 35, 53],
		[2, 28, 33, 55],
		[12, 18, 37, 51],
		[9, 21, 29, 30],
		[43, 45, 61, 85],
		[42, 46, 68, 78],
		[40, 48, 63, 83],
		[36, 52, 64, 82],
		[31, 57, 62, 84],
		[41, 47, 66, 80],
		[38, 50, 58, 59],
		[3, 27, 72, 74],
		[10, 20, 71, 75],
		[5, 25, 69, 77],
		[6, 24, 65, 81],
		[4, 26, 60, 86],
		[8, 22, 70, 76],
		[88, 1, 67, 79],
		[15, 44, 73, 87]
	],

	[
		[88, 2, 42, 47],
		[3, 28, 35, 54],
		[5, 26, 40, 49],
		[9, 22, 39, 50],
		[14, 17, 41, 48],
		[4, 27, 37, 52],
		[7, 24, 44, 45],
		[29, 31, 71, 76],
		[32, 57, 64, 83],
		[34, 55, 69, 78],
		[38, 51, 68, 79],
		[43, 46, 70, 77],
		[33, 56, 66, 81],
		[36, 53, 73, 74],
		[13, 18, 58, 60],
		[6, 25, 61, 86],
		[11, 20, 63, 84],
		[10, 21, 67, 80],
		[12, 19, 72, 75],
		[8, 23, 62, 85],
		[15, 16, 65, 82],
		[1, 30, 59, 87]
	]
]