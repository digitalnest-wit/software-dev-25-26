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

# Display the 'calories' for this recipe.
print(f"Calories: {recipe['calories']}")

print("\nIngredients:")

# Display each ingredient and the portion amount
for ingredient, amount in ingredients:
    print(f"  - {amount} {ingredient}")

print("\n=== Adjust Recipe ===")

new_servings = int(input("How many additional servings do you need? "))

# Update the recipe serving size by an additional amount
recipe["servings"] + new_servings

# Get the 'temperature' for the recipe. If no temperature is provided for the
# recipe, use a default value of 300.
cook_temp = recipe["temperature"]

# Add cooking instructions
instructions = {
    "Step 1": "Mix dry ingredients",
    "Step 2": "Cream butter and sugar",
    "Step 3": "Add eggs and vanilla",
    "Step 4": "Combine wet and dry ingredients",
    "Step 5": "Add chocolate chips"
}

# Check if there is such thing as a 'Step 6' in the ingredients dict.
if instructions.has_key("Step 6"):
    print("\nSix steps for a recipe is crazyyy")

# Display updated recipe
print("\n=== Updated Recipe ===")
print(f"Recipe: {recipe['name']}")
print(f"Servings: {recipe['servings']}")
print(f"Difficulty: {recipe['difficulty']}")
print(f"Temperature: {cook_temp}°F")

# Display the number of ingredients by accessing the dict's length.
print(f"Number of ingredients: {ingredients.length()}")

# Display the instructions
print("\nInstructions:")
for step, instruction in instructions.items():
    print(f"  {step}: {instruction}")
