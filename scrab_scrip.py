letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points = {letter:point for letter, point in zip(letters, points)}
letter_to_points[' '] = 0
players = []
player_to_points = {}
player_to_words = {}

def add_player(player):
    players.append(player)
    player_to_points[player] = []
    player_to_words[player] = []

def score_word(word):
    point_total = 0
    for x in word:
        x = x.upper()
        a = letter_to_points.get(x, 0)
        point_total += a
    return point_total

def play_history(player):
    for x in range(len(player_to_words[player])):
        print(player_to_words[player][x] + ':' + str(score_word(player_to_words[player][x])))
    return '\n'

def play_word(player, word):
    player_to_words[player].append(word)
    return player_to_words

def player_score(player):
    player_points = 0
    for player, words in player_to_words.items():
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points
        return player_to_points[player]


