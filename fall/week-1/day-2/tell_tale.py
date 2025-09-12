print("🎉 Welcome to the Story Maker! 🎉")
print("Answer the following questions to create your custom story.\n")

name = input("Enter a name: ")
place = input("Enter a place: ")
object_ = input("Enter an object: ")
animal = input("Enter an animal: ")
feeling = input("Enter a feeling: ")
activity = input("Enter an activity: ")

# Change the story template below to create your own unique story
story = f"""
One day, {name} went to {place} with a {object_} in their backpack.
On the way, they met a {animal} that looked very {feeling}.
Instead of being scared, {name} decided to {activity} with the {animal}.
It turned out to be the start of an unforgettable adventure!
"""

print("\nHere’s your story! ")
print(story)
