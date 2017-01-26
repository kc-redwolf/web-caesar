def alphabet_position(letter):
	''' Return the position of a given letter in alphabet. '''
	abc_lst = 'abcdefghijklmnopqrstuvwxyz'
	letter = letter.lower()
	if letter in abc_lst:
		abc_pos = abc_lst.index(letter)
		return abc_pos


def rotate_character(char,rot):
	''' Return the result of rotating char by rot number of places to the right. '''
	low_abc = 'abcdefghijklmnopqrstuvwxyz'
	up_abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	if char.isalpha():
		curr_char_pos = int(alphabet_position(char))
		rot_char_pos = int((curr_char_pos + rot) % 26)
		if char.islower():
			rot_char = low_abc[rot_char_pos]
		else:
			rot_char = up_abc[rot_char_pos]
		return rot_char
	else:
		if not char.isalpha():
			return char


def encrypt(text, rot):
	''' Return the result of rotating each letter in the text by rot places to the right. '''
	encrypted_text = ''
	idx = 0
	for ea_char in text:
		old_char = text[idx]
		if old_char.isalpha():
			new_char = rotate_character(old_char, rot)
			encrypted_text += new_char
		else:
			encrypted_text += old_char
		idx += 1
	return encrypted_text
