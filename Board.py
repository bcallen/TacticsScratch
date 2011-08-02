'''
Created on Jul 21, 2011

@author: Bonual
'''
#Note: Board should be a singleton.  Use singleton dev. pattern to
#      ensure that at most one board exists at any time!
class Board:
    '''
    The board stores all active pieces and spaces.
    
    It controls all information about the spatial
    orientation of Spaces and Pieces, the movement 
    costs based on space characteristic and other 
    spatial information.
    '''
    #####################################################
    ###########----Internal class: Path----##############
    class Path:
	'''
	A path represents a specific route on the board.
	'''
	def __init__(self, route):
	    _route = []
	

	def containsSubpath(self, path):
	    pass

    ##############----End path class----##################
    ######################################################

    def __init__(self): 
        _map = []
        _pieces = []
        
    def GetSpace(self,xPosition,yPosition):
	""" """
        invertedY = len(self._map) - yPosition - 1
        return self._map [invertedY][xPosition]
    
    def GetPiece(self,xPosition,yPosition):
	""" """
        invertedY = len(self._pieces) - yPosition - 1
        #Do something special if there's no piece?
        return self._pieces [invertedY][xPosition]
        
    def LoadMap (self, mapStringMatrix):
        """ """
        #Takes a matrix of strings and sets up the map by filling the
        #_map with Spaces, and loading the space characteristics with the
        #Space class LoadMapString method. Set the _pieces matrix to the
        #size of the _map matrix
        pass
        
    def CalcPieceMoveCost(self, fromLoc, toLoc, terrainMoveCostMap, altMoveCostDict):
        """ """
	DeadEnds = set([])
	if self.getPiece(toLoc) == None:
	    #Maybe check if this is an opposing piece,  if it is then route should be checked.
	    #if the piece is not occupiable and not opposing then don't calc.
	else:
	    #Main
	    pass
	#Use specific movement costs to return the number of movement points
        #required to move from one space to another. Intention - piece movement
        #ranged attack calcs, any other cost driven, movement related calc.
        
        pass 
    
    ##################---Private methods---##################
    #Helper method for CalcMoveCost.  Uses a 'Carpeting' approach to cover a set square.
    #Adds to the set of 'dead end' routes that don't make it to the target but
    #are higher cost than the cheapest route.

    #1.  Works a block of all non-folding/non-overlapping routes within the square universe between the startPos and endPos.
    #	 Each route is tested against the current 'best' route.  As soon as the test route being traced
    #	 becomes greater than or equal to the cost of the best route traced so far, the partial route to that point
    #	 is saved as a 'dead end'. All routes containing a known dead-end are skipped with no further calculation.
    #2.	 If the current testing route is better than the prior best route, it becomes the best route.
    #	 Dead ends are then re-checked against the new best route and shortened if possible.
    #3.	 Result provided is the list of dead ends along with the current best route.

    def __MoveCostCarpeting(self, startPos, endPos, terrainMoveCostMap, altMoveCostDict)
	for ColumnNo in range(len(self._map)):#TODO probably add max row/column counts rather than range(len(...))
	    for space in column:
    
    #Hmm probably not neccessary. Just check the other map...
    #Add a "roadblock" to the map for each piece not controlled by the player who controls
    #the active piece.
    def	__AddMoveCostRoadblock(self)
	for ColumnNo in range(len(self._map)):
	    for RowNo in range(len(self.map(ColumnNo)))
		if self.GetPiece(ColumnNo,RowNo) != None:
		    

    def __testBoard(self):
        #Check that every point on the map always has a space.
        #Check null and bad map string matrices.
        #Check null and bad piece string matrices.
	#Check distance calculations on validation maps/pieces.
        pass


