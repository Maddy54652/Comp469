'''
Lab 3
Adam Larson and Madalyn Henderson
09/07/22
'''
#defining the problem that we will pass through
problem = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0, 'R', 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 'D', 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]

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
    #go to 'D' in problem
    #return location of D
    goalState = []
    x = 0
    y = 0
    for i in range(0,len(problem),1):
        for j in range(0,len(problem[i]),1):
            if(problem[i][j] == 'D'):
                x = i
                y = j
                goalState.append(x)
                goalState.append(y)
                return goalState


#Goal test
def goalTest(currentNode,goalLocation):
  if(currentNode.location == goalLocation):
    return True

currentNode = treeNode(findStartState(problem), 0, None)
goalState = findGoalState(problem)
#Create fringe and add current node
fringe = []
fringe.append(currentNode)
found = False
#Looping through a million times so we do not infinite loop
for i in range(1000000):
  currentNode = fringe[0]
  #check goal state
  if(goalTest(currentNode, goalState)):
    found = True
    break;
  #checking if left side is available
  if(problem[currentNode.location[0]][currentNode.location[1]-1] != 1):
    parentNode = currentNode
    currentLocate = [currentNode.location[0], currentNode.location[1]]
    cost = currentNode.cost
    #going down left side if it is available
    while(problem[currentLocate[0]][currentLocate[1]-1] != 1):
      currentLocate[1] -= 1
      cost += 1
    #creating new node and adding it to fringe to be unpacked later
    currentNode = treeNode(currentLocate, cost, parentNode)
    fringe.append(currentNode)
    currentNode = fringe[0]
  #checking if right side is available
  if(problem[currentNode.location[0]][currentNode.location[1]+1] != 1):
    parentNode = currentNode
    currentLocate = [currentNode.location[0], currentNode.location[1]]
    cost = currentNode.cost
    #going down right side if it is available
    while(problem[currentLocate[0]][currentLocate[1]+1] != 1):
      currentLocate[1] += 1
      cost += 1
    #creating new node and adding it to fringe to be unpacked later
    currentNode = treeNode(currentLocate, cost, parentNode)
    fringe.append(currentNode)
    currentNode = fringe[0]
  #checking if down side is available
  if(problem[currentNode.location[0]-1][currentNode.location[1]] != 1):
    parentNode = currentNode
    currentLocate = [currentNode.location[0], currentNode.location[1]]
    cost = currentNode.cost
    #going down side if it is available
    while(problem[currentLocate[0]-1][currentLocate[1]] != 1):
      currentLocate[0] -= 1
      cost += 1
    #creating new node and adding it to fringe to be unpacked later
    currentNode = treeNode(currentLocate, cost, parentNode)
    fringe.append(currentNode)
    currentNode = fringe[0]
  #checking if up side is available
  if(problem[currentNode.location[0]+1][currentNode.location[1]] != 1):
    parentNode = currentNode
    currentLocate = [currentNode.location[0], currentNode.location[1]]
    cost = currentNode.cost
    #going Up if it is available
    while(problem[currentLocate[0]+1][currentLocate[1]] != 1):
      currentLocate[0] += 1
      cost += 1
    #creating new node and adding it to fringe to be unpacked later
    currentNode = treeNode(currentLocate, cost, parentNode)
    fringe.append(currentNode)
    currentNode = fringe[0]
  #Removing starting index
  fringe.pop(0)
#If it fails
if(found == False):
  print("This is not possible to complete")
else:
  #Prints the puzzle
  print("Original Problem:")
  for i in range(0,len(problem),1):
    print(problem[i])
  #Prints the cost
  print("Cost: " + str(currentNode.cost))
  #Prints the path, needs to add it into a list to print it in ascending order
  print("Path: ")
  path = []
  while(currentNode != None):
    path.append(currentNode.location)
    currentNode = currentNode.parent
  for i in range(len(path)-1, -1, -1):
    print(path[i])
