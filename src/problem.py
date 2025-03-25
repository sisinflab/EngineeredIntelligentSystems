class GridProblem:
    def __init__(self, initial_state, goal_state,  environment=None):
        self.environment = environment
        self.initial_state = initial_state
        self.goal_state = goal_state

    def actions(self, state):
        actions = []
        x, y = state

        if x != 0:
            actions.append('up')
        if y != 0:
            actions.append('left')

        if x != 2:
            actions.append('down')

        if y != 2:
            actions.append('right')

        return actions

    def result(self, state, action):
        x, y = state
        if action == 'up':
            return (x-1, y)
        if action == 'down':
            return (x+1, y)
        if action == 'left':
            return (x, y-1)
        if action == 'right':
            return (x, y+1)

    def goal(self, state):
        return state == self.goal_state
