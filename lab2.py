'''
Lab 2
Adam Larson and Madalyn Henderson
8/31/22
'''
#defining the problem that we will pass through
problem = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0, 'R', 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 'D', 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]

#successor function
#save plan and return solution

#Defining the tree node
class treeNode:
  def __init__(self, l, c, p):
    self.location = l
    self.parent = p
    self.cost = c

#define start state
def findStartState(problem):
    #go to 'R' in problem
    #return location of R
    startState = []
    x = 0
    y = 0
    for i in range(0,len(problem),1):
        for j in range(0,len(problem[i]),1):
            if(problem[i][j] == 'R'):
                x = i
                y = j
                startState.append(x)
                startState.append(y)
                return startState

#define goal state
def findGoalState(problem):
    #go to 'G' in problem
    #return location of G
    goalState = []
    x = 0
    y = 0
    for i in range(0,len(problem),1):
        for j in range(0,len(problem[i]),1):
            if(problem[i][j] == 'G'):
                x = i
                y = j
                goalState.append(x)
                goalState.append(y)
                return goalState


#Goal test
def goalTest(currentNode,goalLocation):
  if(currentNode.location == goalLocation):
    return True

currentNode = treeNode(findStartState(problem), None,0) #making parent node NULL
#Create fringe and add current node
fringe = []
fringe.append(currentNode)
#Looping through a million times so we do not infinite loop
#check for goal state
for i in range 1000000:
  currentNode = fringe[0]
  #checking if left side is available
  if(problem[currentNode[0].location[0]-1][currentNode[0].location[1]] != 1):
    parentNode = currentNode
    currentLocate = [currentNode[0].location[0], currentNode[0].location[1]]
    cost = currentNode.cost
    #going down left side if it is available
    while(problem[currentLocate[0]-1][currentLocate[1]] != 1):
      currentLocate[0] -= 1
      cost+=1
    #creating new node and adding it to fringe to be unpacked later
    currentNode = treeNode(currentLocate, parentNode, cost)
    fringe.append(currentNode)
    currentNode = fringe[0]
