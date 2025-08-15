import random

subjects =[
    "srk",
   "virat kohli"
   "modi"
  "dhoni",
  "ramesh"
  "bravo"
]
   




actions = [
    "attack",
    "runs away",
    "dances ",
    "celebrates"
    "dwells"
    "sings"
]

places_or_things = [
    "at delhi",
    "at kolkata",
    "at mumbai",
    "at swizerland"
    "at bangkok"
    "at lomdom"
]

while True:
    subject = random.choice(subjects) 
    action  = random.choice(actions)
    place_or_thing =random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing} "
    print("\n"+ headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip()
    if user_input == "no":
      break

print("\nthanks for using the fake news headline generator. have a fun day ")