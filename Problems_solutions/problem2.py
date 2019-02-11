age, name = int(input()), input()

if age > 2:
	human_age = 20 + (age-2)*4
else:
	human_age = age*10

print('%s is %s human years old' % (name, human_age))