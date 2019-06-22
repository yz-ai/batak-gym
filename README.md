<h1 align="center">Welcome to batak-gym 👋</h1>
<p align="center">
  <img src="https://img.shields.io/badge/version-0.0.1-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/kefranabg/readme-md-generator/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" target="_blank" />
  </a>
</p>

> This game is a challenging environment for AI projects. One version of the game is the same with spades. It is similar to spades, hearts, bid whist, contract bridge and tarneeb. We will be implementing versions of this game eventually.

![card examples](./cards.webp)

## Reinforcement Learning

Batak is a POMDP problem. Its observability is limited to one's hand and the actively picked cards at turns.

## Milestones

We are planning to release this environment step by step.

1. [ ] No bidding, spades is the default trump.
2. [ ] With bidding, spades is the default trump.
3. [ ] With bidding, highest bidder sets the trump.

## ⚡ Environments

> There are three different environments in this gym. Each environment only changes the way the game is played.

<figure>
  <img src="./default-deck.webp" alt="Default Deck with 52 cards">
 <!-- <figcaption>Fig.2 - Default Deck with 52 cards</figcaption> -->
</figure>

### 1. Simple Game Environment

- The card game is played with 4 people. The default deck contains 52 cards. These 52 cards are distributed equally to 4 people. So at the beginning of the game each player has 13 cards.
- The game includes four different types of cards: clubs, diamonds, spades and hearts.
- There is no bidding session before a game start.
- The default trump is always **_spade_**.
- The players only play one card in their turns.
- During a lap, the players can play any card of the same type as the card on the ground without having to increase the card.
- The player who plays the highest card wins this lap.
- Can't play spade until trump is broken.
- If a player does not have any card with the same type on the ground, the player should play **_spade_**. This breaks the trump. After that players can play spades as well.
- After all the cards have been played, points are tallied for each player.
- Each player must get a minimum of 1. Otherwise, they sink to 5.

### 2. Batak Game Environment

- The card game is played with 4 people. The default deck contains 52 cards. These 52 cards are distributed equally to 4 people. So at the beginning of the game each player has 13 cards.
- The game includes four different types of cards: clubs, diamonds, spades and hearts.
- Must play bigger card if present. (As an example: hearts-7 was thrown on the ground. You also have hearts-5 and hearts-9 and hearts-king. You have to throw at least hearts-9. If the cards in your hand do not pass the cards on the floor, you can play any card)
- This card game has a bidding session before game turns start. The bidding opens with 5. Other players may raise or pass the bid respectively. If no-one bids, the first bidder is considered to have entered the bidding with 4.
- The player who won the bidding determines the trump card and starts the game.
- The player who plays the highest card wins this lap.
- If a player does not have any card with the same type on the ground, the player should play **_selected trump_**. This breaks the trump. After that players can play spades as well.
- Can't play spade until trump is broken.
- Each player must get a minimum of 1. Otherwise, they sink to 5.

<!--

## Rewards

### Rewards without bidding

1. After every character plays a card and hand is decided, a reward is issued as 1 or 0.
2. After all the cards have been played, reward is issued as taken hands times 10.

### Rewards with bidding

### Spades style

1. After every character plays a card and hand is decided, a reward is issued as 1 or 0.
2. If the player failed the bid reward is -10 times bid. If the player won the bid reward is 10 times bid.

### Batak style

1. After every character plays a card and hand is decided, a reward is issued as 1 or 0.
2. Player is the bidder and wons the bid, reward is +1 times bid.
3. Player is the bidder and fails the bid, reward is -1 times bid.
4. Player is not the bidder and takes nothing reward is the -1 times bidder's bid.

--> 

## 🤝 Contributing

Contributions, issues and feature requests are welcome.<br />
Feel free to check [issues page](https://github.com/yz-ai/batak-gym/issues) if you want to contribute.

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START -->
<!-- prettier-ignore -->
<table>
  <tr>
    <td align="center"><img src="https://avatars2.githubusercontent.com/u/9072047?s=460&v=4" width="75px;" alt="Kıvanç Güçkıran"/><br /><sub><b>Kıvanç Güçkıran</b></sub><br /><a href="https://github.com/kivancguckiran" title="Code">💻</a></td>
    <td align="center"><img src="https://avatars1.githubusercontent.com/u/4029302?s=460&v=4" width="75px;" alt="Furkan Arslan"/><br /><sub><b>Furkan Arslan</b></sub><br /><a href="https://github.com/FurkanArslan" title="Code">💻</a></td>
    <td align="center"><img src="https://avatars2.githubusercontent.com/u/29750826?s=460&v=4" width="75px;" alt="Umut Can Altın"/><br /><sub><b>Umut Can Altın</b></sub><br /><a href="https://github.com/umutcanaltin" title="Code">💻</a></td>
    <td align="center"><img src="https://avatars3.githubusercontent.com/u/20097381?s=460&v=4" width="75px;" alt="Sinan Çalışır"/><br /><sub><b>Sinan Çalışır</b></sub><br /><a href="https://github.com/snnclsr" title="Code">💻</a></td>
  </tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:END -->
