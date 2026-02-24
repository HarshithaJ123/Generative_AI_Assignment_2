#number guessing game program
import random
best_score = None
while True:
  print("\n--- Number Guessing Game ---")
  number = random.randint(1, 100)
  attempts = 7
  used = 0

  while attempts > 0:
    guess = int(input("Enter your guess (1-100): "))
    used += 1
    attempts -= 1

    if guess == number:
      print("Correct! You guessed the number.")
      print("Attempts used:", used)

      if best_score is None or used < best_score:
        best_score = used
        print("New Best Score:", best_score)

      break
    
    elif guess > number:
      print("Too high!")
    else:
      print("Too low!")

      # hint if close (bonus)
      if abs(guess - number) <= 5:
        print("Hint: You are very close!")
        print("Attempts remaining:", attempts)
  else:
    print("You lost! The number was:", number)
    choice = input("\nDo you want to play again? (yes/no): ")
    if choice.lower() != "yes":
      print("Thanks for playing!")
      break