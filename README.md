# Batak-Gym

This game is a challenging environment for AI projects. One version of the game is the same with spades. It is similar to spades, hearts, bid whist, contract bridge and tarneeb. We will be implementing versions of this game eventually.

## Reinforcement Learning

Batak is a POMDP problem. Its observability is limited to one's hand and the actively picked cards at turns.

## Milestones

We are planning to release this environment step by step.

1. No bidding, spades is the default trump.
2. With bidding, spades is the default trump.
3. With bidding, highest bidder sets the trump.

## Default Rules

1. Can't play another suit, if one has the current trick's suit.
2. Can't lead trump until trump is broken.
3. After all the cards have been played, points are tallied for each player.

## Activatable Rules

1. Must play bigger card if present.
2. The default deck contains 52 cards. The number of cards can be changed to play easier setups.
3. Bidding opens with 5. If no-one bids, first bidder bids with 4.

## Rewards without bidding

1. After every character plays a card and hand is decided, a reward is issued as 1 or 0.
2. After all the cards have been played, reward is issued as taken hands times 10. (no bidding)

## Rewards with bidding

### Spades style

1. After every character plays a card and hand is decided, a reward is issued as 1 or 0.
2. If the player failed the bid reward is -10 times bid. If the player won the bid reward is 10 times bid.

### Batak style

1. Player is the bidder and wons the bid, reward is +1 times bid.
2. Player is the bidder and fails the bid, reward is -1 times bid.
3. Player is not the bidder and takes nothing reward is the -1 times bidder's bid.
