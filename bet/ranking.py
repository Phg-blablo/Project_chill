class Rank:
    def __init__(self, players):
        self.players = players
    def ranking(self):
        ranking = sorted(self.players, key = lambda p: p.account, reverse=True)
        print('\n Final Ranking')
        for i, player in enumerate(ranking, start=1):
            print(f'{i}. {player.name} - {player.account:.2f}')