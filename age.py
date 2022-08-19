driving = input('Have you ever driven a car?')
if driving != 'yes' and driving != 'no':
	print('please answer yes or no.')
	raise SystemExit

age = input('How old are you?')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('You are pass.')
	else:
		print('It is illegal.')
elif driving == 'no':
	if age >= 18:
		print('you may go for a license')
	else:
		print('it is ok, you may get a license few years later.')