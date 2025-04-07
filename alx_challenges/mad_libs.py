def mad_libs():
    print("welcome to mad libs! lets create a fun story together.")

    noun = input("enter a noun: ").strip()
    verb = input("enter a verb: ").strip()
    adjective = input("enter an adjective: ").strip()
    place = input("enter a place: ").strip()
    animal = input("enter an animal: ").strip()

    story = f"""one day, a {adjective} {noun} decided to go on an adventure.
     it traveled all the way to {place}, where it met a {animal}.
      the {noun} decided to {verb} in front of the {animal}. 
       by the end of the day the {noun} learned that being {adjective} is the best way to make new friends"""
    
    print("\n here is your mad lib story: \n")
    print(story)

mad_libs()