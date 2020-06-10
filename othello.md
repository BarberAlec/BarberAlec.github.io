## An Analysis of Othello AI Strategies

This project was completed for the CS7_IS2 Artificial Intelligence module as a team of 4. We were awarded an end of year grade of 90% in recognition of the work.

**Project description:** Othello is an interesting game in the domain of artificial intelligence due to a somewhat unexpected level of complexity. Simplified versions of the game on a 6x6 and 4x4 versions of the board have been solved, but no full solution has been found for the classic 8x8 board and above. This letter surveys a number of state-of-the-art approaches to Othello game playing including CNNs and adversarial models. Performance is measured against computational efficacy, model memory size and Monte Carlo simulation against a benchmark greedy algorithm. A further investigation into  heuristics is also presented. Results indicate that the adversarial models outperform the CNN but is highly dependant on the heuristics adopted. A further analysis on Bayesian and reinforcements methods is provided. [Click here for Othello PDF](pdf/An_Analysis_of_Othello_AI_Strategies.pdf).

### The game

Othello is a two-player, deterministic, zero-sum (i.e. the total reward is fixed and the player’s scoreis negatively related) board game which has perfect information. The game is played on an 8x8 board using 64 dual colored discs. Each disc is colored black on one side and white on the other. Initially, the entire board is empty except the central 4 squares. In the main diagonal, white discs are kept on d4 and e5, and on the other diagonal black discs are kept i.e. on e4 and d5. This initial board configuration is shown in Figure 1a below.

[](images/oth_example_board_pos.png)

The game begins with player black (henceforth referred to as just black or white) making the firstmove. A legal move is made by placing a disc on an empty square so that in at least one directionfrom the square played on, there is a sequence of one or more of the opponents discs followed bythe player’s own disc. The opponent’s discs, in such a sequence, are then flipped and become thecurrent player’s color. For example, if the player moves e6(as highlighted in Figure 1a), the whitedisc on e5 will be turned over to black (as highlighted in Figure 1b). If a player cannot make a legal move, they must forfeit their turn. The game ends when neitherplayer can make a legal move, i.e. either when all 60 squares are filled or, if squares are left, whenneither player can legally place their disc in one. The player with most discs on the board wins, or ifthe number of the discs are equal, then the game is deemed as a draw. The proceeding sections willoutline adversarial methods and CNN approaches to Othello game playing.


### Methods assessed
#### Adversarial 
- Mini - Max
- Alpha - Beta Pruning
- NegaScout

#### CNN
- Adopted a image format for all game-states.
- Trained in the fast-ai enviroment.
- Generalised poorly


For code and more details see the repo [here](https://github.com/BarberAlec/Othello-Game-Playing-AI-Evaluation).
