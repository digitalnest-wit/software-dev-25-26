# A program that determines scholarship eligibility based on GPA, income, major, and extracurriculars

gpa = float(input('Enter GPA: '))
monthly_income = float(input('Enter monthly income: $'))
major = input('Enter study major: ').strip().lower()
num_extracurriculars = int(input('How many extracurriculuars are you involved in? '))

print()

# Scholarship A:
# Eligibile applicants must have at least a 3.0 GPA, make less than $2,000 per month, and
# be majoring in linguistics, and participate in at least 1 extracurricular.
is_eligible_for_a = gpa >= 3.0 and monthly_income < 2000 and major == 'linguistics' and num_extracurriculars >= 1
if is_eligible_for_a:
    print('Eligible for Scholarship A')

# Scholarship B:
# Eligibile applicants must have at least a 4.0 GPA, make less than $3,000 per month, and
# be majoring in computer science.
is_eligible_for_b = gpa >= 4.0 and monthly_income < 3000 and major == 'computer science'
if is_eligible_for_b:
    print('Eligible for Scholarship B')

# Scholarship C:
# Eligibile applicants must have at least a 3.5 GPA, make less than $2,500 per month, and
# participate in at least 2 extracurriculars.
is_eligible_for_c = gpa >= 3.5 and monthly_income < 2500 and num_extracurriculars >= 2
if is_eligible_for_c:
    print('Eligible for Scholarship C')
