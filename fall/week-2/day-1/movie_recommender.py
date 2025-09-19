
# ============================================================================
# CHALLENGE: Movie Recommender
# Expected behavior: Recommends a movie based on the user's age and genre
# preference.
# ============================================================================

print('Welcome to Movie Recommender')
print('I\'ll recommend you a movie based on your age and genre preference.')
print()

age = int(input('Enter your age: '))
genre = input('Enter a genre (action, comedy, or horror): ')

print()

if age >= 18:
	if genre == 'action':
		print('I recommend Kill Bill Vol. 1 (2003)')
	elif genre == 'comedy':
		print('I recommend Mean Girls (2004)')
	elif genre == 'horror':	
		print('I recommend Us (2019)')
	else:	
		print('I don\'t recognize that genre.')
else:
	if genre == 'action':	
		print('I recommend The Incredibles (2004)')
	elif genre == 'comedy':
		print('I recommend Bee Movie (2007)')
	elif genre == 'horror':
		print('I recommend Coraline (2009)')
	else:
		print('I don\'t recognize that genre.')


