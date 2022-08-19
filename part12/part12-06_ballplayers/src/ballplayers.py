class BallPlayer:
    def __init__(self, nimi: str, number: int, goals: int, passes: int, minutes: int):
        self.nimi = nimi
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(nimi={self.nimi}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')

def most_goals(players: list):
    player = max(players, key=lambda item: item.goals)
    return player.nimi

def most_points(players: list):
    player = max(players, key= lambda item: item.goals + item.passes)
    return (player.nimi, player.number)

def least_minutes(players: list):
    return min(players, key= lambda item: item.minutes)

if __name__ == "__main__":
    player1 = BallPlayer("Archie Bonkers", 13, 5, 12, 46)
    player2 = BallPlayer("Speedy Tickets", 7, 2, 26, 55)
    player3 = BallPlayer("Cruella De Hill", 9, 1, 32, 26)
    player4 = BallPlayer("Devilled Tasmanian", 12, 1, 11, 41)
    player5 = BallPlayer("Donald Quack", 4, 3, 9, 12)
    
    team = [player1, player2, player3, player4, player5]
    print(most_goals(team))
    print(most_points(team))
    print(least_minutes(team))