complements = {'G':'C', 'C':'G', 'T':'A', 'A':'T'}
sequence = input()

while sequence != '.':
	rev_compl = ''.join(complements[char] for char in sequence[::-1])
	print(rev_compl)
	sequence = input()