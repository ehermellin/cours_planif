import pyplanning as pp
import time
import math

### Loading PDDL Files ###

domain, problem = pp.load_pddl("domain.pddl", "problem.pddl")

### Solving using BFS ###

#tic = time.time()
#plan = pp.solvers.search_plan(problem)
#print("Breadth-First Search")
#print("Execution Time: %.2f" % (time.time() - tic))
#print("Plan found:")
#print(plan, "\n")


### Solving using A* with goals remaining heuristic ###

tic = time.time()
plan = pp.solvers.search_plan(problem, pp.solvers.heuristics.goals_remaining(problem))
print("A* - Goals Remaining Heuristic (Note: Non-admissable)")
print("Execution Time: %.2f" % (time.time() - tic))
print("Plan found:")
print(plan, "\n")


### Solving using A* with a Custom Heuristic ###

def custom_heuristic(state):
    num_total = len(problem.goal_state.props)
    num_complete = 0
    for prop in state.knowledge:
        if prop in problem.goal_state.props:
            num_complete += 1
    return math.ceil((num_total-num_complete)/2)

#tic = time.time()
#plan = pp.solvers.search_plan(problem, custom_heuristic)
#print("A* - Custom Heuristic")
#print("Execution Time: %.2f" % (time.time() - tic))
#print("Plan found:")
#print(plan, "\n")


### Solving using GraphPlan ###

#tic = time.time()
#plan = pp.solvers.graph_plan(problem)
#print("Graph Plan")
#print("Execution Time: %.2f" % (time.time() - tic))
#print("Plan found:")
#print(plan, "\n")