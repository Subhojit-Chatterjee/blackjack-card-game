import random
import logo


def deal_card():
    # Returns a random card from the deck of cards
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(card_set):
    if len(card_set) == 2 and sum(card_set) == 21:
        return 0
    if sum(card_set) > 21 and 11 in card_set:
        card_set.remove(11)
        card_set.append(1)
    return sum(card_set)


def compare(user_score, computer_score):
    if user_score == computer_score:
        print("\nBoth user and computer have same score. It's a draw.😑")
    elif computer_score == 0:
        print("\nComputer wins by a Blackjack.")
    elif user_score == 0:
        print("\nCongrats! You win by a Blackjack.")
    elif user_score > 21:
        print("\nYour score went over 21, you lose!")
    elif computer_score > 21:
        print("\nComputer's score went over 21.You win!")
    elif user_score > computer_score:
        print("\nYou have a higher score. You win!")
    else:
        print("\nYou lose!")


def play_blackjack():
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0
    game_over = False

    print(logo.logo)
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            print(f"Your current hand is {user_cards} and your current score is {user_score}."
                  f"\nComputer's first card is {computer_cards[0]}")
            user_choice = input("Do you want to pick another card? (y/n): ")

            if user_choice == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
    print(f"\nYour final hand is {user_cards}. Your final score is {user_score}. Computer's hand is {computer_cards}."
          f" Computer's final score is {computer_score}.")
    compare(user_score, computer_score)


while input("Do you wish to play a game of blackjack? (y/n): ") == 'y':
    play_blackjack()
