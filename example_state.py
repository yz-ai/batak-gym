#
# STATE #1
# 
# Expecting bid and trump

state_1 = {
    'id': 0,
    'type': 'BIDDING',
    'current_player': 2,
    'expecting_action': 'BID_AND_TRUMP',
    'current_game_count': 4,
    'total_game_count': 10,
    'hand': [
        {'type': 'SPADES', 'number': 2},
        {'type': 'HEARTS', 'number': 12},
        # ...
    ],
    'players': [
        {
            'id': 0,
            'bid': 5,
        },
        {
            'id': 1,
            'bid': 6,
        },
    ],
}

#
# STATE #2
#
# Bid winner

state_2 = {
    'id': 0,
    'type': 'BID_WINNER',
    'player': 1,
    'bid': 6,
    'trump': 'HEARTS',
    'current_game_count': 4,
    'total_game_count': 10,
}

#
# STATE #3
#
# Hand

state_3 = {
    'id': 0,
    'type': 'HAND',
    'current_player': 0,
    'player_offset': 0,
    'trump_broken': False,
    'trump': 'SPADES',
    'hand_taken': 3,
    'bid': 5,
    'game_score': 30,
    'turn_count': 2,
    'current_game_count': 4,
    'total_game_count': 10,
    'current_bid_holder': {
        'source_player': 0,
        'bid': 6,
    },
    'last_play': {'type': 'DIAMONDS', 'number': 1, 'source_player': 3},
    'current_set': [
        {'type': 'CLUBS', 'number': 2, 'source_player': 2, 'winner': False},
        {'type': 'CLUBS', 'number': 5, 'source_player': 3, 'winner': False},
        {'type': 'CLUBS', 'number': 8, 'source_player': 0, 'winner': False},
        # ...
    ],
    'hand': [
        {'type': 'SPADES', 'number': 1},
        {'type': 'HEARTS', 'number': 3},
        # ...
    ],
    'legal_moves': [
        {'type': 'SPADES', 'number': 1},
        # ...
    ],
    'players': [
        {
            'id': 1,
            'hand_taken': 3,
        },
        {
            'id': 2,
            'hand_taken': 2,
        },
    ],
}

#
# State #4
#
# Hand Decision

state_4 = {
    'type': 'HAND_DECISION',
    'set': [
        {'type': 'CLUBS', 'number': 2, 'source_player': 2, 'winner': False},
        {'type': 'CLUBS', 'number': 5, 'source_player': 3, 'winner': False},
        {'type': 'CLUBS', 'number': 8, 'source_player': 0, 'winner': False},
        {'type': 'CLUBS', 'number': 12, 'source_player': 1, 'winner': True},
    ],
}

#
# State #5
#
# Game Decision

state_5 = {
    'type': 'GAME_DECISION',
    'players': [
        {
            'id': 0,
            'bid': 5,
            'taken': 3,
            'score': -20,
        },
        # ...
    ],
}
