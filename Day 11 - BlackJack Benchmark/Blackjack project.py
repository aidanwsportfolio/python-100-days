import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)

def calculate_score(cards):
    score = sum(cards)

    if score == 21 and len(cards) == 2:
        return 0

    while 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def compare(user_score, cpu_score):
    if cpu_score == 0 and user_score == 0:
        print("You lose.")  # both blackjack
    elif cpu_score == 0:
        print("You Lose!")  # computer blackjack
    elif user_score == 0:
        print("You Win!")   # user blackjack
    elif user_score > 21:
        print("You Lose!")  # user bust
    elif cpu_score > 21:
        print("You Win!")   # computer bust
    elif user_score > cpu_score:
        print("You Win!")   # normal win
    elif cpu_score > user_score:
        print("You Lose!")  # normal loss
    else:
        print("Draw.")      # normal draw

def play_game():
    user_cards = []
    cpu_cards = []
    play_blackjack = input("Do you want to play a game of blackjack?: 'y' or n' ")
    if play_blackjack == 'y':
        print(art.logo)
        user_cards.append(deal_card())
        user_cards.append(deal_card())
        cpu_cards.append(deal_card())
        cpu_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        cpu_score = calculate_score(cpu_cards)

        # End immediately if blackjack detected
        if user_score == 0 or cpu_score == 0:
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print(f"Computer's final hand: {cpu_cards}, final score: {cpu_score}")
            compare(user_score, cpu_score)
            return

        print(f"Your Cards: {user_cards}, Current Score: {calculate_score(user_cards)}")
        print(f"Computer's First Card: {cpu_cards[0]}")
        continue_playing = input("Type 'y' to get another card, type 'n' to pass: ")

        if continue_playing == 'n':
            print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
            if calculate_score(user_cards) < 17 and calculate_score(cpu_cards) != 0:
                cpu_cards.append(deal_card())
            print(f"Computer's final hand: {cpu_cards}, final score: {calculate_score(cpu_cards)}")

            user_score = calculate_score(user_cards)
            cpu_score = calculate_score(cpu_cards)
            if user_score == 0 or cpu_score == 0 or user_score > 21:
                compare(user_score, cpu_score)
                return
            compare(user_score, cpu_score)
            return
        while continue_playing == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            if user_score == 0 or user_score > 21:
                print(f"Your final hand: {user_cards}, final score: {user_score}")
                print(f"Computer's final hand: {cpu_cards}, final score: {cpu_score}")
                compare(user_score, cpu_score)
                return

        user_score = calculate_score(user_cards)
        cpu_score = calculate_score(cpu_cards)
        while cpu_score < 17 and cpu_score != 0:
            cpu_cards.append(deal_card())
            cpu_score = calculate_score(cpu_cards)
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {cpu_cards}, final score: {cpu_score}")
        compare(user_score, cpu_score)

play_game()

while input("Do you want to play a game of blackjack?: 'y' or 'n' ") == 'y':
    print("\n" * 20)  # clears the screen
    play_game()

