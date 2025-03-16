import random

def mad_libs():
    parts_of_speech = {
        "adjective": [],
        "noun": [],
        "verb": [],
        "adverb": [],
        "plural_noun": []
    }

    # Geting user inputs for each part of speech
    for pos, words in parts_of_speech.items():
      while True:
        num_words = input(f"How many {pos}s do you want to enter? (Enter a number): ")
        try:
          num_words = int(num_words)
          if num_words > 0:
              break
          else:
            print("Please enter a positive number")
        except ValueError:
          print("Invalid input. Please enter a number.")
          
      for _ in range(num_words):
          word = input(f"Enter a {pos}: ")
          parts_of_speech[pos].append(word)


    story = f"""
    The {random.choice(parts_of_speech['adjective'])} {random.choice(parts_of_speech['noun'])} {random.choice(parts_of_speech['verb'])} {random.choice(parts_of_speech['adverb'])} 
    over the lazy {random.choice(parts_of_speech['plural_noun'])}. 
    """

    print("\nHere's your Mad Libs story:")
    print(story)

if __name__ == "__main__":
  mad_libs()
