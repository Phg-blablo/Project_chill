from player import Player
from game import Game
from ranking import Rank
def main():
    numplayers = int(input('How many people you guys want to play: '))
    players = []
    for i in range (numplayers):
        name = input(f'Enter name of players {i+1}: ')
        while True:
            try:
                age = int(input(f'Enter age of player {i+1}: '))
                if age <18:
                    print('Sorry, customers must be older than 18')
                    return 
                else:
                    print('Vertify......')
                    break
            except ValueError:
                print('Invalid input, try again!!')
                return
        players.append(Player(name, age))
    if not players:
        print('Sorry, we are out of business right now, please come back later!!!')
        return
    g = Game(players)
    while True:
        for player in players:
            if player.account > 0:
                print('Turn of ', player.name)
                g.play(player)
            else:
                print(player.name, 'you are bankrupt, please come back next time')
        again = input('Do you guys want to continue(yes/no): ').strip().lower()
        if again != 'yes':
            print('Thank you for choosing us, see you next time!!!!')
            break
    r = Rank(players)
    r.ranking()
if __name__ == '__main__':
    main()
