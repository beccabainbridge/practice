#step climbing or change counting
def total_ways(total, methods):
    if total == 0:
        return 1
    elif total < 0 or not methods:
        return 0
    else:
        return total_ways(total - methods[-1], methods) + total_ways(total, methods[:-1])

steps = [1, 2, 3]
change = [1, 5, 10, 25, 50]

print total_ways(5, steps)
print total_ways(11, change)

paths = {}

# project euler 15
def lattice_paths(width, height):
    if (width, height) in paths:
        pass
    elif width == 0 and height == 0:
        return 1
    elif width < 0 or height < 0:
        return 0
    else:
        paths[(width, height)] =  lattice_paths(width-1, height) + lattice_paths(width, height-1)
    return paths[(width, height)]


print lattice_paths(2,2)
print lattice_paths(10,10)
print lattice_paths(20,20)
