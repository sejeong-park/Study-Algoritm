

order = [189, 404, 178, 391, 318, 216, 110, 120, 352, 327, 234, 56, 411, 247, 458, 367, 406, 139, 75, 117, 484, 326, 323, 36, 343, 27, 389, 5, 39, 197, 304, 153, 357, 303, 383, 293, 301, 161, 422, 229, 324, 331, 4, 134, 488, 322, 38, 49, 344, 500, 355, 233, 354, 325, 289, 369, 81, 192, 47, 84, 61, 191, 260, 208, 374, 440, 89, 71, 159, 361, 259, 100, 6, 42, 58, 381, 8, 379, 403, 263, 489, 33, 498, 131, 40, 99, 285, 495, 333, 436, 430, 459, 215, 393, 172, 423, 428, 402, 292, 140, 433, 265, 167, 253, 148, 207, 275, 52, 338, 74, 185, 262, 149, 341, 214, 351, 473, 30, 366, 225, 109, 492, 113, 24, 77, 108, 170, 486, 23, 44, 407, 62, 142, 82, 359, 31, 198, 128, 114, 315, 124, 251, 290, 43, 118, 368, 230, 427, 493, 370, 158, 55, 206, 34, 442, 279, 96, 485, 408, 312, 203, 135, 20, 269, 165, 119, 240, 497, 22, 106, 417, 465, 431, 228, 221, 111, 146, 321, 250, 213, 297, 306, 469, 467, 220, 104, 222, 211, 123, 276, 70, 311, 85, 464, 143, 125, 294, 386, 372, 419, 447, 305, 476, 116, 460, 2, 481, 17, 414, 313, 268, 160, 150, 295, 195, 175, 452, 205, 380, 416, 496, 457, 307, 278, 477, 463, 231, 365, 387, 472, 63, 115, 272, 171, 155, 320, 163, 426, 21, 180, 277, 482, 401, 287, 494, 257, 439, 156, 169, 166, 184, 88, 181, 362, 453, 194, 37, 50, 363, 204, 210, 300, 224, 273, 15, 358, 398, 121, 16, 90, 151, 227, 60, 102, 45, 252, 122, 79, 284, 377, 168, 141, 101, 80, 235, 218, 353, 54, 382, 441, 329, 340, 347, 258, 14, 335, 48, 236, 255, 345, 378, 342, 291, 186, 360, 412, 212, 308, 444, 274, 443, 397, 97, 483, 270, 242, 200, 107, 400, 12, 456, 190, 479, 7, 182, 73, 25, 201, 65, 432, 136, 196, 349, 132, 187, 91, 32, 480, 226, 281, 18, 388, 299, 241, 399, 237, 68, 244, 238, 438, 72, 421, 3, 209, 475, 455, 435, 471, 373, 499, 283, 376, 316, 127, 409, 9, 280, 264, 434, 28, 138, 462, 126, 76, 468, 179, 248, 267, 162, 57, 448, 371, 298, 29, 288, 249, 254, 470, 245, 105, 94, 466, 103, 461, 445, 271, 385, 176, 328, 202, 286, 64, 183, 396, 437, 152, 415, 296, 112, 314, 395, 413, 302, 319, 223, 1, 451, 51, 177, 478, 98, 243, 384, 310, 137, 35, 219, 92, 346, 95, 410, 69, 392, 350, 67, 239, 157, 19, 261, 10, 332, 429, 41, 330, 130, 487, 174, 491, 309, 424, 53, 129, 246, 317, 356, 336, 83, 154, 450, 217, 26, 78, 375, 144, 266, 147, 133, 339, 446, 282, 454, 348, 337, 164, 11, 87, 66, 405, 13, 46, 334, 364, 86, 193, 173, 418, 425, 490, 93, 199, 232, 188, 256, 394, 474, 449, 420, 145, 390, 59]
source = "kdjmkmclljkljldaiagciafbibbenhmjajabllhbcifneiffjncablkbnaidcikgjmfakkdfknekjkhmgllnigfhdejnmhildjkbdamnkaeejdbgfilmhijgjdnmjakllecnbmbbfngfjmgekmmmhmflfficfnegilekhelaeajdafglhebjjcigbjfghnkijggblhjbaididkhggmnjidkdidlhljicmmlachdeidbakjhhmfimchnmfacbkfcmiidjknedlmnkimmihhbagneigcebbdndeenindnbikhdddbkhccefldkkhkgghmjcgjbnmebkekemddmhdkhdegkkkdkfneaclbnghbbhbfmkafaggejckjgencgcjbdcjnhbhdcmkbalbflgjcfnfljjgfigfgmmeemfjlhmenkfhhgdlacgdafgihaabcjjfhflidcjlagflifdlamidabdhgccebkglnaljikgbfddmlknidn"
target= "kmkkfkkejjjafakgkkkkkkbkknkladjk"

def getMaximumRemovals(order, source, target):
    # Write your code here
	result = 0
	source_list = list(source)
	target_dict = dict()
	for i in target:
		target_dict[i] = target_dict.get(i,0) + 1

	total_cnt = sum([value for value in target_dict.values()])
	print(target_dict)
	for order_num in order:
		source_list[order_num-1] = '-'
		new_source = ''.join(source_list)
		# print(new_source)
		source_dict = dict()
		for i in new_source:
			source_dict[i] = source_dict.get(i,0) + 1
		cnt = 0
		for key, value in target_dict.items():
			if key in source_dict.keys():
				if source_dict[key] >= value:
					cnt+=1

		if cnt == len(list(target_dict.keys())):
			result += 1

	return result




print(getMaximumRemovals(order, source, target))

