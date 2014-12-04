import numpy
import math
class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.middle = None
        self.data = None
        
class Question1_Solver:
    def __init__(self):
        self.model = self.learn('train.data');
        return;

    # Add your code here.
    # Read training data and build your decision tree
    # Store the decision tree in this class
    # This function runs only once when initializing
    # Please read and only read train_data: 'train.data'
    def learn(self, train_data):
        #Read the data and populate vector
        with open(train_data) as f:
            content = f.readlines()
        datas = numpy.zeros((len(content),16))
        labels = numpy.zeros((len(content)))
        integer = 0
        for data in content:
            
            data = data.split()
            if data[0] == 'democrat':
                whichcrat = 0
            if data[0] == 'republican':
                whichcrat = 1
            tempdata = data[1].split(',')
            temp = []
            index = 0
            for value in tempdata:
                
                if value == 'y':
                    datas[integer][index] = 1
                if value == 'n':
                    datas[integer][index] = 0
                if value == '?':
                    datas[integer][index] = 2
                index = index + 1
            labels[integer] = whichcrat
            integer = integer + 1
        features = []
        for i in range(0,16):
            features.append(i)
        root = Tree()
        root = self.build_tree(root, features, datas, labels, 'democrat')
        return root;
        
    
    def build_tree(self, root, features, datas, labels, string):

        if len(labels) == 0:
            root.data = string
            return root
        if self.checkEqual(labels):
            if labels[0] == 0:
                root.data = 'democrat'
            if labels[0] == 1:
                root.data = 'republican'
            return root
        if len(features) == 0:
            if (len(labels)-sum(labels))>sum(labels):
                root.data = 'democrat'
            else:
                root.data = 'republican'
            return root
        
        chosen = self.choose_feature(features, datas, labels)
        root.data = chosen
        newroot1 = Tree()
        newroot2 = Tree()
        newroot3 = Tree()
        newfeatures = [x for x in features if x != chosen]
        yesses = []
        nos = []
        questionmarks = []
        index = 0

        for response in datas[:,chosen]:
            if response == 1:
                yesses.append(index)
            if response == 0:
                nos.append(index)
            if response == 2:
                questionmarks.append(index)
            index = index + 1

        root.right = self.build_tree(newroot1, newfeatures, datas[yesses][:], labels[yesses], 'democrat')
        root.left = self.build_tree(newroot2, newfeatures, datas[nos][:], labels[nos], 'democrat')
        root.middle = self.build_tree(newroot3, newfeatures, datas[questionmarks][:], labels[questionmarks], 'democrat')
        return root
        
    def checkEqual(self, iterator):
       return len(set(iterator)) <= 1
    # Add your code here.
    # Use the learned decision tree to predict
    # query example: 'n,y,n,y,y,y,n,n,n,y,?,y,y,y,n,y'
    # return 'republican' or 'republican'
    def choose_feature(self, features, datas, labels):
        return features[0]
    def solve(self, query):
        tempdata = query.split(',')
        index = 0
        data = numpy.zeros((16))
        for value in tempdata:
            
            if value == 'y':
                data[index] = 1
            if value == 'n':
                data[index] = 0
            if value == '?':
                data[index] = 2
            index = index + 1
        output = self.model
        while(output.data != 'democrat' and output.data != 'republican'):

            if(data[output.data] == 1):
                output = output.right
            else:
                if(data[output.data] == 0):
                    output = output.left
                else:
                    if(data[output.data] == 2):
                        output = output.middle
        return output.data;

