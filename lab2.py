'''
Lab 2
Adam Larson and Madalyn Henderson
8/31/22
'''
#defining the problem that we will pass through
problem = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0, 'R', 1], [1, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 'D', 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]

#define start state
#goalTest
#create fringe
#successor function
#save plan and return solution
#ask user for map to play
#calculate cost

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
