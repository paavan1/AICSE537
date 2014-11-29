import math
class Question3_Solver:
    def __init__(self):
        return;

    # Add your code here.
    # Return the centroids of clusters.
    # You must use [(30, 30), (150, 30), (90, 130)] as initial centroids
    def solve(self, points):
        centroids = [[30, 60], [150, 60], [90, 130]]
        newcentroid = self.update_centroid(centroids,points)
        while(self.are_unequal(centroids,newcentroid)):
            centroids = newcentroid
            newcentroid = self.update_centroid(centroids,points)
        return newcentroid
        
    def dist(self, p1, p2):
        return math.sqrt(math.pow(p1[0]-p2[0],2) + math.pow(p1[1]-p2[1],2))
    def update_centroid(self,centroids,points):
        print "updating centroid"
        distances = [0.0,0.0,0.0]
        assignments = []
        pointsineachcentroid = [0,0,0]
        for data in points:
            for i in range(0,3):
                distances[i] = self.dist(data,centroids[i])
            assignments.append(distances.index(min(distances)))
        
        newcentroids = [[0, 0], [0, 0], [0, 0]]
        
        for i in range(0,len(points)):
            pointsineachcentroid[assignments[i]] += 1
            newcentroids[assignments[i]][0] += points[i][0]
            newcentroids[assignments[i]][1] += points[i][1]
        for i in range(0,3):
            newcentroids[i][0] /= pointsineachcentroid[i]
            newcentroids[i][1] /= pointsineachcentroid[i]
        return newcentroids;
        
    def are_unequal(self, p1,p2):
        booleanarray = []
        for i in range(0,3):
            for j in range(0,2):
                booleanarray.append(p1[i][j] == p2[i][j])
        return not all(booleanarray)