from src.node import Node
from graphviz import Digraph


def expand(node, problem):
    actions = problem.actions(node.state)
    reached_states = [problem.result(state=node.state,
                                     action=a) for a in actions]
    new_nodes = [node.generate(state=s,
                               action=a,
                               cost=1) for s, a in zip(reached_states, actions)]
    return new_nodes


class VisualTreeSearch:
    def __init__(self, problem, strategy=None):
        self.problem = problem
        self.tree = Digraph()

    def search(self):
        root_node = Node(state=self.problem.initial_state)
        fringe = [root_node]
        self.tree.node(str(root_node.state))
        edges = set()

        while len(fringe) != 0:
            node = fringe.pop()
            print(f'Node: {node}')
            if self.problem.goal(node.state):
                return node.path()

            new_nodes = expand(node, self.problem)
            for n in new_nodes:
                self.tree.node(str(n.state))
                edge = str(node.state), str(n.state), str(n.action)
                if edge not in edges:
                    edges.add(edge)
                    self.tree.edge(str(node.state), str(n.state), label=n.action)

            fringe = new_nodes + fringe

            print(fringe)
            self.tree.render('tree', format='png', view=True)
            input()

        return 'Fail'


class TreeSearch:
    def __init__(self, problem, strategy=None):

        self.problem = problem

    def search(self):
        root_node = Node(state=self.problem.initial_state)
        fringe = [root_node]

        while len(fringe) != 0:
            node = fringe.pop()
            print(f'Node: {node}')
            if self.problem.goal(node.state):
                return node.path()

            new_nodes = expand(node, self.problem)
            fringe = new_nodes + fringe
            print(fringe)
            input()

        return 'Fail'
