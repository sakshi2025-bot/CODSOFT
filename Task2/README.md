# Task 2: Tic-Tac-Toe AI

This project is an AI agent that plays the classic game of Tic-Tac-Toe against a human player. The AI is designed to be unbeatable by using the **Minimax algorithm**, a core concept in game theory and artificial intelligence.

The program is a command-line application built in Python.

### Features
* **Unbeatable AI:** The AI player uses the Minimax algorithm to find the optimal move, ensuring it will either win the game or force a draw.
* **Human vs. AI Gameplay:** The game allows a human player to compete directly against the AI.
* **Command-Line Interface:** The game runs entirely in the terminal, providing a straightforward and functional user experience.

### How it Works
The AI's intelligence is powered by the **Minimax algorithm**. This is a recursive search algorithm that evaluates all possible moves from the current game state to a terminal state (win, loss, or draw). It assigns a score to each final outcome and then chooses the move that leads to the best possible score for the AI, while assuming the human player will also play optimally to minimize the AI's score.

### How to Run
1.  Make sure you have Python installed.
2.  Save the code as `tictactoe_ai.py`.
3.  Open your terminal or command prompt.
4.  Navigate to the directory where you saved the file.
5.  Run the game using the command: `python tictactoe_ai.py`

### Learning Takeaways
This project was a valuable exercise in:
* Understanding and implementing search algorithms.
* Applying game theory principles to a practical problem.
* Working with recursion and basic AI logic.
