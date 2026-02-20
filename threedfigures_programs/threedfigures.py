import math

# -------- CUBE --------
def cube_volume(a):
    return a ** 3

def cube_tsa(a):
    return 6 * a * a


# -------- CUBOID --------
def cuboid_volume(l, b, h):
    return l * b * h

def cuboid_csa(l, b, h):
    return 2 * h * (l + b)

def cuboid_tsa(l, b, h):
    return 2 * (l*b + b*h + l*h)


# -------- CYLINDER --------
def cylinder_volume(r, h):
    return math.pi * r * r * h

def cylinder_csa(r, h):
    return 2 * math.pi * r * h

def cylinder_tsa(r, h):
    return 2 * math.pi * r * (r + h)


# -------- CONE --------
def cone_volume(r, h):
    return (1/3) * math.pi * r * r * h

def cone_csa(r, h):
    l = math.sqrt(r*r + h*h)
    return math.pi * r * l

def cone_tsa(r, h):
    l = math.sqrt(r*r + h*h)
    return math.pi * r * (r + l)


# -------- SPHERE --------
def sphere_volume(r):
    return (4/3) * math.pi * r**3

def sphere_tsa(r):
    return 4 * math.pi * r**2


# -------- HEMISPHERE --------
def hemisphere_volume(r):
    return (2/3) * math.pi * r**3

def hemisphere_csa(r):
    return 2 * math.pi * r**2

def hemisphere_tsa(r):
    return 3 * math.pi * r**2