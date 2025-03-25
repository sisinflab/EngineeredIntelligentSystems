from src.problem import GridProblem

problem = GridProblem(initial_state=(5, 0), goal_state=(2, 2))

print(problem.actions((0, 0)))
print(problem.actions((1, 1)))
print(problem.actions((1, 2)))

print(problem.result((2,2), 'down'))

print(problem.goal((2,2)))
