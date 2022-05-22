import random

""" main function to execute one game of the professor calculator """


def main():
    score = 0   # user correct answers counter
    level = get_level()  # prompt user for game level
    problems = dict()   # dictionary to hold the math problems and their solutions

    # populating the problems dictionary with random generated math equations
    # while len(problems) < 10:
    for i in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        prob = f"{num1} + {num2} = "
        problems[prob] = num1 + num2

    # traversing the randomly generated problems and prompt the user to solve them
    # the user will have three chances to solve each problem in order to recieve score point for that question
    for problem in problems.keys():
        errors = 0
        correct_result = problems.get(problem)
        if(evaluate_problem(problem, correct_result)):
            score += 1

    print(f"Score: {score}")


""" function to prompt the user until the user inserting valid game level
    users can insert only levels 1, 2 or 3 """


def get_level():
    while True:
        inp = input("Level: ")
        if inp == "1" or inp == "2" or inp == "3":
            return inp


""" generates random integer with level number of digits
    if level is 1 return 1 digit random number, if level is 2 return 2 digit random number
    else return 3 digit random number """


def generate_integer(level):
    if level == "1":
        return random.randint(0, 9)
    elif level == "2":
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


""" evaluate one problem of the game by showing the user the problem
    and prompting the user for his answer, the function let the user answer the question up to 3 times
    if the user insert correct answer in one of those 3 chances the function will return True
    otherwise the function will return False which indicates the user wasn't able to
    provide correct answer in his given 3 chances """


def evaluate_problem(problem, correct_result):
    errors = 0
    while True:
        user_result = input(problem)
        if user_result.isnumeric():
            user_result = int(user_result)
            if user_result == correct_result:
                return True
            else:
                errors += 1
                if errors == 3:
                    print("EEE")
                    print(f"{problem} {correct_result}")
                    break
                else:
                    print("EEE")
                    continue
        else:
            errors += 1
            if errors == 3:
                print("EEE")
                print(f"{problem} {correct_result}")
                break
            else:
                print("EEE")
                continue
    return False


if __name__ == "__main__":
    main()
