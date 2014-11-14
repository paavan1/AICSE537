import string
class Question1_Solver:
    def __init__(self, cpt):
        self.cpt = cpt;
        return;

    # ####################################
    # ADD YOUR CODE HERE
    # Pr(x|y) = self.cpt.conditional_prob(x, y);
    # A word begins with "`" and ends with "`".
    # For example, the probability of word "ab":
    # Pr("ab") = \
    # self.cpt.conditional_prob("a", "`") * \
    #    self.cpt.conditional_prob("b", "a") * \
    #    self.cpt.conditional_prob("`", "b");
    # query example:
    #    query: "ques_ion";
    #    return "t";
    def solve(self, query):

        #To compare which letter gives max prob
        max_prob = 0.0
        #Probability
        prob = 0.0

        #To iterate through all the letters and calculate prob
        #Skip the calculation of prob when char is "_".
        for i, c in enumerate(query):
            if c != "_" and i <= len(query)-1:
                #To calculate the first probability
                if i == 0:
                    prob = self.cpt.conditional_prob(query[i], "`")
                #To calculate the last probability
                elif i == len(query)-1:
                    prob = prob * self.cpt.conditional_prob("`", query[i])
                    max_prob = prob
                #To calculate middle probabilities
                else:
                    if query[i - 1] == "_":
                        continue
                    else:
                        prob = prob * self.cpt.conditional_prob(query[i], query[i - 1])
                        max_prob = prob
            else:
                if i == 0:
                    letter_before = "`"
                    letter_after = query[i + 1]
                    prob = 1.0
                elif i == len(query)-1:
                    letter_before = query[i - 1]
                    letter_after = "`"
                else:
                    letter_before = query[i - 1]
                    letter_after = query[i + 1]


        #To iterate through all alphabets and check which gives the max prob
        #Handling the case when char is "_"
        alphs = string.ascii_lowercase
        all_prob = {}

        for i in alphs:
            prob = max_prob * self.cpt.conditional_prob(i, letter_before)
            prob = prob * self.cpt.conditional_prob(letter_after, i)

            if prob != 0.0:
                all_prob[i] = prob

        if len(all_prob.keys()) > 0:
            missing_letter = max(all_prob, key=all_prob.get)
        else:
            missing_letter = "a"

        return missing_letter;