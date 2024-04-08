import numpy as np
import matplotlib.pyplot as plt
import random as rd

points = {"green" : [],
          "purple" : []}

epoch = 15

for i in range(epoch):

    x, y = rd.uniform(-5,-1), rd.uniform(-5,-1)
    values = [x,y]
    points['green'].append(values)

for i in range(epoch):

    x, y = rd.uniform(1,5), rd.uniform(1,5)
    values = [x,y]
    points['purple'].append(values)


new_point = [rd.uniform(-3,3), rd.uniform(-3,3)]

def get_distance(p, q):

    return np.sqrt(np.sum((np.array(p) - np.array(q)) ** 2))

def get_highest_category(points):

    categories = {}

    for value in points:

        if value[1] in categories.keys():

            categories[value[1]] += 1

        else:

            categories[value[1]] = 1

    most_viewed = ""
    count = 0
    
    for key in categories:
        
        if most_viewed == "": 
            most_viewed = key
            count = categories[key]
            continue
            
        if categories[key] > count:
            most_viewed = key
            count = categories[key]
            
    return most_viewed
            

class KNearestNeighbor:

    def __init__(self, k=3):
        
        self.k = k
        self.points = None

    def fit(self, points):

        self.points = points

    def predict(self, new_point):

        distance = []

        for category in self.points:

            for point in self.points[category]:

                dist = get_distance(point, new_point)
                
                distance.append([dist, category])

        distance = sorted(distance)

        return get_highest_category(distance[:self.k])
    

obj = KNearestNeighbor(5)

obj.fit(points)

found_color = obj.predict(new_point)

ax = plt.subplot()
ax.grid(True, color = '#121212')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis="x", color='white')
ax.tick_params(axis="y", color='white')

green = '#42f56c'

color = green if found_color == 'green' else "#8142f5"

for point in points['green']:

    ax.scatter(point[0], point[1], c = green, s = 50)
    print(f"{point} ploted, color = green")

for point in points["purple"]:
    
    ax.scatter(point[0], point[1], c = "#8142f5", s = 50)
    print(f"{point} ploted, color = purple")

ax.scatter(new_point[0], new_point[1], c=color, marker="*", s=200)

for point in points['green']:

    ax.plot([new_point[0], point[0]], [new_point[1], point[1]], c = green, ls = '--', lw = 0.5)
    

for point in points['purple']:

    ax.plot([new_point[0], point[0]], [new_point[1], point[1]], c = "#8142f5", ls = '--', lw = 0.5)

plt.xlim(-5, 5)
plt.ylim(-5, 5)


plt.show()
