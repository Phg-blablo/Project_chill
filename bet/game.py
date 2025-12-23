from random import randint
class Game:
    def __init__(self, players):
        self.players = []
    #hàm tung xúc sắc ngẫu nhiên
    def randomdice(self, player):
        player.dice1 = randint(1,6)
        player.dice2 = randint(1,6)
        player.dice3 = randint(1,6)
        player.total = player.dice1+player.dice2+player.dice3
        player.threekind = (player.dice1 == player.dice2 == player.dice3)
        return player.total, player.threekind
    #hàm nhập số tiền
    def bet_money(self, player):
        while True:
            try:
                player.bet = float(input('enter your bet: '))
                if player.bet > player.account:
                    print('Your balance is not enough')
                elif player.bet <= 0:
                    print('Invalid bet amout. Try again')
                else:
                    print('You have bet: ', player.bet)
                    break
            except ValueError:
                print('Invalid input, try again')
        return player.bet
    #hàm chọn kết quả và đặt cược
    def bet_number(self, player):
        while True:
            try:  
                player.choice = input('enter your choice:(over,under,threekind): ').strip().lower()
                if player.choice in ['over','under','threekind']:
                    print('your choice is: ',player.choice,'with: ', player.bet)
                    return player.choice
                else:
                    print('Invalid choice')
            except ValueError:
                print('Invalid input! Try again')
    #hàm thông báo kết quả
    def win_rate(self, player):
        if player.choice == 'over' and player.total >10 and not player.threekind:
            print('You win:', player.bet*1.5)
            return player.bet*1.5
        elif player.choice == 'under' and player.total <= 10 and not player.threekind:
            print('You win:', player.bet*1.5)
            return player.bet*1.5
        elif player.choice == 'threekind' and player.threekind:
            print('Three kind, you win Jackpot!!', player.bet*10)
            return player.bet*10
        else:
            print('You lose all your bet, try again')
            return -player.bet
    #hàm lưu kết quả
    def play(self, player):
        self.bet_money(player)
        self.bet_number(player)
        self.randomdice(player)
        result = self.win_rate(player)
        player.account += result
        print('Your balance is:', player.account)
        return player.accountno