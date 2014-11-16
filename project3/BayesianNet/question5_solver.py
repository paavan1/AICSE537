import string
class Question5_Solver:
    def __init__(self, cpt2):
        self.cpt2 = cpt2;
        return;

    #####################################
    # ADD YOUR CODE HERE
    #         _________
    #        |         v
    # Given  z -> y -> x
    # Pr(x|z,y) = self.cpt2.conditional_prob(x, z, y);
    #
    # A word begins with "``" and ends with "``".
    # For example, the probability of word "ab":
    # Pr("ab") = \
    #    self.cpt2.conditional_prob("a", "`", "`") * \
    #    self.cpt2.conditional_prob("b", "`", "a") * \
    #    self.cpt2.conditional_prob("`", "a", "b") * \
    #    self.cpt2.conditional_prob("`", "b", "`");
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
                    prob = self.cpt2.conditional_prob(query[i], "`", "`")
                elif i == 1:
                    prob = prob * self.cpt2.conditional_prob(query[i], "`", query[i - 1])
                #To calculate the last probability
                elif i == len(query)-1:
                    prob = prob * self.cpt2.conditional_prob(query[i], query[i - 2], query[i - 1])
                    prob = prob * self.cpt2.conditional_prob("`", query[i - 1], query[i])
                    prob = prob * self.cpt2.conditional_prob("`", query[i], "`")
                    max_prob = prob
                #To calculate middle probabilities
                else:
                    if query[i - 1] == "_":
                        continue
                    if query[i - 2] == "_":
                        continue
                    else:
                        prob = prob * self.cpt2.conditional_prob(query[i], query[i - 2], query[i - 1])
                        max_prob = prob
            else:
                if i == 0 and len(query) == 2:
                    letter_before_1 = "`"
                    letter_before_2 = "`"
                    letter_after_1 = query[i + 1]
                    letter_after_2 = "`"
                    prob = 1.0
                elif i == 0:
                    letter_before_1 = "`"
                    letter_before_2 = "`"
                    letter_after_1 = query[i + 1]
                    letter_after_2 = query[i + 2]
                    prob = 1.0
                elif i == 1 and len(query) == 2:
                    letter_before_1 = "`"
                    letter_before_2 = query[i - 1]
                    letter_after_1 = "`"
                    letter_after_2 = "`"
                elif i == 1 and len(query) == 3:
                    letter_before_1 = "`"
                    letter_before_2 = query[i - 1]
                    letter_after_1 = query[i + 1]
                    letter_after_2 = "`"
                elif i == 1:
                    letter_before_1 = "`"
                    letter_before_2 = query[i - 1]
                    letter_after_1 = query[i + 1]
                    letter_after_2 = query[i + 2]
                elif i == len(query)-1:
                    letter_before_1 = query[i - 2]
                    letter_before_2 = query[i - 1]
                    letter_after_1 = "`"
                    letter_after_2 = "`"
                elif i == len(query)-2:
                    letter_before_1 = query[i - 2]
                    letter_before_2 = query[i - 1]
                    letter_after_1 = query[i + 1]
                    letter_after_2 = "`"
                else:
                    letter_before_2 = query[i - 1]
                    letter_before_1 = query[i - 2]
                    letter_after_1 = query[i + 1]
                    letter_after_2 = query[i + 2]


        #To iterate through all alphabets and check which gives the max prob
        #Handling the case when char is "_"
        alphs = string.ascii_lowercase
        all_prob = {}

        for i in alphs:
            prob = max_prob * self.cpt2.conditional_prob(i, letter_before_1, letter_before_2)
            prob = prob * self.cpt2.conditional_prob(letter_after_1, letter_before_2, i)
            prob = prob * self.cpt2.conditional_prob(letter_after_2, i, letter_after_1)

            if prob != 0.0:
                all_prob[i] = prob

        if len(all_prob.keys()) > 0:
            missing_letter = max(all_prob, key=all_prob.get)
        else:
            missing_letter = "t"

        return missing_letter
