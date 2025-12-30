# Week 2 – Turn-Based Battle Simulator

## Student Information

Name: Alejandro R
GitHub Username: Turbo170

---

## Project Overview

This project is a turn-based battle simulator written in Python.

The player and an enemy take turns attacking until one of them is defeated.  
The game uses loops, lists, and randomness to control game flow and outcomes.

---

## Programs Included

This week includes multiple small practice programs and one main project.

### Mini Assignments

- `countdown.py` – Uses a while loop to count down
- `list_practice.py` – Uses a list and a for loop
- `random_damage.py` – Uses the random module

### Main Assignment

- `battle_simulator.py` – Turn-based battle game

---

## Concepts Used

This project demonstrates the following concepts:

- `while` loops
- `for` loops
- Lists and list indexing
- Iterating over lists
- Random number generation
- Conditional logic
- Basic game loop structure

---

## How to Run the Programs

From inside the `week2` folder, run any file using:

`python filename.py`


Examples:

```python countdown.py
python list_practice.py
python random_damage.py
python battle_simulator.py```


---

## Battle Simulator Description

Briefly describe how your battle simulator works:

- How does the player attack?
- How does the enemy attack?
- What determines a win or loss?
- Are there any player choices?

(Write 4–6 sentences.)

Both the player and enemy attacks are chosen randomly with the damage being random as well. A win or loss are determined once one of you hit 0 health. I did not "include" any
player choices even though I had a list of moves (used it for other code).
---

## Design Decisions

Describe any design choices you made:

- Why did you use lists the way you did?
- How did you structure your loop?
- Did you add anything optional or extra?

(2–4 sentences.)

 I used the list as a way so the code can randomly choose one of the moves to be selected and printed. The loop starts with the player starting the loop with enter, begining their turn and automatically creating a random attack damage number, moving onto a random move, printing the random attack and damage, finally printing both the player hp and enemy hp. The end of the loop also includes an if statement for when one of you reach 0 hp. For the enemy, the loop code is the exact same.
---

## Known Issues or Limitations

List any bugs, missing features, or improvements you would make with more time.

If none, write:  
`None`

I could have added the actual features of selecting the moves, but i kinda forgot a bit of the code for it. Also, im not sure on how to make critical chances code for those moves.
---

## Reflection

Answer the following questions:

- What concept from this week was the most challenging?
- What concept do you feel most confident about?
- What part of your code are you most proud of?

(3–5 sentences total.)

In general, working on the battle sim was a bit hard because we only worked on random damage this week, and there were some things that I didnt know of like
import random, import time, and random.choice, which i needed to look up. As well looking up if I were doing the right things. It looks simple now that I have finally done it.
Im most confident in my use of variables in the prints, as well as import time. Im doing a lot better with if statements as of finishing the sim.
Im most proud of my use of if import random and random.randint() because i was totally confused at the start of how they work, and finally got used to it.
---