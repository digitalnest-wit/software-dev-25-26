banner = f'''
+{'-' * 48}+
|{'Private Club Entry Kiosk'.center(48)}|
|{' ' * 48}|
|{' A program that may or may not grant the'.ljust(48)}|
|{' user access into a private club.'.ljust(48)}|
|{' ' * 48}|
|{' ~ ' * 16}|
'''
print(banner)

age = int(input('| How old are you? '))
print()

has_id = input('| Do you have your ID with you? ').lower().find('y') >= 0
print()

is_wearing_shoes = input('| Are you wearing shoes? ').lower().find('y') >= 0
print()

is_vip = input('| Are you in the VIP list? ').lower().find('y') >= 0
print()

knows_secret = input('| What\'s the secret password? ').strip() == 'pickles'
print()

satisfies_rule_1 = age >= 21 and has_id and is_wearing_shoes
satisfies_rule_2 = is_vip or knows_secret
satisfies_rule_3 = is_wearing_shoes

if satisfies_rule_3 and (satisfies_rule_2 or satisfies_rule_1):
	print('| * You\'re in!')
else:
	print('| * Access denied.'.ljust(47), ' |')

footer  = f'''
|{' ~ ' * 16}|
|{' ' * 48}|
+{'-' * 48}+
'''
print(footer)
