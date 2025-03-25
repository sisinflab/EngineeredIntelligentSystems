class Node:
    def __init__(self, state, action=None, parent=None, depth=0, cost=0):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.action = action
        self.actual_cost = cost

    def __repr__(self):
        return str(self.state)

    def generate(self, state, action, cost):
        return Node(
            parent=self,
            state=state,
            depth=self.depth+1,
            action=action,
            cost=self.actual_cost+cost
        )

    def path(self):
        path = []
        node = self
        while node.parent is not None:
            path.append(node.action)
            node = node.parent
        path.reverse()
        return path


