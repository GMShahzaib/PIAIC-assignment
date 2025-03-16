import random

def guess_the_number():

  lower_bound = 1
  upper_bound = 100  # we can adjust the range
  secret_number = int(input("Enter the secret number between 1 and 100: "))

  if not (lower_bound <= secret_number <= upper_bound):
      print("Secret number must be within the specified range.")
      return

  print(f"I'm guessing your number between {lower_bound} and {upper_bound}")

  guesses_taken = 0
  while True:
    guesses_taken += 1
    guess = random.randint(lower_bound, upper_bound)

    print(f"My guess is: {guess}")

    if guess == secret_number:
      print(f"Hooray! I guessed it in {guesses_taken} tries!")
      break
    elif guess < secret_number:
      print("Too low!")
      lower_bound = guess + 1
    else:
      print("Too high!")
      upper_bound = guess - 1

if __name__ == "__main__":
  guess_the_number()
