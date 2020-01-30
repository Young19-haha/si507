import random, math

max_input_s = input("Enter an interger greater than zero: ")
num = int(max_input_s)
secret = random.randint(0, num)
count = int(math.log(num, 2) + 1)

while True:
  response_s = input("Enter a guess, or 'quit': ")
  if response_s == 'quit':
    break
  else:
    response = int(response_s)
    if response == secret:
      print("You got it!")
      break
    elif response > 1000 or response < 0:
      print("Invalid input. Entera number between 0 and 1000")
    else:
      # print("Invalid input. Entera number between 0 and 1000")
      if response > secret:
        print("Too high! Try again.")
      elif response < secret:
        print("Too low! Try again.")
      else:
        print("Invalid input. Entera number between 0 and 1000")
      count = count - 1
      if count == 1:
        print(f"You have {count} guess remained.")
      elif count == 0:
        print(f"You have run out of gusses.\nByebye!")
        break
      else:
        print(f"You have {count} guesses remained.")
  # else:
  #   print("Nope, you're wrong.")

  


