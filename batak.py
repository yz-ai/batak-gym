import random
import numpy as np

# 0-12 SPADES (2-3-4-5-6-7-8-9-10-J-Q-K-A)
# 13-25 CLUBS (2-3-4-5-6-7-8-9-10-J-Q-K-A)
# 26-38 HEARTS (2-3-4-5-6-7-8-9-10-J-Q-K-A)
# 39-51 DIAMONDS (2-3-4-5-6-7-8-9-10-J-Q-K-A)
from environments import SimpleEnv

idx2card = {
    0: '2S', 1: '3S', 2: '4S', 3: '5S', 4: '6S', 5: '7S', 6: '8S', 7: '9S', 8: '10S', 9: 'JS', 10: 'QS', 11: 'KS', 12: 'AS',
    13: '2C', 14: '3C', 15: '4C', 16: '5C', 17: '6C', 18: '7C', 19: '8C', 20: '9C', 21: '10C', 22: 'JC', 23: 'QC', 24: 'KC', 25: 'AC',
    26: '2H', 27: '3H', 28: '4H', 29: '5H', 30: '6H', 31: '7H', 32: '8H', 33: '9H', 34: '10H', 35: 'JH', 36: 'QH', 37: 'KH', 38: 'AH',
    39: '2D', 40: '3D', 41: '4D', 42: '5D', 43: '6D', 44: '7D', 45: '8D', 46: '9D', 47: '10D', 48: 'JD', 49: 'QD', 50: 'KD', 51: 'AD'}

card2idx = {card: idx for idx, card in idx2card.items()}
suit_indices = {"S": list(range(0, 13)), "C": list(range(13, 26)), "H": list(range(26, 39)), "D": list(range(39, 52))}


def deal_cards():
    cards = np.arange(0, 52)
    player_hands = []
    # Shuffle card indices to deal cards.
    shuffled_idx = np.random.permutation(52)
    start_idx = 0
    end_idx = 13

    for i in range(4):
        # Give the first 13 card from shuffled deck to player 0, next 13 to player 1 etc.
        current_hand = cards[shuffled_idx[start_idx:end_idx]]
        player_hands.append(np.sort(current_hand))
        start_idx += 13
        end_idx += 13

    return player_hands


def print_current_hands(player_hands):
    for i, hand in enumerate(player_hands):
        print("Current Player: ", i)
        for idx in hand:
            print(idx2card[idx], " ", end="")
        print("\n")


def get_playable_cards(player_hand, current_trump, trump_broken, current_suit, current_set, current_highest):

    playable_cards = []
    trump_cards = [idx for idx in player_hand if idx in suit_indices[current_trump]]

    # If the current_player plays the first card.
    if current_highest is None:
        if not trump_broken:
            # Return all the cards that is not trump suit.
            playable_cards = [card_idx for card_idx in player_hand if card_idx not in suit_indices[current_trump]]

        else:
            # If trump is broken you can play any card you want.
            playable_cards = player_hand
    # If there are already cards in the set.
    else:

        same_suit_cards = [idx for idx in player_hand if idx in suit_indices[current_suit]]

        # If we don't have any cards that is same suit with the playground.
        if not same_suit_cards:
            # If we also don't have any trump card, we can play any card from the hand.
            if not trump_cards:
                playable_cards = player_hand

            # If we have trump in our hand.
            else:

                trumps_in_current_set = [trump_card for trump_card in current_set if trump_card in suit_indices[current_trump]]

                # If there is no trump card in the playground.
                # HERE, WE BROKE THE TRUMP.
                if not trumps_in_current_set:
                    playable_cards = trump_cards
                    print("TRUMP BROKEN")
                    trump_broken = True

                # There is trump in the playground.
                else:
                    # This will hold the highest trump card in the current set, because current set cards (trump cards) will be sorted by ascending order).
                    highest_trump_card = trumps_in_current_set[-1]
                    bigger_trump_cards = [card_idx for card_idx in trump_cards if card_idx > highest_trump_card]

                    # If we have bigger trump cards in our hand.
                    if bigger_trump_cards:
                        playable_cards = bigger_trump_cards
                    # If we don't have any.
                    else:
                        playable_cards = trump_cards
        # If we have cards that are the same suite with the current set.
        else:
            bigger_cards = [card_idx for card_idx in same_suit_cards if card_idx > current_highest]

            if not bigger_cards:
                playable_cards = same_suit_cards
            else:
                playable_cards = bigger_cards

    return playable_cards, trump_broken


def main():
    player_hands = deal_cards()
    # print_current_hands(player_hands)

    # For simplicity, default trump is spades now.
    current_trump = "S"
    trump_broken = False

    # And also for simplicity, the current bid is 4 and player 0 is the default starter.
    current_bid = 4
    current_player = 0
    current_suit = "D"
    current_highest = None
    current_set = []
    print_current_hands(player_hands)

    count = 0
    while count < 5:
        print(f"Player {current_player} is now playing")
        player_hand = player_hands[current_player]
        playable_cards, trump_broken = get_playable_cards(player_hand, current_trump, trump_broken, current_suit, current_set, current_highest)

        print(f"PLAYER {current_player}'S playable cards: ")
        print(playable_cards)
        for idx in playable_cards:
            print(idx2card[idx], " ", end="")

        random_card = random.choice(playable_cards)
        current_suit = idx2card[random_card][-1]
        print("Current suit: ", current_suit)
        print(f"PLAYER {current_player} is playing: {random_card}/{idx2card[random_card]}")

        print("\n")
        current_set.append(random_card)
        # Remove the played card from the current_player's hand. Maybe better way??
        player_hands[current_player] = np.delete(player_hand, np.argwhere(player_hand == random_card))

        current_player += 1
        if current_highest is None:
            current_highest = random_card

        else:
            trump_cards = [card_idx for card_idx in current_set if card_idx in suit_indices[current_trump]]

            same_suit_cards = [card_idx for card_idx in current_set if card_idx in suit_indices[current_suit]]
            if not trump_cards:
                current_highest = same_suit_cards[-1]

            else:
                current_highest = trump_cards[-1]

        if current_player % 4 == 0:
            current_player = 0
            current_set = []
            count += 1


def main_with_env():
    env = SimpleEnv()
    state = env.reset()

    print(state.hand, state.history)


if __name__ == '__main__':
    main_with_env()
