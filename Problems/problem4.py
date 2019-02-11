sentence = input()

while sentence != 'Palindrome!':
	if sentence.lower().replace(' ', '').replace(',', '') == sentence.lower().replace(' ', '').replace(',', '')[::-1]:
		print('"%s" is a palindrome' % sentence)
	else:
		print('"%s" is not a palindrome' % sentence)
	sentence = input()