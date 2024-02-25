# train-game
Outputs all solutions to the train game

### What is the the train game again?
Train carriages often have a "carriage identification number" consisting of four numbers. In the train game, a person seeks to create an equation with these four numbers that adds to ten. For example, a solution to `8028` would be `8*0+2+8`. Not every set of four numbers is solvable. This program outputs all carriage identification numbers that have solutions alongside one solution (though more than one solution may be possible).

### Reccomended usage
`python3 traingame.py > solns.txt`

### What is this code doing?
To find all solvable carriage identification numbers, `find_solvable()` first generates every four number sequence. For each of these, `train_game()` is called, generating every possible equation and checking if `eval()` is equal to `10`. All solutionss are returned in a list of strings. `find_solvable()` determines if each number is solvable by checking if `train_game()` returns an empty list (no solutions) or not. 

### Limitations / The Future ... 
Some variations of the game's ruleset have could be covered in the future, including:
* Arranging the four numbers in any order.
* Allowing `sin()`, `cos()`, `^2`, and `^(1/2)` (current available operations are (`+`,`-`,`*`,`/`))
* Allowing brackets in calcuations
If the goal of this project is to quickly verify whether a number is solvable, a database could be populated to answer queries faster. Additional columns could exist for different rulesets e.g. a number might be solvable in one ruleset but not another.
