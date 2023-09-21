class Game:
    def __init__(self, title):
        self.title = title
    
    def get_title(self):
        return self._title
    
    def set_title(self, value):
        if type(value) is str and 0 < len(value) and not hasattr(self, 'title'):
            self._title = value
        else: 
            print('Invalid title')

    title = property(get_title, set_title)

    def results(self):
        return [result for result in Result.all if result.game is self]

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        count = 0
        total_score = 0
        for result in self.results():
            if result.player is player:
                count += 1
                total_score += result.score
        if count == 0:
            return 0
        return total_score/count

class Player:

    def __init__(self, username):
        self.username = username

    def get_username(self):
        return self._username
    
    def set_username(self, value):
        if type(value) is str and 2<=len(value)<=16:
            self._username = value
        else:
            print("Invalid username")

    username = property(get_username, set_username)

    def results(self):
       return [result for result in Result.all if result.player is self]

    def games_played(self):
       return list({result.game for result in self.results()})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        games_played = [result.game for result in self.results()]
        return games_played.count(game)

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    def get_score(self):
        return self._score
    def set_score(self, value):
        if type(value) is int and 1<=(value)<=5000 and not hasattr(self, 'score'):
            self._score = value
        else: 
            print("Invalid score")
    
    score = property(get_score, set_score)

    def get_player(self):
        return self._player

    def set_player(self, value):
        if type(value) is Player:
            self._player = value
        else: 
            print("Invalid player")

    player = property(get_player, set_player)

    def get_game(self):
        return self._game
    
    def set_game(self, value):
        if type(value) is Game:
            self._player = value
        else: 
            print("Invalid player")
    
new_game = Game("New Game")
snake = Game("Snake")
cs = Game("Counter Strike")
kam = Player("Kam")
terance = Player("Terance")
ryan = Player("ryan")
Result(kam, new_game, 3000)
Result(terance, new_game, 2000)
Result(ryan, cs, 200)
Result(kam, snake, 3600)
# print(ryan.results())