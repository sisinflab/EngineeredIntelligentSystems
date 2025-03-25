from src.node import Node
from graphviz import Digraph

dot = Digraph()

node = Node(state='root', parent=None, action=None, cost=0, depth=0)

actions = range(10)
states = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

dot.node('root')
for action, state in zip(actions, states):
    new_state = state
    dot.node = new_state
    dot.edge(node.state, new_state, label=str(action))
    node = node.generate(state=state, action=action, cost=1)

print(node.path())
dot.render('tree', format='png', view=True)