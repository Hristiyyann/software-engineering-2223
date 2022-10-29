import math

class Circle:
    def __init__(self, circle_name, X, Y, radius):
       self.name = circle_name
       self.X = X
       self.Y = Y
       self.radius = radius

def distance_beetween_centers(first, second):
    return math.sqrt(math.pow((second.X - first.X),2) + math.pow((second.Y - first.Y),2))

def mutual_position(radii_sum, radii_subtraction, distance_beetween_centers):
    if distance_beetween_centers == radii_subtraction ==  0: return "They are equal"
    elif distance_beetween_centers > radii_sum: return "They don't touch"
    elif distance_beetween_centers == radii_sum: return "They touch externally"
    elif radii_subtraction < distance_beetween_centers < radii_sum: return "They intersect at two points"
    elif distance_beetween_centers == radii_subtraction: return "They touch internally"
    elif distance_beetween_centers < radii_subtraction: return "One lying inside other"
    
 
print(f"Input for first circle")
X1 = float(input("X : "))
Y1 = float(input("Y : "))
radius1 = float(input("Radius : ")) 

print(f"Input for second circle")
X2 = float(input("X : "))
Y2 = float(input("Y : "))
radius2 = float(input("Radius : ")) 
    
         
first_circle = Circle("first circle", X1, Y1, radius1)
second_circle = Circle("second circle", X2, Y2, radius2)
radii_sum = first_circle.radius + second_circle.radius
radii_subtraction = abs(first_circle.radius - second_circle.radius)
distance = distance_beetween_centers(first_circle, second_circle)
print(f'Sum {radii_sum} sub {radii_subtraction} dis {distance}')
print(mutual_position(radii_sum, radii_subtraction, distance))