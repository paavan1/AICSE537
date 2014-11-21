import string
import re
class Question4_Solver:
    def __init__(self, cpt):
        alphs = ["`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                 "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        #Below is the cpt for one hidden variable
        #given characters are in rows
        self.cpt_onehidden = [[0 for x in range(27)] for x in range(27)]
        sum_prob = 0

        for left_let in alphs:
            for right_let in alphs:
                sum_prob=0
                for mid_let in alphs:
                    sum_prob += cpt.conditional_prob(mid_let, left_let) * cpt.conditional_prob(right_let, mid_let)
                i_right = ord(right_let) - 96
                i_left = ord(left_let) - 96
                self.cpt_onehidden[i_right][i_left] = sum_prob
                    
                    
        self.cpt_twohidden = [[0 for x in range(27)] for x in range(27)]
        for left_let in alphs:
            for right_let in alphs:
                i_right = ord(right_let) - 96
                i_left = ord(left_let) - 96
                sum_prob=0
                for mid_let in alphs:
                    i_mid=ord(mid_let) - 96
                    sum_prob += cpt.conditional_prob(mid_let, left_let) * self.cpt_onehidden[i_right][ i_mid]
                
                self.cpt_twohidden[i_right][i_left] = sum_prob
                    
        self.cpt = cpt;
        return;
    def findProb(self,letter,word1):
         word=word1
         i= word1.index("_")
         word=re.sub('[_]', letter, word) 
         #word = word1[:i-1]+ letter + word1[i+1:]
         print word
         prob=1;
         for i, c in enumerate(word):
          if   c!="-" and i <= len(word)-1:
                #To calculate the first probability
                if i == 0:
                    prob = self.cpt.conditional_prob(word[i], "`")
                elif i == 1 and word[i-1]=="-":
                     prob = prob * self.cpt_onehidden[ord(word[i])-96][ord("`")-96]
                elif i == 2 and word[i-1]=="-" and  word[i-2]=="-":
                     prob = prob * self.cpt_twohidden[ord(word[i])-96][ord("`")-96]
                #To calculate the last probability
                elif i == len(word)-1 :
                    if(word[i]=="-" and word[i-1]=="-"):
                     prob = prob * self.cpt_twohidden[ord("`")-96][ ord(word[i-2])-96]
                    elif(word[i]=="-" ):
                     prob = prob * self.cpt_onehidden[ord("`")-96][ ord(word[i-1])-96]
                    else:
                     prob = prob * self.cpt.conditional_prob("`", word[i])
                    
                #To calculate middle probabilities
                else:
                    
                    if(word[i-1]=="-" and word[i-2]=="-"):
                     prob = prob * self.cpt_twohidden[ord(word[i])-96][ ord(word[i-3])-96]
                    elif(word[i-1]=="-" ):
                     prob = prob * self.cpt_onehidden[ord(word[i])-96][ord(word[i-2])-96]
                    else:
                     print  word[i]
                     prob = prob * self.cpt.conditional_prob(word[i], word[i-1])
         else:
             if i == len(word)-1 :
                    if(word[i]=="-" and word[i-1]=="-"):
                     prob = prob * self.cpt_twohidden[ord("`")-96][ ord(word[i-2])-96]
                    elif(word[i]=="-" ):
                     prob = prob * self.cpt_onehidden[ord("`")-96][ ord(word[i-1])-96]
                    else:
                     prob = prob * self.cpt.conditional_prob("`", word[i])
         print prob
         return prob;
     


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
    #    query: ["que-_-on", "--_--icial",
    #            "in_elligence", "inter--_"];
    #    return "t";
    def solve(self, query):
        #To compare which letter gives max prob
        max_prob = 0.0
        #Probability
        prob = 0.0
        missing_letter=""
        words= query
        #To iterate through all the letters and calculate prob
        #Skip the calculation of prob when char is "_".
        alphs = string.ascii_lowercase
        for letter in alphs:
         prob=1.0
         for word in words:
             
            prob=prob*self.findProb(letter,word)
         if(max_prob<prob):
             max_prob=prob
             missing_letter=letter   
             
           

        return missing_letter;
     
    