import re
from math import log
class Question1_Solver:
    def __init__(self, col=-1, res=None, node1=None, node2=None, node3=None):
        self.learn('train.data');
        self.col = col
        self.res = res
        self.node1 = node1
        self.node2 = node2
        self.node3 = node3
        self.label = ''
        self.is_leaf = None
        return;


    def divide_records(self, rows, column, value):
        split = lambda row: row[column] == value

        set1 = [row for row in rows if split(row)]
        set2 = [row for row in rows if not split(row)]
        return (set1,set2)

    def calculate_count(self, rows):
        rec = {}
        for i in rows:
            res = i[0]
            if res not in rec:
                rec[res] = 0
            else:
                rec[res] += 1
        return rec

    def calculate_entropy(self, rows):
        cal_log = lambda x: log(x)/log(2)
        res = self.calculate_count(rows)
        entropy = 0.0
        for result in res.keys():
            val = float(res[result])/len(rows)
            if val < 0.00001:
                val = 0.00001
            entropy -= val * cal_log(val)
        return entropy

    def build_tree(self, rows):
        if len(rows) == 0:
            return Question1_Solver()
        total_entropy = self.calculate_entropy(rows)

        highest_gain = 0.0
        best_attr = None
        best_sets = None
        label = ''

        column_count = len(rows[0])
        for col in range(1, column_count):
            # # Generate the list of different values in this column
            # column_values = {}
            # for row in rows:
            #     column_values[row[col]] = 1

            # Dividing the rows up for each value in this column
            # for value in column_values.get('y'):
            (set1, set2) = self.divide_records(rows, col, 'y')
            (set3, set4) = self.divide_records(set2, col, 'n')

            # Information gain
            p = float(len(set1))/len(rows)
            q = float(len(set3))/len(rows)
            gain = total_entropy - p * self.calculate_entropy(set1) - q * self.calculate_entropy(set3) - \
                (1-(p + q)) * self.calculate_entropy(set4)
            if gain > highest_gain:
                highest_gain = gain
                best_attr = col
                best_sets = (set1, set3, set4)

        # Creating the sub branches
        if highest_gain > 0:
            yBranch = self.build_tree(best_sets[0])
            nBranch = self.build_tree(best_sets[1])
            oBranch = self.build_tree(best_sets[2])
            return Question1_Solver(col=best_attr, node1=yBranch, node2=nBranch, node3=oBranch)
        else:
            return Question1_Solver(res=self.calculate_count(rows))


    # Add your code here.
    # Read training data and build your decision tree
    # Store the decision tree in this class
    # This function runs only once when initializing
    # Please read and only read train_data: 'train.data'
    def learn(self, train_data):

        # Storing the data in list
        records = []

        # Reading data from file
        with open(train_data) as line:
            data = line.readlines()

        # Processing the data and storing in a list
        for i in data:
            record = re.split('\t|,|\n', i)
            del record[-1]
            records.append(record)


        tree = self.build_tree(records)

        return;

    # Add your code here.
    # Use the learned decision tree to predict
    # query example: 'n,y,n,y,y,y,n,n,n,y,?,y,y,y,n,y'
    # return 'democrat' or 'republican'
    def solve(self, query):

        return 'democrat';

