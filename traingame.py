from itertools import permutations 
 
def train_game(number):
    """
    returns all equations to a four number sequence that equal ten
    output is a list of strings that can be eval()'d as expressions
    """

    combs = list(permutations([
                                "+", "+", "+", 
                                "-", "-", "-", 
                                "*", "*", "*",
                                "/", "/", "/",
                                ], 3))
    combs = list(dict.fromkeys(combs))
    solns = []

    for comb in combs:

        comb = list(comb)
        calc = [ number[0] , comb[0] , number[1] , comb[1] , number[2] , comb[2] , number[3] ]
        calc = ''.join(calc)

        try:

            if type(calc) != int and eval(calc) == float(10):
                solns.append(calc)
            elif type(calc) == int and eval(calc) == 10:
                solns.append(calc)

        # division by zero in equation is invalid, skip
        except ZeroDivisionError:
            continue

    return solns


def print_answers(calcs):
    for calc in calcs:
        print(">>>", calc, '= 10')

def find_solvable():
    for i in range(0,9999):
        number = str(i).zfill(4)
        if train_game(number) != []:
            # if solvable, just show one soln
            print(number, train_game(number)[-1])

find_solvable()
