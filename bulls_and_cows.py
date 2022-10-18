import random

from simpleai.search import SearchProblem, astar

GOAL = "7564"


class BullsAndCowsProblem(SearchProblem):
    bulls = ['x' for x in range(len(GOAL))]
    cows = []

    def actions(self, state):
        print(f'here in actions | state {state}')
        if state != GOAL:
            return list('0123456789')
        else:
            return []

    def result(self, state, action):
        print(f'here in result | state {state}')
        print(f'self.bulls {self.bulls}')
        print(f'self.cows {self.cows}')
        state = self.bulls
        temp_cows = self.cows

        for it in range(len(state)):
            if state[it] == 'x':
                if temp_cows:
                    chosen_number = random.choice(temp_cows)
                    state[it] = chosen_number
                    temp_cows.pop(temp_cows.index(chosen_number))
                else:
                    state[it] = action

        return ''.join(state)

    def is_goal(self, state):
        print(f'here in is_goal | state {state}')
        return state == GOAL

    def heuristic(self, state):
        print(f'here in heuristic | state {state}')

        for it in range(len(state)):
            if state[it] == GOAL[it]:
                self.bulls[it] = state[it]
            else:
                self.bulls[it] = 'x'
        state = self.bulls

        for it in range(len(GOAL)):
            if (state[it] in GOAL) and (state[it] not in self.cows) and (state[it] not in self.bulls):
                self.cows.append(state[it])

        wrong = sum([0 if state[i] != 'x' else 1 for i in range(len(state))])
        print(f"wrong: {wrong}")
        return wrong


def generate_num_v2():
    # while True:
        num = random.randint(1000, 9999)
        numbers = list(str(num))
        if len(numbers) == len(set(numbers)):
            return str(num)


problem = BullsAndCowsProblem(initial_state=generate_num_v2())
result = astar(problem)

print(result.state)
print(result.path())
