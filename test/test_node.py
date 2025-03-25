from src.node import Node

parent = Node(state='Corato')

child = parent.generate(state='Altamura', action='goToAltamura', cost=10)

childofmychild = child.generate(state='Minervino', action='goToMinervino', cost=20)

print(child.state)
print(child.actual_cost)
print(child.parent.state)

print(childofmychild.actual_cost)

path = [childofmychild.action, childofmychild.parent.action, childofmychild.parent.parent.action]

print(path)
print(childofmychild.path())
