print("Calculate your average Wordle score!\n")

print("Input your Guess Distribution")

guesses = [
  int(input("1: ")),
  int(input("2: ")),
  int(input("3: ")),
  int(input("4: ")),
  int(input("5: ")),
  int(input("6: "))
]

total_guesses = sum(guesses)
total_score = sum(map(lambda x: x[0] * x[1], list(enumerate(guesses, start=1))))

print("\nYour average score is: ", float(total_score / total_guesses))
