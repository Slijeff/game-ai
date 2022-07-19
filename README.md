# game-ai
An implementation of Minimax with alpha-beta pruning algorithm on the game of Gomoku (five-in-a-row). It contains a frontend with React and a flask backend that connects to the AI agent class. A demo was deployed at http://gomoku.slijeff.com (it uses the flask development server so please use it only as a demo).

![Screenshot of UI](screenshot1.png?raw=true)

## Deploy Instruction
To deploy it on your server on port 80 with docker-compose:
1. `git clone` this repo and `cd` into it.
2. Run `sudo docker-compose build`
3. Run `sudo docker-compose up`

## Goals
- [X] Implement Minimax agent
- [ ] Implement MCTS agent
- [X] Implement Gomoku class
- [X] Implement Tic-tac-toe class
- [X] Implement front-end
- [X] Implement flask backend
