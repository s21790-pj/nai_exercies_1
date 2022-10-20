import random

from simpleai.search import SearchProblem, astar

GOAL = "7564"


class BullsAndCowsProblem(SearchProblem):
    bulls = ['x' for x in range(len(GOAL))]
    cows = ['']

    def actions(self, state):
        """

        :param state:
        :return:
        """
        missing_numbers = ''
        if state != GOAL:
            for num in self.bulls:
                if num in self.cows:
                    self.cows.pop(self.cows.index(num))
            if self.cows[0] != '':
                temp_cows = ''.join(self.cows)
                self.cows[0] = temp_cows
                for missing_number in range(self.bulls.count('x') - len(temp_cows)):
                    chosen_number = str(random.randint(0, 9))
                    while (chosen_number in self.bulls) or (chosen_number in temp_cows):
                        chosen_number = str(random.randint(0, 9))
                    missing_numbers += chosen_number
                temp_cows += missing_numbers
                self.cows[0] = temp_cows
                return self.cows
            else:
                missing_numbers = ''
                for it in range((self.bulls.count('x'))):
                    chosen_number = str(random.randint(0, 9))
                    while chosen_number in self.bulls or chosen_number in missing_numbers:
                        chosen_number = str(random.randint(0, 9))
                    missing_numbers += chosen_number
                return [missing_numbers]

    def result(self, state, action):
        """

        :param state:
        :param action:
        :return:
        """
        # 4
        state = self.bulls
        temp_cows = list(action)

        for it in range((self.bulls.count('x'))):
            chosen_number = random.choice(temp_cows)
            temp_cows.pop(temp_cows.index(chosen_number))
            self.bulls[self.bulls.index('x')] = chosen_number

        self.cows = temp_cows
        state = self.bulls
        return ''.join(state)

    def is_goal(self, state):
        """

        :param state:
        :return:
        """
        return state == GOAL

    def heuristic(self, state):
        """

        :param state:
        :return:
        """
        self.cows = ['']
        result = ''

        for it in range(len(GOAL)):
            if state[it] == GOAL[it]:
                self.bulls[it] = state[it]
            else:
                self.bulls[it] = 'x'

        for it in range(len(GOAL)):
            if (state[it] in GOAL) and (state[it] not in self.bulls):
                result += str(state[it])
            self.cows[0] = result

        state = self.bulls
        wrong = sum([0 if state[i] != 'x' else 1 for i in range(len(state))])
        return wrong


def generate_num_v2():
    """

    :return:
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
