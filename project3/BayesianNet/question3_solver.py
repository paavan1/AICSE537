import string
class Question3_Solver:
    def __init__(self, cpt):
        alphs = ["`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                 "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        mid_alphs = string.ascii_lowercase
        #Below is the cpt for one hidden variable
        #given characters are in rows
        self.cpt3 = [[0 for x in range(27)] for x in range(27)]
        sum_prob = 0.0

        for left_let in alphs:
            for right_let in alphs:
                sum_prob = 0.0
                for mid_let in mid_alphs:
                    sum_prob += cpt.conditional_prob(left_let, mid_let) * cpt.conditional_prob(mid_let, right_let)
                    i_right = ord(right_let) - 96
                    i_left = ord(left_let) - 96
                    self.cpt3[i_left][i_right] = sum_prob

        #Below is the cpt for 2 hidden variables
        self.cpt4 = [[0 for x in range(27)] for x in range(27)]
        sum_prob = 0.0

        for left_let in alphs:
            for right_let in alphs:
                sum_prob = 0.0
                for mid_let in mid_alphs:
                    # print left_let+mid_let+right_let
                    i_left = ord(left_let) - 96
                    i_mid = ord(mid_let) - 96
                    i_right = ord(right_let) - 96
                    sum_prob += cpt.conditional_prob(left_let, mid_let) * self.cpt3[i_mid][i_right]
                    self.cpt4[i_left][i_right] = sum_prob

        self.cpt = cpt

    #####################################
    # ADD YOUR CODE HERE
    # Pr(x|y) = self.cpt.conditional_prob(x, y);
    # A word begins with "`" and ends with "`".
    # For example, the probability of word "ab":
    # Pr("ab") = \
    #    self.cpt.conditional_prob("a", "`") * \
    #    self.cpt.conditional_prob("b", "a") * \
    #    self.cpt.conditional_prob("`", "b");
    # query example:
    #    query: "qu--_--n";
    #    return "t";
    def solve(self, query):

        alphs = ["`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                 "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        #To compare which letter gives max prob
        max_prob = -9999999999.0
        #missing letter
        missing_letter = '*'

        #To check if its first "-"
        is_first = False
        #To check if its second "-"
        is_second = False
        query = "`" + query + "`"

        mid_alphs = string.ascii_lowercase
        for letters in mid_alphs:
            #replacing "_" with various alphabets
            q = query.replace("_", letters)
            prob = 1.0
            letter_before = query[0]
            count = 0
            for c, i in enumerate(q):
                count += 1
                if i == "-":
                    if count == 1:
                        letter_before = i
                        continue
                    if is_first:
                        is_first = False
                        is_second = True
                    else:
                        is_first = True
                        is_second = False
                else:
                    if count == 1:
                        letter_before = i
                        continue
                    if is_first == False and is_second == False:
                        prob *= self.cpt.conditional_prob(i, letter_before)
                        #If its the first "-"
                    elif is_first == True:
                        prob *= self.cpt3[ord(i) - 96][ord(letter_before) - 96]
                        is_first = False
                        #If its the second "-"
                    elif is_second == True:
                        prob *= self.cpt4[ord(i) - 96][ord(letter_before) - 96]
                        is_second = False
                    else:
                        print "Error"
                if i != "-":
                    letter_before = i
            #To check if the prob is greater than max prob else assign to max prob
            if prob > max_prob:
                max_prob = prob
                missing_letter = letters

        #To return the missing letter
        return missing_letter

