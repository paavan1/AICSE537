import numpy
import math
class Question2_Solver:
    def __init__(self):
        probabilities = self.learn('train.data');
        self.probabilities = probabilities
        return;

    # Add your code here.
    # Read training data and build your naive bayes classifier
    # Store the classifier in this class
    # This function runs only once when initializing
    # Please read and only read train_data: 'train.data'
    def learn(self, train_data):
        #Initialize model with zero probabilities
        probabilities = numpy.zeros((2,3,16))
        for i in range(0,16):
            #probabilities is a list with indices [democrat|republican][y|n|?][features]
            probabilities[0][0][i] = 0
            probabilities[0][1][i] = 0
            probabilities[0][2][i] = 0
            probabilities[1][0][i] = 0
            probabilities[1][1][i] = 0
            probabilities[1][2][i] = 0
        #Read the data and populate counts
        with open(train_data) as f:
            content = f.readlines()
        for data in content:
            data = data.split()
            if data[0] == 'democrat':
                whichcrat = 0
            if data[0] == 'republican':
                whichcrat = 1
            tempdata = data[1].split(',')
            index = 0
            for value in tempdata:
                if value == 'y':
                    probabilities[whichcrat][0][index] = probabilities[whichcrat][0][index] + 1
                if value == 'n':
                    probabilities[whichcrat][1][index] = probabilities[whichcrat][1][index] + 1
                if value == '?':
                    probabilities[whichcrat][2][index] = probabilities[whichcrat][2][index] + 1
                index = index + 1
        #normalize and take logs
        numoftraindata = probabilities[0][0][0] + probabilities[0][1][0] + probabilities[0][2][0]
        for i in range(0,2):
            for j in range(0,3):
                for k in range(0,16):
                    probabilities[i][j][k] = (probabilities[i][j][k]+1)/(numoftraindata+16)
        return probabilities;
    
    def calc_prob(self, query, whichcrat):
        tempdata = query.split(',')
        index = 0
        prob_to_calc = 1
        for value in tempdata:
            if value == 'y':
                prob_to_calc = prob_to_calc *self.probabilities[whichcrat][0][index]
            if value == 'n':
                prob_to_calc = prob_to_calc *self.probabilities[whichcrat][1][index]
            if value == '?':
                prob_to_calc = prob_to_calc *self.probabilities[whichcrat][2][index]
            index = index + 1
        return prob_to_calc;
    
    # Add your code here.
    # Use the learned naive bayes classifier to predict
    # query example: 'n,y,n,y,y,y,n,n,n,y,?,y,y,y,n,y'
    # return 'republican' or 'republican'
    def solve(self, query):
        prob = [0.0,0.0]
        prob[0] = self.calc_prob(query,0)
        prob[1] = self.calc_prob(query,1)
        if prob[0] == prob[1]:
            return 'republican'
        if prob[0]>prob[1]:
            return 'democrat';
        else:
            return 'republican'
