# ============================================================================
# CODE ALONG: Age Classifier
# Expected behavior: Displays a different message depending on the age of the
# user.
# ============================================================================

age = int(input('Enter your age: '))

if age >= 65:
    print('You are a senior')
elif age >= 21:
    print('You are old enough to drink')
elif age >= 18:
    print('You are an adult')
else:
    print('You are a child')


