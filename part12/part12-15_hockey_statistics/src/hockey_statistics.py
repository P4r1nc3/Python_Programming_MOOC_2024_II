import json

class Player:
    def __init__(self, name:str, nationality:str, assists:int, goals:int, penalties:int, team:str, games:str):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    
    def __str__(self):
        return f'{self.name:21}{self.team:3}{self.goals:4} + {self.assists:2} = {(self.goals+self.assists):3}'

class HockeyApplication:    
    def __init__(self):
        self.players = []
    
    def help(self):
        print('commands:')
        print('0 quit')
        print('1 search for player')
        print('2 teams')
        print('3 countries')
        print('4 players in team')
        print('5 players from country')
        print('6 most points')
        print('7 most goals')
    
    def read_file(self, file_name: str):
        with open(file_name) as file:
            data = file.read()
        return json.loads(data)

    def add_players(self, all_players: list):
        for player in all_players:
            p = Player(player['name'], player['nationality'], player['assists'], player['goals'], player['penalties'], player['team'], player['games'])
            self.players.append(p)

    def search_player(self):
        name = input('name: ')
        for player in self.players:
            if player.name == name:
                print(player)
    
    def list_teams(self):
        teams = map(lambda player: player.team, self.players)
        teams = set(list(teams))
        for team in sorted(teams):
            print(team)

    def list_countries(self):
        countries = map(lambda player: player.nationality, self.players)
        countries = set(list(countries))
        for country in sorted(countries):
            print(country)

    def __points_scored(self, player: Player):
        return [(player.goals + player.assists), player.goals]

    def list_players_in_team(self):
        team = input('team: ')
        team_players = filter(lambda player: player.team == team, self.players)
        team_players = sorted(team_players, key=self.__points_scored, reverse=True)
        for player in team_players:
            print(player)

    def list_players_in_country(self):
        country = input('country: ')
        country_players = filter(lambda player: player.nationality == country, self.players)
        country_players = sorted(country_players, key=self.__points_scored, reverse=True)
        for player in country_players:
            print(player)

    def list_players_most_points(self):
        max_num_of_players = int(input('how many: '))
        points_players = sorted(self.players, key=self.__points_scored, reverse=True)
        count = 1
        for player in points_players:
            if count <= max_num_of_players:
                print(player)
                count += 1

    def __goals_scored(self, player: Player):
        return [player.goals, (player.games)*-1]

    def list_players_most_goals(self):
        max_num_of_players = int(input('how many: '))
        points_players = sorted(self.players, key=self.__goals_scored, reverse=True)
        count = 1
        for player in points_players:
            if count <= max_num_of_players:
                print(player)
                count += 1

    def execute(self):
        if True:
            file_name = input('file name: ')
        else:
            file_name = 'partial.json'
        all_players = self.read_file(file_name)
        print(f'read the data of {len(all_players)} players')
        self.add_players(all_players)
        self.help()
        while True:
            print()
            command = input('command: ')
            if command == '0':
                break
            elif command == '1':
                self.search_player()
            if command == '2':
                self.list_teams()
            elif command == '3':
                self.list_countries()
            if command == '4':
                self.list_players_in_team()
            elif command == '5':
                self.list_players_in_country()
            if command == '6':
                self.list_players_most_points()
            elif command == '7':
                self.list_players_most_goals()

app = HockeyApplication()
app.execute()