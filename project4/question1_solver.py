import re
from math import log
class Question1_Solver:
    def __init__(self, col=-1, value=None, res=None, node1=None, node2=None, node3=None):
        self.learn('train.data');
        self.col = col
        self.value = value
        self.res = res
        self.node1 = node1
        self.node2 = node2
        self.node3 = node3
        return;

    entropy = 0.0
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
        global entropy
        cal_log = lambda x: log(x)/log(2)
        res = self.calculate_count(rows)

        for result in res.keys():
            val = float(res[result])/len(rows)
            entropy -= val * cal_log(val)
        return entropy

    def build_tree(self, rows, scoref=entropy):
        print scoref
        if len(rows) == 0:
            return Question1_Solver()
        curr_score = scoref(rows)

        highest_gain = 0.0
        best_attribute = None
        best_sets = None

        column_count = len(rows[0])-1



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

        results = []
        for i, c in enumerate(records):
            results.append(records[i][0])

        (set1, set2) = self.divide_records(records, 1, '?')
        (set3, set4) = self.divide_records(set2, 1, 'y')
        # print set1.__len__()
        # print set3.__len__()
        # print set4.__len__()
        # print self.calculate_count(records)
        # print self.calculate_entropy(set2)
        self.build_tree(records)


        return;

    # Add your code here.
    # Use the learned decision tree to predict
    # query example: 'n,y,n,y,y,y,n,n,n,y,?,y,y,y,n,y'
    # return 'republican' or 'republican'
    def solve(self, query):
        return 'democrat';

