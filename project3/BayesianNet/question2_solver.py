import string
class Question2_Solver:
    def __init__(self, cpt):
        self.cpt = cpt;
        return;

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
    #    query: "que__ion";
    #    return ["s", "t"];
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
                    if query[i - 1] == "_":
                        prob = prob * self.cpt.conditional_prob("`", query[i])
                        max_prob = prob
                    else:
                        prob = prob * self.cpt.conditional_prob(query[i], query[i - 1])
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
                    if query[i + 1] == "_":
                        letter_before = "`"
                        letter_after = query[i + 2]
                        prob = 1.0
                elif i == 1:
                    letter_before = "`"
                    letter_after = query[i + 1]
                elif i == len(query)-1:
                    if query[i - 1] == "_":
                        letter_before = query[i - 2]
                        letter_after = "`"
                else:
                    if query[i + 1] == "_":
                        letter_before = query[i - 1]
                    elif query[i - 1] == "_":
                        letter_after = query[i + 1]

        alphs = string.ascii_lowercase
        all_prob = {}

        #Check the combination of letters that give maximum probability
        for i in alphs:
            for j in alphs:
                prob = max_prob * self.cpt.conditional_prob(i, letter_before)
                prob = prob * self.cpt.conditional_prob(j, i)
                prob = prob * self.cpt.conditional_prob(letter_after, j)

                if prob != 0.0:
                    all_prob[i + ":" + j] = prob

        if len(all_prob.keys()) > 0:
            missing_letter = max(all_prob, key=all_prob.get)
        else:
            missing_letter = "t:a"

        result = missing_letter.split(':')
        return result
