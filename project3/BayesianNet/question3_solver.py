class Question3_Solver:
    def __init__(self, cpt):
        alphs = ["`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                 "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        #Below is the cpt for one hidden variable
        #given characters are in rows
        self.cpt3 = [[0 for x in range(27)] for x in range(27)]
        sum_prob = 0

        for left_let in alphs:
            for right_let in alphs:
                for mid_let in alphs:
                    sum_prob += cpt.conditional_prob(mid_let, left_let) * cpt.conditional_prob(right_let, mid_let)
                    i_right = ord(right_let) - 96
                    i_left = ord(left_let) - 96
                    self.cpt3[i_right][i_left] = sum_prob

        self.cpt = cpt;

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

        return "t";

