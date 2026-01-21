import unified_planning
from unified_planning.shortcuts import *

simple_problem = Problem('simple_problem')
x = Fluent('x', BoolType())

a = InstantaneousAction('a')
a.add_effect(x, True)

simple_problem.add_fluent(x)
simple_problem.add_action(a)
simple_problem.set_initial_value(x, False)
simple_problem.add_goal(x)

planner = OneshotPlanner(name='pyperplan')
result = planner.solve(simple_problem)
print(result)