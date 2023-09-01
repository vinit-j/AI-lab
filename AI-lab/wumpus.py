from kanren import run, eq, membero, var, conde, fresh
from sympy import Or, And

# Define symbols and variables
x, y = var(), var()

# Define the size of the grid (in this example, a 4x4 grid)
grid_size = 4

# Define the locations of the pits, gold, wumpus, and the starting point
pits = [(1, 2), (3, 3), (2, 4)]
gold = (3, 2)
wumpus = (1, 3)
start = (1, 1)

# Define the percept function
def percept(location):
    breeze = membero(location, pits)
    glitter = eq(location, gold)
    stench = eq(location, wumpus)
    return breeze, glitter, stench

# Define the possible actions (up, down, left, right)
actions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

# Define the safe location constraints
def safe_location(x, y):
    return And(1 <= x, x <= grid_size, 1 <= y, y <= grid_size, Or(*[And(x != px, y != py) for px, py in pits]))

# Define the rules for moving and shooting
def move_rules(x, y, x1, y1):
    return conde([eq((x1, y1), a), safe_location(x1, y1), eq((x, y), (x1, y1))])

# Define the rules for picking up gold
def pickup_gold(x, y):
    return eq((x, y), gold)

# Define the rules for shooting the wumpus
def shoot_wumpus(x, y, x1, y1):
    return And(eq((x, y), start), eq((x1, y1),
