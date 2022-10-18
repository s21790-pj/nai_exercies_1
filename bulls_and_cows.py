import random

from simpleai.search import SearchProblem, astar

GOAL = "7564"


class BullsAndCowsProblem(SearchProblem):
    bulls = ['x' for x in range(len(GOAL))]
    cows = []

    def actions(self, state):
        print(f'here in actions | state {state}')
        print(f'self.bulls {self.bulls}')

        if state != GOAL:
            for num in self.bulls:
                if num in self.cows:
                    print('HERE')
                    self.cows.pop(self.cows.index(num))
            if self.cows:
                return self.cows
            else:
                print('HERE')
                chosen_numer = random.randint(0, 9)

                while chosen_numer in self.bulls:
                    chosen_numer = random.randint(0, 9)
                return str(chosen_numer)

    def result(self, state, action):
        state = self.bulls
        print(f'here in result | state {state}')
        print(f"action: {action}")
        print(f'self.bulls {self.bulls}')
        print(f'self.cows {self.cows}')
        temp_cows = self.cows

        for it in range(len(state)):
            chosen_numer = random.choice(action)
            if self.bulls[it] == 'x':
                self.bulls[it] = chosen_numer

        state = self.bulls

        return ''.join(state)

    def is_goal(self, state):
        print(f'here in is_goal | state {state}')
        return state == GOAL

    def heuristic(self, state):
        print(f'here in heuristic | state {state}')

        for it in range(len(GOAL)):
            if (state[it] in GOAL) and (state[it] not in self.cows):
                self.cows.append(state[it])

        for it in range(len(GOAL)):
            if state[it] == GOAL[it]:
                self.bulls[it] = state[it]
            else:
                self.bulls[it] = 'x'

        state = self.bulls
        wrong = sum([0 if state[i] != 'x' else 1 for i in range(len(state))])
        print(f"wrong: {wrong}")
        return wrong


def generate_num_v2():
    while True:
        num = random.randint(1000, 9999)
        numbers = list(str(num))
        if len(numbers) == len(set(numbers)):
            return str(num)


# problem = BullsAndCowsProblem(initial_state=generate_num_v2())
problem = BullsAndCowsProblem(initial_state='4675')
result = astar(problem)

print(result.state)
print(result.path())
