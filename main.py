
from art import logo, vs
from game_data import data
import random 

def format_data(account):
  """Format the account data into printable format"""
  account_name = account["name"]
  account_descr= account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"
    
#Display art.
print(logo)
# Generate a random account from game.
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
  account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}.")
print(vs)
print(f"Compare become: {format_data(account_b)}.")

#Format the account data into printable format.





#Ask yser for a guess.

#Check if user is correct.


#Get follower count of each account.

#Use if statement to check if user is correct


#Give user feedback on their guess.


#Score keeping


#Make the game repeatable


#Making the account at position B become the next account at position A

#Clear the screen 

