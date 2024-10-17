import random
import art

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)  # Ensure we return a single card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)  # Convert an Ace from 11 to 1

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "It's a Draw! 😉"
    elif c_score == 0:
        return "You Lose! 🫠, Opponent has a BlackJack 😊"
    elif u_score == 0:
        return "You Win! 💯, You got the BlackJack 😊"
    elif u_score > 21:
        return "You Lose!🫠, Score went over 21"
    elif c_score > 21:
        return "You Won!💯, Opponent score went over 21"
    elif u_score > c_score:
        return "You Won!💯, Score greater than opponent"
    else:
        return "You Lose!🫠, score less than opponent"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    # Deal two cards to user and computer
    for _ in range(2):
        user_cards.append(deal_card())  # Append a single card value
        computer_cards.append(deal_card())  # Append a single card value

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
               is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Opponent final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' to play 'n' to no: ").lower() == "y":
    print("\n" * 20)
    play_game()




