# Recipe Manager

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
    "chocolate_chips": "2 cups"
}

# Display recipe info
print(f"Recipe: {recipe['name']}")
print(f"Servings: {recipe['servings']}")
print(f"Total Time: {recipe['prep_time'] + recipe['cook_time']} minutes")

# Bug 1: KeyError - accessing key that doesn't exist
if 'calories' in recipe:
    print(f"Calories: {recipe['calories']}")

# Display ingredients
print("\nIngredients:")
# Bug 2: Missing .items()
for ingredient, amount in ingredients.items():
    print(f"  - {amount} {ingredient}")

# Bug 3: Wrong syntax for adding new ingredient
ingredients["vanilla_extract"] = "1 tsp"

# Update servings
print("\n=== Adjust Recipe ===")
new_servings = int(input("How many additional servings do you need? "))

# Bug 4: Missing assignment operator
recipe["servings"] += new_servings

# Bug 5: Trying to access key that might not exist without .get()
cook_temp = recipe.get("temperature", 100)

# Add cooking instructions
instructions = {
    "Step 1": "Mix dry ingredients",
    "Step 2": "Cream butter and sugar",
    "Step 3": "Add eggs and vanilla",
    "Step 4": "Combine wet and dry ingredients",
    "Step 5": "Add chocolate chips"
}

# Bug 6: Wrong method for checking if key exists
if "Step 6" in instructions:
    print("\nFinal step exists")

# Display updated recipe
print("\n=== Updated Recipe ===")
print(f"Recipe: {recipe['name']}")
print(f"Servings: {recipe['servings']}")
print(f"Difficulty: {recipe['difficulty']}")
print(f"Temperature: {cook_temp}°F")

# Bug 7: Trying to get number of ingredients incorrectly
print(f"Number of ingredients: {len(ingredients)}")

print("\nInstructions:")
for step, instruction in instructions.items():
    print(f"  {step}: {instruction}")
