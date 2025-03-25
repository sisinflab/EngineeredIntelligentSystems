from src.problem import GridProblem
from src.search import TreeSearch, VisualTreeSearch

problem = GridProblem(initial_state=(0, 0), goal_state=(2, 2))

mysearch = TreeSearch(problem=problem)
print(mysearch.search())

mysearch = VisualTreeSearch(problem=problem)
print(mysearch.search())
