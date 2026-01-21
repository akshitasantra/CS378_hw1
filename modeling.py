import unified_planning
from unified_planning.shortcuts import *

room = UserType('room')
mobile_robot = UserType('mobile_robot')
mobile_manipulator = UserType('mobile_manipulator', mobile_robot)
mobile_vacuum = UserType('mobile_vacuum', mobile_robot)

tidy = Fluent('tidy', rm=room)
clean = Fluent('clean', rm=room)
connected = Fluent('connected_rooms', rm1=room, rm2=room)
current_room = Fluent('current_room', r=mobile_robot, rm=room)

move_room = InstantaneousAction('move_room', r=mobile_robot, rm_from=room, rm_to=room)
move_room_robot = move_room.parameter('r')
move_room_from = move_room.parameter('rm_from')
move_room_to = move_room.parameter('rm_to')
move_room.add_precondition(current_room(move_room_robot, move_room_from))
move_room.add_precondition(connected(move_room_to, move_room_from))
move_room.add_effect(current_room(move_room_robot, move_room_from), False)
move_room.add_effect(current_room(move_room_robot, move_room_to), True)

tidy_room = InstantaneousAction('tidy_room', r=mobile_manipulator, rm=room)
tidy_room_robot = tidy_room.parameter('r')
tidy_room_room = tidy_room.parameter('rm')
tidy_room.add_precondition(current_room(tidy_room_robot, tidy_room_room))
tidy_room.add_effect(tidy(tidy_room_room), True)
tidy_room.add_effect(clean(tidy_room_room), False)

clean_room = InstantaneousAction('clean_room', r=mobile_vacuum, rm=room)
clean_room_robot = clean_room.parameter('r')
clean_room_room = clean_room.parameter('rm')
clean_room.add_precondition(current_room(clean_room_robot, clean_room_room))
clean_room.add_precondition(tidy(clean_room_room))
clean_room.add_effect(clean(clean_room_room), True)

# Base Problem
problem = Problem('problem')
problem.add_fluent(tidy)
problem.add_fluent(clean)
problem.add_fluent(connected)
problem.add_fluent(current_room)
problem.add_action(move_room)
problem.add_action(tidy_room)
problem.add_action(clean_room)

# Map 1
map1 = problem.clone()
r1 = map1.add_object('r1', room)
r2 = map1.add_object('r2', room)
mv1 = map1.add_object('mv1', mobile_vacuum)
mm1 = map1.add_object('mm1', mobile_manipulator)
map1.set_initial_value(connected(r1, r2), True)
map1.set_initial_value(connected(r2, r1), True)
map1.set_initial_value(current_room(mm1, r1), True)
map1.set_initial_value(current_room(mv1, r1), True)
map1.set_initial_value(clean(r1), False)
map1.set_initial_value(clean(r2), False)
map1.set_initial_value(tidy(r1), False)
map1.set_initial_value(tidy(r2), False)
map1.add_goal(clean(r1))
map1.add_goal(clean(r2))
map1.add_goal(tidy(r1))
map1.add_goal(tidy(r2))

def prob1():
    return map1

# Map 2
map2 = problem.clone()
nw = map2.add_object('nw', room)
ne = map2.add_object('ne', room)
sw = map2.add_object('sw', room)
se = map2.add_object('se', room)

map2.set_initial_value(connected(nw, ne), True)
map2.set_initial_value(connected(ne, nw), True)

map2.set_initial_value(connected(nw, sw), True)
map2.set_initial_value(connected(sw, nw), True)

map2.set_initial_value(connected(se, ne), True)
map2.set_initial_value(connected(ne, se), True)

map2.set_initial_value(connected(se, sw), True)
map2.set_initial_value(connected(sw, se), True)

mm1 = map2.add_object('mm1', mobile_manipulator)
mv1 = map2.add_object('mv1', mobile_vacuum)
map2.set_initial_value(current_room(mm1, sw), True)
map2.set_initial_value(current_room(mv1, ne), True)
map2.set_initial_value(clean(nw), False)
map2.set_initial_value(clean(ne), False)
map2.set_initial_value(clean(sw), False)
map2.set_initial_value(clean(se), False)
map2.set_initial_value(tidy(nw), False)
map2.set_initial_value(tidy(ne), False)
map2.set_initial_value(tidy(sw), False)
map2.set_initial_value(tidy(se), False)
map2.add_goal(clean(nw))
map2.add_goal(clean(ne))
map2.add_goal(clean(sw))
map2.add_goal(clean(se))
map2.add_goal(tidy(nw))
map2.add_goal(tidy(ne))
map2.add_goal(tidy(sw))
map2.add_goal(tidy(se))

def prob2():
    return map2

# Map 3
map3 = problem.clone()
rm1 = map3.add_object('rm1', room)
rm2 = map3.add_object('rm2', room)
rm3 = map3.add_object('rm3', room)
rm4 = map3.add_object('rm4', room)
rm5 = map3.add_object('rm5', room)
rm6 = map3.add_object('rm6', room)
rm7 = map3.add_object('rm7', room)
rm8 = map3.add_object('rm8', room)
corridor = map3.add_object('corridor', room)

mm1 = map3.add_object('mm1', mobile_manipulator)
map3.set_initial_value(current_room(mm1, corridor), True)
mv1 = map3.add_object('mv1', mobile_vacuum)
map3.set_initial_value(current_room(mv1, corridor), True)


map3.set_initial_value(connected(corridor, rm1), True)
map3.set_initial_value(connected(rm1, corridor), True)
map3.set_initial_value(connected(corridor, rm2), True)
map3.set_initial_value(connected(rm2, corridor), True)
map3.set_initial_value(connected(corridor, rm3), True)
map3.set_initial_value(connected(rm3, corridor), True)
map3.set_initial_value(connected(corridor, rm4), True)
map3.set_initial_value(connected(rm4, corridor), True)
map3.set_initial_value(connected(corridor, rm5), True)
map3.set_initial_value(connected(rm5, corridor), True)
map3.set_initial_value(connected(corridor, rm6), True)
map3.set_initial_value(connected(rm6, corridor), True)
map3.set_initial_value(connected(corridor, rm7), True)
map3.set_initial_value(connected(rm7, corridor), True)
map3.set_initial_value(connected(corridor, rm8), True)
map3.set_initial_value(connected(rm8, corridor), True)

map3.set_initial_value(clean(rm1), False)
map3.set_initial_value(clean(rm2), False)
map3.set_initial_value(clean(rm3), False)
map3.set_initial_value(clean(rm4), False)
map3.set_initial_value(tidy(rm1), True)
map3.set_initial_value(tidy(rm2), True)
map3.set_initial_value(tidy(rm3), True)
map3.set_initial_value(tidy(rm4), True)

map3.set_initial_value(clean(rm5), True)
map3.set_initial_value(clean(rm6), True)
map3.set_initial_value(clean(rm7), True)
map3.set_initial_value(clean(rm8), True)
map3.set_initial_value(tidy(rm5), False)
map3.set_initial_value(tidy(rm6), False)
map3.set_initial_value(tidy(rm7), False)
map3.set_initial_value(tidy(rm8), False)

map3.add_goal(clean(rm1))
map3.add_goal(clean(rm2))
map3.add_goal(clean(rm3))
map3.add_goal(clean(rm4))
map3.add_goal(clean(rm5))
map3.add_goal(clean(rm6))
map3.add_goal(clean(rm7))
map3.add_goal(clean(rm8))
map3.add_goal(tidy(rm1))
map3.add_goal(tidy(rm2))
map3.add_goal(tidy(rm3))
map3.add_goal(tidy(rm4))
map3.add_goal(tidy(rm5))
map3.add_goal(tidy(rm6))
map3.add_goal(tidy(rm7))
map3.add_goal(tidy(rm8))


def prob3():
    return map3

from unified_planning.engines import PlanGenerationResultStatus

def solve(prob):
    planner = OneshotPlanner(name='pyperplan')
    result = planner.solve(prob)
    if result.status in [PlanGenerationResultStatus.SOLVED_SATISFICING,
                         PlanGenerationResultStatus.SOLVED_OPTIMALLY]:
        print("SOLVED. Plan length:", len(result.plan.actions), "Plan:", result.plan.actions)
    else:
        print("NOT SOLVED")
    

print("Map1")
solve(prob1())

print("Map2")
solve(prob2())

print("Map3")
solve(prob3())

