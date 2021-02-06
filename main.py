
from art import logo, vs
from game_data import data
import random 
from replit import clear

def format_data(account):
  """Format the account data into printable format"""
  account_name = account["name"]
  account_descr= account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follower counts and returns if they got it right. """
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


#Display art.
print(logo)
#Getting the score
score = 0
game_should_continue = True 
account_b = random.choice(data)

#Make the game repeatable
while game_should_continue:
   
  # Generate a random account from game.
  account_a = account_b
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Compare become: {format_data(account_b)}.")

  #Format the account data into printable format.


  #Ask user for a guess.
  guess = input("Who has more followers? Type 'A' or 'B'.").lower()


  #Check if user is correct.
  #Get follower count of each account.
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"] 
  #Use if statement to check if user is correct
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  #Clear the screen 
  clear()
  print(logo)

  #Give user feedback on their guess.
  if is_correct:
    #Score keeping
    score += 1
    print(f"You are right! Current score: {score}")
  else:
    print(f"Sorry, that's wrong. The final score is {score}")

#Making the account at position B become the next account at position A



