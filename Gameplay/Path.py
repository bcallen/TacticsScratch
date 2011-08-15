#Path.py
#Private class within Board

class Path:
    '''
    Ordered path of coordinates on the board.

    Moves from space to adjacent space.  
    Each space in the path is guaranteed 
    to be adjacent to the steps in the
    path that are listed next to it.
    '''
    def __init__(self, xPosition = None, yPosition = None):
	if Path != None:
	    self._path = Path
	else:
	    self._path = []
	if path != None:
	    self._path.append(path)
     
    # REQ:  None
    # RET:  Returns the list of coords in the path,  optional endstep allows the return of a subpath
    def GetPath(self, endStep = 999):
	''' '''
	if self.GetPathLength < endStep:
	    returnPath = self._path [0:endStep]
	else:
	    returnPath = self._path
	return Path(returnPath)

    def len(self):
	''' '''
	return len(self.getPath())

    def GetPoint(self, step):
	'''Return a point based on it's location in the path.
	
	Note that negatives start with the last step of the path.
	'''
	pathLength = self.getPathLength()
	if pathLength != 0 and step < pathLength and step >= -pathLength:
	    return self.getPath()[step]
	else:
	    return None

    def GetStep(self, xPosition, yPosition)
	''' Return the path step of a given board location

	If the coordinates are not on the path, then return 0 '''
	if thisList.count((xPosition, yPosition)) == 0:
             return -1
	else:
             return thisList.index((xPosition, yPosition))


    # REQ:  integers xPosition and yPosition representing
    #	    coordinates on the board.
    # RET:  Void.  Adds the new position to the route.
    def AddStep(self, xPosition, yPosition, board):
	'''' '''
	if board.IsOnBoard(xPosition, yPosition) == False:
		pass #TODO throw exception
	if self.getPathLength() == 0 or self.getPoint(-1) in board.IsAdjacent(_lastLocation, xPosition, yPosition):
	    self._path.append((xPosition, yPosition))
   
   # REQ: None
   # RET: Final step in the path, which has been removed
    def CutStep(self):
	if self.getPathLength() == 0:
	    pass
	else:
	    return self._path.pop(-1)
