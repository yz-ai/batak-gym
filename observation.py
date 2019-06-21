
state = {
  'current_player': 0, # 0, 1, 2, 3
  'trump_broken': False,
  'expecting_bid': False,
  'expecting_trump': False,
  'current_trump': 'SPADES',
  'last_play': { 'type': 'DIAMONDS', 'number': 1, 'source_player': 3 },
  'current_set': [
    { 'type': 'CLUBS', 'number': 2, 'source_player': 2 },
    { 'type': 'CLUBS', 'number': 1, 'source_player': 3 },
    # ...
  ],
  'players': [
    {
      'id': 0,
      'hand': [
        { 'type': 'SPADES', 'number': 1 },
        { 'type', 'HEARTS', 'number': 3 },
        # ...
      ],
      'legal_moves': [
        { 'type': 'SPADES', 'number': 1 },
        # ...
      ],
      'current_score': 3,
      'current_bid': 5,
      # ...
    },
    # ...
  ],
}
