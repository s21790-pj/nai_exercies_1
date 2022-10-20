import random

from typing import List
from simpleai.search import SearchProblem, astar

# Answer to the task
GOAL = "1234"


class BullsAndCowsProblem(SearchProblem):
    # Initialization of bull score and cow score tables
    bulls = ["x" for x in range(len(GOAL))]
    cows = [""]

    def actions(self, state: str) -> List:
        """
        The method responsible for verifying the current result, and selecting missing numbers.
        The method first selects for missing numbers those that are contained in the cows.
        If there are more missing numbers than cows, the numbers are selected randomly
        so that they are not present in bulls and cows.
        :param state: Current answer in the form of a 4-digit number written as a string
        :return: One-element array, containing the missing drawn numbers in string form
        """
        missing_numbers = ""
        if state != GOAL:
            for num in self.bulls:
                if num in self.cows:
                    self.cows.pop(self.cows.index(num))
            if self.cows[0] != "":
                temp_cows = "".join(self.cows)
                self.cows[0] = temp_cows
                for missing_number in range(self.bulls.count("x") - len(temp_cows)):
                    chosen_number = str(random.randint(0, 9))
                    while (chosen_number in self.bulls) or (chosen_number in temp_cows):
                        chosen_number = str(random.randint(0, 9))
                    missing_numbers += chosen_number
                temp_cows += missing_numbers
                self.cows[0] = temp_cows
                return self.cows
            else:
                missing_numbers = ""
                for it in range((self.bulls.count("x"))):
                    chosen_number = str(random.randint(0, 9))
                    while (
                        chosen_number in self.bulls or chosen_number in missing_numbers
                    ):
                        chosen_number = str(random.randint(0, 9))
                    missing_numbers += chosen_number
                return [missing_numbers]

    def result(self, state: str, action: str) -> str:
        """
        The method responsible for creating a new result by randomly
        substituting in the missing places the numbers obtained from the action method.
        :param state: Current answer in the form of a 4-digit number written as a string
        :param action:
        :return:
        """
        state = self.bulls
        temp_cows = list(action)

        for it in range((self.bulls.count("x"))):
            chosen_number = random.choice(temp_cows)
            temp_cows.pop(temp_cows.index(chosen_number))
            self.bulls[self.bulls.index("x")] = chosen_number

        self.cows = temp_cows
        state = self.bulls
        return "".join(state)

    def is_goal(self, state: str) -> bool:
        """
        A method that verifies the correctness of the current answer with the expected result.
        :param state: Current answer in the form of a 4-digit number written as a string
        :return: True if the answer and the result are the same otherwise False
        """
        return state == GOAL

    def heuristic(self, state: str) -> int:
        """
        The method responsible for verifying the state of the answer.
        In the method, the number of cows and bulls is obtained.
        Also, the number of incorrect digits in the result is determined
        by verifying the number of 'x' in the bulls array.
        :param state: Current answer in the form of a 4-digit number written as a string
        :return: Number of incorrect digits in the current answer
        """
        self.cows = [""]
        result = ""

        for it in range(len(GOAL)):
            if state[it] == GOAL[it]:
                self.bulls[it] = state[it]
            else:
                self.bulls[it] = "x"

        for it in range(len(GOAL)):
            if (state[it] in GOAL) and (state[it] not in self.bulls):
                result += str(state[it])
            self.cows[0] = result

        state = self.bulls
        wrong = sum([0 if state[i] != "x" else 1 for i in range(len(state))])
        return wrong


def generate_num_v2() -> str:
    """
    The method responsible for generating a random number as the initial answer to a task.
    :return: A number consisting of 4 random, non-repeating digits
    """
    while True:
        num = random.randint(1000, 9999)
        numbers = list(str(num))
        if len(numbers) == len(set(numbers)):
            return str(num)


problem = BullsAndCowsProblem(initial_state=generate_num_v2())
result = astar(problem)

print(result.state)
print(result.path())
