def rock_paper_scissors(player1: str, player2: str):
    outcomes = ["Player 1 wins!", "Player 2 wins!", "It's a tie!"]
    beats = {
        "rock" : "scissors", 
        "paper" : "rock", 
        "scissors" : "paper"
    }

    player1 = player1.lower()
    player2 = player2.lower()

    if player1 == player2:
        return outcomes[2]
    
    if beats[player1] == player2:
        return outcomes[0]
    
    return outcomes[1]
    
print(rock_paper_scissors("rock", "scissors"))
print(rock_paper_scissors("paper", "scissors"))
print(rock_paper_scissors("paper", "rock"))
print(rock_paper_scissors("rock", "paper"))
print(rock_paper_scissors("scissors", "paper"))
print(rock_paper_scissors("scissors", "rock"))
print(rock_paper_scissors("rock", "rock"))



