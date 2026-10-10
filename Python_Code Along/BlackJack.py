import  random

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self) -> str:
        return f"{self.rank['rank']} of {self.suit}"
class Deck:
    def __init__(self):
        self.cards = []
        suits =["spades","clubs","hearts","diamonds"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10}
        ]
        for suit in suits:
            for rank in ranks:
                # print(suit+" "+rank)
                self.cards.append(Card(suit,rank))
    def shuffle(self):
        if len(self.cards)>1:
            return random.shuffle(self.cards)
    def deal(self,number):
        cards_dealt=[]
        for i in range(number):
            if len(self.cards)>0:
                card=self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt
class Hand:
    def __init__(self,dealer=False):
        self.cards=[]
        self.value=0
        self.dealer=dealer
    def add_card(self,card_list):
        self.cards.extend(card_list)

    def calculate_value(self):
        self.value=0
        has_Ace=False
        for card in self.cards:
            card_value=int(card.rank["value"])
            self.value+=card_value
            if card.rank["rank"]=="A":
                has_Ace=True
        if has_Ace and self.value>21:
            self.value-=10
    def get_value(self):
        self.calculate_value()
        return self.value
    def is_blackjack(self):
        return self.get_value()==21
    def display(self,show_all_dealer_cards=False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
        for index,card in enumerate(self.cards):
            if index==0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack():
                print("hidden")
            else:
                print(card)
        if not self.dealer:
            print("Value:",self.get_value())
        print()

class Game:
    def play(self):
        game_number=0
        games_to_play=0
        while games_to_play<=0:
            try:
                games_to_play=int(input("How many games do u want to play? "))
            except:
                print("You must enter a number.")

        while game_number < games_to_play:
            game_number+=1

            deck=Deck()
            deck.shuffle()

            player_hand=Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print()
            print("*" * 30)
            print (f"{game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand,dealer_hand):
                continue
            choice=""
            while player_hand.get_value()<21 and choice not in ["s","stand"]:
                choice= input("Please chose 'Hit' or 'Stand': ").lower()
                print()
                while choice not in ["h","s","hit","stand"]:
                    choice=hoice= input("Please chose 'Hit' or 'Stand' (or H/S) : ")
                    print()
                if choice in ['hit','h']:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()
            if self.check_winner(player_hand,dealer_hand):
                continue
            player_hand_value=player_hand.get_value()
            dealer_hand_value=dealer_hand.get_value()

            while dealer_hand_value <17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value=dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue
            print("Final Results")
            print("Your hand:",player_hand_value)
            print("Dealer hand:",dealer_hand_value)

            self.check_winner(player_hand,dealer_hand,True)

        print("\nThanks for Playing")

    def check_winner(self,player_hand,dealer_hand,game_over=False):
        if not game_over:
            if player_hand.get_value()>21:
                print("You Buster. Dealer Wins")
                return  True
            elif dealer_hand.get_value()>21:
                print("Dealer busted. you Win!")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Both players have a blackjack , Tie")
                return True
            elif player_hand.is_blackjack():
                print("You have blackjack you win")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer has a blackjack. Dealer wins")
                return True
        else :
            if player_hand.get_value()>dealer_hand.get_value():
                print("You Win")
            elif player_hand.get_value()==dealer_hand.get_value():
                print("You Tie")
            else:
                print("Dealer Wins")
            return True
        return False

g=Game()
g.play()
# deck=Deck()
# deck.shuffle()
#
# hand=Hand()
# hand.add_card(deck.deal(2))
# hand.display()







# deck1 = Deck()
# print(deck1.cards)
# deck2= Deck()
# deck2.shuffle()
# print(deck2.cards)
# card1 = Card('diamonds', {'rank': '3', 'value': 3})
# print (card1)
    # suite = "Hearts"
    # suite = suits[2]
    # rank = "K"
    # value = 10
    # # print("Your card is:")
    # # print(rank)
    # print ("Your card is:"+rank+" of "+ suite)
    # # suits.append("snakes")
    # ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
   # print (cards)
    # random.shuffle(cards)
    # print(cards)
    # card = cards.pop()
    # print(card)
    # shuffle()
    # # cards_dealt=deal(2)
    # # card=cards_dealt[0]
    # # rank = card[1]
    # # if rank=="A":
    # #     value =11
    # # elif rank=="K" or rank=="J" or rank=="Q":
    # #     value =10
    # # else:
    # #     value = int(rank)
    # # rank_dict={"rank":rank,"value":value}
    # # # print(rank, value)
    # # print(rank_dict["rank"],rank_dict["value"])
    # card=deal(1)[0]
    # print(card[1]["value"])



















