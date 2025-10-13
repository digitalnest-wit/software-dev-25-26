# Grade Book Program

# Create a list of test scores
scores = [85.5, 92.0, 78.0, 90.5, 88.0]

# Display original scores
print("Test Scores:")
print(f"Test 1: {scores[0]}")
print(f"Test 2: {scores[1]}")
print(f"Test 3: {scores[2]}")
print(f"Test 4: {scores[3]}")
print(f"Test 5: {scores[4]}")

# Allow updating a score
print("\nUpdate a test score if needed.")
update = input("Would you like to update a score? (yes/no): ")

if update == "yes":
    test_num = int(input("Which test number? (1-5): "))
    new_score = float(input("Enter new score: "))
    scores[test_num - 1] = new_score
    print(f"\nTest {test_num} updated to {new_score}")

# Calculate total using index access and len()
total = 0
for i in range(len(scores)):
    total = total + scores[i]

# Calculate average
average = total / len(scores)

# Display results
print(f"\nFinal Results:")
print(f"Total points: {total}")
print(f"Number of tests: {len(scores)}")
print(f"Average score: {average:.2f}")
