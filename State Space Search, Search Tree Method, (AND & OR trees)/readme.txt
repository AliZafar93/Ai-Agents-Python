Logic Simulation and Games in Python
Overview
This project includes three mini Python applications designed to simulate basic logic gates and simple AI-based puzzles:

AND/OR Gate Simulation

8-Puzzle Game

City Path Finder Game

Each task helps to build understanding of conditional logic, simple search methods, and user interaction through command-line interfaces.

1. AND/OR Gate Simulation
This simulation models two real-world examples of basic logic gates:

Office Door Access (AND Gate)

Both an employee ID card and a fingerprint must be valid (yes) to grant access.

Street Lights Control (OR Gate)

Street lights turn ON if it is either nighttime or motion is detected.

How to Use:

Run the program.

Choose an option:

(1) Office Door Access

(2) Street Lights Control

(3) Exit

Follow the prompts based on your choice.

2. 8-Puzzle Game
This is a simple interactive puzzle where the goal is to arrange numbers from 1 to 8, with 0 representing the empty space.

The goal state:
123
456
78_
Features:

Random puzzle generator.

Player moves the empty space (_) by typing up, down, left, or right.

Invalid moves are handled gracefully.

How to Play:

Run the puzzle code.

The puzzle will print automatically.

Input your move based on where you want to move the blank space.

Keep playing until you reach the goal state!

3. City Path Finder Game
A simple navigation game where the player moves between cities connected by direct roads.

Start from a current city (Lahore) and try to reach the goal city (Karachi).

Only allowed to move between cities directly connected to the current city.

Cities Map Example:

markdown
Lahore → Faisalabad → Sargodha → Chakwal → Kallar Kahar → Rawalpindi → Islamabad → Murree
                                                      ↓
                                                  Karachi (via Multan, Sukkur, Hyderabad)
How to Play:

You are shown your current city and available next cities.

Input your next move.

If the move is valid, you will move forward; otherwise, you will be asked to try again.

Continue until you reach Karachi!

Requirements
Python 3.x

No external libraries needed (only built-in Python modules are used)

How to Run
Save the Python code to a .py file (for example, logic_games.py).

Open your terminal or command prompt.

Navigate to the directory containing the file.

Run the command:

bash
python logic_games.py
Follow on-screen instructions to play.

Notes
Each task can be separated and run independently if needed.

These tasks demonstrate basic use of loops, conditions, functions, user input handling, and simple AI game strategies