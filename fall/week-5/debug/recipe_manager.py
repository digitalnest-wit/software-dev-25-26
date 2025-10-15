# Recipe Manager (BUGGY VERSION)

print("=== Recipe Manager ===\n")

recipe = {
    "name": "Chocolate Chip Cookies",
    "servings": 24,
    "prep_time": 15,
    "cook_time": 12,
    "difficulty": "Easy"
}

ingredients = {
    "flour": "2 cups",
    "sugar": "1 cup",
    "butter": "1 cup",
    "eggs": 2,
    "chocolate chips": "2 cups"
}

# Display recipe info
print(f"Recipe: {recipe['name']}")
print(f"Servings: {recipe['servings']}")
print(f"Total Time: {recipe['prep_time'] + recipe['cook_time']} minutes")

# Bug 1: KeyError - accessing key that doesn't exist
# TODO: Check if the key appears in the dictionary first, before trying to access
# the value.
print(f"Calories: {recipe['calories']}")

# Display ingredients
print("\nIngredients:")
# Bug 2: Missing .items()
# TODO: Use the correct method on the ingredients dict to access the keys and
# values to iterate over them with a for-loop.
for ingredient, amount in ingredients:
    print(f"  - {amount} {ingredient}")

# Update servings
print("\n=== Adjust Recipe ===")
new_servings = int(input("How many servings do you need? "))

# Bug 3: Missing assignment operator
# TODO: Use the correct assignment operator to update the recipe serving size.
recipe["servings"] + new_servings

# Bug 4: Trying to access key that might not exist without .get()
# TODO: Use the get() dict method with a default value of 100.
cook_temp = recipe["temperature"]

# Add cooking instructions
instructions = {
    "Step 1": "Mix dry ingredients",
    "Step 2": "Cream butter and sugar",
    "Step 3": "Add eggs and vanilla",
    "Step 4": "Combine wet and dry ingredients",
    "Step 5": "Add chocolate chips"
}

# Bug 5: Wrong method for checking if key exists
# TODO: What operator should you use to check if a key exists in a dict?
if instructions.has_key("Step 6"):
    print("\nFinal step exists")

# Display updated recipe
print("\n=== Updated Recipe ===")
print(f"Recipe: {recipe['name']}")
print(f"Servings: {recipe['servings']}")
print(f"Difficulty: {recipe['difficulty']}")
print(f"Temperature: {cook_temp}°F")

# Bug 6: Trying to get the number of ingredients incorrectly
# TODO: What built-in function should you use to get the length of an object?
print(f"Number of ingredients: {ingredients.length()}")

print("\nInstructions:")
for step, instruction in instructions.items():
    print(f"  {step}: {instruction}")
