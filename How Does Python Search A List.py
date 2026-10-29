# https://www.youtube.com/watch?v=F_4jhylgZi4
# How Does Python Search A List?
# Create a list
fish = ["bass",
        "trout",
        "perch",
        "walleye",
        "bluegill",
       ]
# Let's see what we have so far:
print(f"fish: {fish}")
print(f"fish is of type {type(fish)}")
# Let's search for "perch".
# This is a basic linear search.
# Use the enumerate function.
for i, my_fish in enumerate(fish):
  if my_fish == "perch":
      print(f"perch found at index {i}")
# What if the target isn't there?
# Let's search for "eel".
# The else looks funny,
#  but it works.
for i, f in enumerate(fish):
  if f == "eel":
      print(f"eel found at index {i}")
else:
  print("eel not found")
# Here's another trick:
# Use the in keyword.
# We don't get the index
#  rather we get True/False
eel_found = "eel" in fish
print(f"found: {eel_found}")
# Yet another trick.
# Use the index() method
i = fish.index("bass")
print(f"bass found at index {i}")
# What if the value isn't there?
# What does index() do?
# It throws an exception
try:
    i = fish.index("eel")
except Exception as ex:
    print(f"exception: {ex}")
