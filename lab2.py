'''
Lab 2
Adam Larson and Madalyn Henderson
8/31/22
'''
#defining the problem that we will pass through
problem = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0, 'R', 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 'D', 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]

#goalTest
#successor function
#save plan and return solution
#ask user for map to play
#calculate cost

#Defining the tree node
class treeNode:
  def __init__(l, c, p):
    location = l
    parent = p
    cost = c
  def updateLocation(l):
    location = l
  def updateParent(p):
    parent = p
  def updateCost(c):
    cost = c

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

def goalTest(currentNode):
  if(currentNode.location == goalLocation):
    return True

currentNode = treeNode(findStartState(problem), 0)
#Create fringe and add current node
fringe = []
fringe.append(currentNode)
for i in 1000000:
  currentNode = fringe[0]
  if(problem[currentNode[0].location[0]-1][currentNode[0].location[1]] != 1):
    currentNode.updateParent(currentNode)
    while(problem[currentNode[0].location[0]-1][currentNode[0].location[1]] != 1):
      currentLocate = [currentNode[0].location[0]-1, currentNode[0].location[1]]
      currentNode.updateLocation(currentLocate)
      currentNode.updateCost(currentNode.cost + 1)
    fringe.append(currentNode)
    currentNode = fringe[0]
