def goUp(location,xVal):
  i = xVal
  while(location[i] != '1'):
    i+=1
    xVal = i
  return xVal
    
def goDown(location,xVal):
    i = xVal
  while(location[i] != '1'):
    i-=1
    xVal = i
  return xVal
def goLeft(location,yVal):
  i = yVal
  while(location[i] != '1'):
    i = i-1
    yVal = i
  return yVal
def goRight(location,yVal):
  i = yVal
  while(location[i] != '1'):
    i = i+1
    yVal = i
