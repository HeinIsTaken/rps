import random

def rps():
  player_choice = input({"Rock,Paper,Scissors"})
  choices = ["rock","paper","scissors"]
  computer_choice = random.choice(choices)
  result = {"Player":player_choice,"Computer":computer_choice}
  return result


def winner(player, computer):
  print(f"You chosed {player},The Computer chosed {computer}")
  if player == computer:
    return "It's a tie!" 
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors,You win!"
    else:
      return "Paper covers rock,you lose."
      
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock, you win!"
    else:
      return "Scissors cuts paper,you lose."

  elif player == "scissors":
    if computer == "paper":
      return "Scissors cuts paper,you win!"
    else:
      return "Rock smashes scissors,you lose."

  return 
result = rps()
conclusion = winner(result["Player"],result["Computer"])
print(conclusion)

