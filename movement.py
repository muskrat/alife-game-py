"""
Entity movement subsystem for alife program

I K Stead, 12-09-2012
"""
import random

def random_pos(xlim, ylim):
    x = random.randint(1, xlim)
    y = random.randint(1, ylim)
    return (x, y)

def normalise(a, b):
    """Normalise a 2D vector, i.e. return a vector in the same direction as
    the vector between a and b but with unit length
    """
    dy = b[1] - a[1]
    dx = b[0] - a[0]
    vector = (dy ** 2 + dx ** 2) ** 0.5
    # Normalise, round and cast to int
    dx = int(round(dx / vector))
    dy = int(round(dy / vector))
   
    return (dx, dy) 

def move(source, dest, speed=0):
    """Return new position after one tick of movement given current position
    and destination
    """
    norm = normalise(source, dest)
    new_pos = (source[0] + norm[0], source[1] + norm[1])
    return new_pos

def update(entity_list):
    """Take a list of entity dicts and move them one step towards 
    their destination
    """
    for entity in entity_list:
        # If no destination, pick a new random one
        if entity["dest"] == None:
            entity["dest"] = random_pos(100, 100)
        
        # Only moveable entities should have the dest field
        if "dest" in entity:
            # Move one step towards destination
            cpos = entity["position"]
            dest = entity["dest"]
            entity["position"] = move(cpos, dest) 

        # Clear destination if it has been reached
        if entity["dest"] == entity["position"]:
            entity["dest"] = None
