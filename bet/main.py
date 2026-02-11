from player import Player
from game import Game
from ranking import Rank
#hàm khởi động trò chơi, hỏi số lượng người, hỏi tuổi
def create_players ():
    num_players = int(input('Nhập số lượng người chơi: '))
    players = []
    for i in range (num_players):
        name = input(f'Nhập tên người chơi: {i+1}: ')
        while True:
            try:
                age = int(input('Nhập số tuổi của người chơi: '))
                if age <16:
                    print('Người chơi phải trên 16 tuổi!, vui lòng nhập lai')
                    continue
                break
            except ValueError:
                print('Hãy nhập lại đúng định dạng!')
        players.append(Player(name, age))
    return players
def bet_amout (game, player):
    while True:
        try:
            bet = float(input('Nhập số tiền cược: '))
            ok, msg = game.valid_bet(player, bet)
            if ok:
                return bet
            else:
                print(msg)
        except ValueError:
            print('Vui lòng nhập lại: ')
def main():
    players = create_players()
    game = Game(players)
if __name__ == '__main__':
    main()
