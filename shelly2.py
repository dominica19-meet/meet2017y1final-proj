import turtle
a = ["apple", "banana", "strawberry", "orange", "grape"]

a.sort()

clones_list = []
for n in range(len(a)):
    obj = turtle.clone()
    clones_list.append(obj)
    turtle.register_shape(a[n])
    obj.shape(a[n])
