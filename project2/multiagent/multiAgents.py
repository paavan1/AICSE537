# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)
        self._expanded = 0
        
class MinimaxAgent(MultiAgentSearchAgent):
     
    def getAction(self, gameState):
      #Generating the legal actions
          legalActions = gameState.getLegalActions()
          maxscore= -999999
          for action in legalActions:
          #Getting the successor game states from the pacman initial state
            newGameState = gameState.generateSuccessor(0,action) 
          #Getting the min score of the successor game state
            score = self.minValue(newGameState, 0,  1)
          #update the maximum value and best action
            if (score >maxscore):
             maxscore = score
             bestaction=action
          print "Expanded nodes: " + str(self._expanded)
          
          return bestaction
    def minValue(self, gameState, currentDepth, ghostIndex):
    #Terminal state check - return the evaluation function of the  state
        self._expanded+=1
        if self.testterminalstate(gameState, currentDepth):
            return self.evaluationFunction(gameState)
    
    
    
        #Get the list of legal actions for the current ghost
        ghostLegalActions = gameState.getLegalActions(ghostIndex)
    
        minscore= 999999
    
        #Get the number of ghosts from the game state
        ghostnumber = gameState.getNumAgents() - 1
        #Looping thought the current ghost's moves
        for action in ghostLegalActions:
            newGameState= gameState.generateSuccessor(ghostIndex, action)
        #if the current ghost is the last ghost then switch to the max function
        #  else call the min function for next ghost agent
            if(ghostIndex == ghostnumber):
            
               scores = self.maxValue(newGameState, currentDepth + 1)
        
            elif(ghostIndex < ghostnumber):
            
               scores = self.minValue(newGameState, currentDepth, ghostIndex + 1)
            if(scores<minscore):
                minscore=scores
        #returning the minimum value of all scores
        return minscore

    
    def maxValue(self, gameState, currentDepth):
    
        self._expanded+=1
         #Terminal state check - return the evaluation function of the  state
        if self.testterminalstate(gameState, currentDepth):
            return self.evaluationFunction(gameState)
    
        #Generate the legal pacman actions
        pacmanLegalActions = gameState.getLegalActions()
    
        maxscore= -999999
        #For every valid pacman action, compute scores
        for action in pacmanLegalActions:
            if not (action == 'STOP'):
                newGameState = gameState.generateSuccessor(0,action)
                pacmanScores = self.minValue(newGameState, currentDepth , 1)
                if(pacmanScores>maxscore):
                    maxscore=pacmanScores
        #Return the maximum score
        return maxscore
    def testterminalstate(self,gameState,currentDepth):
        # check for loss or win or maximum depth reached 
          if self.depth == currentDepth or gameState.isLose() or gameState.isWin() :
              return True
          else:
              return False

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
          alpha = float('-Inf')
        
          beta = float('inf')
        # current score
          score = float('-Inf')
      #Generating the legal actions
          legalActions = gameState.getLegalActions()
          maxscore= float('-Inf')
          for action in legalActions:
          #Getting the successor game states from the pacman initial state
            newGameState = gameState.generateSuccessor(0,action) 
          #Getting the min score of the successor game state
            score = self.minValue(newGameState, 0,  1,alpha,beta)
          #update the maximum value and best action
            if (score >maxscore):
             maxscore = score
             bestaction=action
            alpha=max(alpha,maxscore)
          print "Expanded nodes: " + str(self._expanded)
          return bestaction
    def minValue(self, gameState, currentDepth, ghostIndex,alpha,beta):
    #Terminal state check - return the evaluation function of the  state
        self._expanded+=1
        if self.testterminalstate(gameState, currentDepth):
            return self.evaluationFunction(gameState)
    
    
        minscore = float('inf') 
        #Get the list of legal actions for the current ghost
        ghostLegalActions = gameState.getLegalActions(ghostIndex)
    
        
    
        #Get the number of ghosts from the game state
        ghostnumber = gameState.getNumAgents() - 1
        #Looping thought the current ghost's moves
        for action in ghostLegalActions:
            newGameState= gameState.generateSuccessor(ghostIndex, action)
        #if the current ghost is the last ghost then switch to the max function
        #  else call the min function for next ghost agent
            if(ghostIndex == ghostnumber):
                
                   score = self.maxValue(newGameState, currentDepth + 1,alpha,beta)
            
            elif(ghostIndex < ghostnumber):
                
                   score= self.minValue(newGameState, currentDepth, ghostIndex + 1,alpha,beta)
            #alpha pruning
            if(score<alpha):
                return score
            elif(score<minscore):
                minscore=score
            
            beta=min(beta,score)
        #returning the minimum value of all scores
        return minscore

    
    def maxValue(self, gameState, currentDepth,alpha,beta):
        maxscore = float('-Inf')
        self._expanded+=1
         #Terminal state check - return the evaluation function of the  state
        if self.testterminalstate(gameState, currentDepth):
            return self.evaluationFunction(gameState)
    
        #Generate the legal pacman actions
        pacmanLegalActions = gameState.getLegalActions()
    
    
        #For every valid pacman action, compute scores
        for action in pacmanLegalActions:
            if not (action == 'STOP'):
                newGameState = gameState.generateSuccessor(0,action)
                pacmanScore = self.minValue(newGameState, currentDepth , 1,alpha,beta)
                 #beta pruning
                if(pacmanScore>beta):
                 return pacmanScore
                elif(pacmanScore>maxscore):
                 maxscore=pacmanScore
                alpha=max(alpha,pacmanScore)
        #Return the maximum score
        return maxscore
    def testterminalstate(self,gameState,currentDepth):
        # check for loss or win or maximum depth reached 
          if self.depth == currentDepth or gameState.isLose() or gameState.isWin() :
              return True
          else:
              return False
class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
    """
      Your agent for the mini-contest
    """

    def getAction(self, gameState):
        """
          Returns an action.  You can use any method you want and search to any depth you want.
          Just remember that the mini-contest is timed, so you have to trade off speed and computation.

          Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
          just make a beeline straight towards Pacman (or away from him if they're scared!)
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

