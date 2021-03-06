'''
Created on Jul 21, 2011

@author: Bonual
'''
#Note: Board should be a singleton.  Use singleton dev. pattern to
#      ensure that at most one board exists at any time!
import heapq

class Board:
    '''
    The board stores all active pieces and spaces.
    
    It controls all information about the spatial
    orientation of Spaces and Pieces, the movement 
    costs based on space characteristic and other 
    spatial information.
    '''
        
    def __init__(self): 
        self._map = []
        self._pieces = []
        
    def GetSpace(self,xPosition,yPosition):
        """ """
        return self._map [yPosition][xPosition]
    
    def GetPiece(self,xPosition,yPosition):
        """ """
        return self._pieces [yPosition][xPosition]
    
    def LoadMap (self, SpaceMatrix):
        """Loads the spaces on the map"""
        pass

    def LoadPosition (self, PositionMatrix):
        """Loads the pieces on the map"""
        pass
    
    def CalculateMoveCosts(self, fromLoc):
        """ """
        moveCost = 0
        toLoc = fromLoc
        ActivePiece = GetPiece(fromLoc)
        Paths = {fromLoc : (moveCost, toLoc)}
        Potentials = [(self.__CalcMoveCost(fromLoc,toLoc,ActivePiece),
            fromLoc, toLoc) for toLoc in self.GetAdjacents(fromLoc)]
        heapq.heapify(Potentials)
        while Potentials != []:
            while True:
                currentMin = heapq.heappop(Potentials)
                if Potentials == [] or currentMin[2] not in Paths:
                    moveCost, fromLoc, toLoc = (currentMin[0], currentMin[1], currentMin[2])
                    break
            if not toLoc in Paths:
                Paths.setdefault(toLoc , (moveCost, fromLoc))
            for newLoc in self.GetAdjacents(toLoc):
                if not newLoc in Paths:
                    heapq.heappush(Potentials, 
                        (moveCost + self.__CalcMoveCost(toLoc, newLoc, ActivePiece),
                        toLoc, newLoc))
        return Paths


    
    ## REQ: Integer x and y coordinates.
    ## RET: Boolean indicating whether the coordinates fall
    ##  on the map.
    def IsOnBoard(self, xPosition, yPosition):
        ValidY = (yPosition >= 0) and (yPosition < len(self._map))
        if ValidY:
            ValidX = (xPosition >= 0) and (xPosition < len(self._map[yPosition]))
        else:
            ValidX = False
        return (ValidY and ValidX)
    
    ## REQ: Integer coordinates.
    ## RET: List of adjacent map coordinates.
    def GetAdjacents(self, Position):
        ## 1 -- Takes valid coordinates corresponding to a space on the board
        ## 2 -- Returns the set of adjacent spaces
        xPosition = Position[0]
        yPosition = Position[1]
        Adjacents = set([])
        #Set YPosition modifier for hexagonal adjacency
        if xPosition % 2 == 0:
                YModifier = -1
        else:
                YModifier = 1
        #TODO coordinate with pieces, players and terrain to only show passable/usable adjacents
        #Check that each location is on the board, if so then add to Adjacents
        if self.IsOnBoard(xPosition, yPosition + 1):
                Adjacents.add((xPosition, yPosition + 1))
        if self.IsOnBoard(xPosition, yPosition + 1):
                Adjacents.add((xPosition, yPosition + 1))
        if self.IsOnBoard(xPosition + 1, yPosition):
                Adjacents.add((xPosition +1, yPosition))
        if self.IsOnBoard(xPosition + 1, yPosition + YModifier):
                Adjacents.add((xPosition + 1, yPosition + YModifier))
        if self.IsOnBoard(xPosition - 1, yPosition):
                Adjacents.add((xPosition -1, yPosition))
        if self.IsOnBoard(xPosition - 1, yPosition + YModifier):
                Adjacents.add((xPosition - 1, yPosition + YModifier))
        return Adjacents

    ##################---Private methods---##################


    def __CalcMoveCost(self, fromLoc, toLoc, checkPiece)
        """Calculate the cost of movement from fromLoc to toLoc for the check piece.
        
        These should be adjacent steps on the map. This calculation does NOT take interim
        spaces into consideration."""
        #Temporary placeholder - in a test map of move costs use the new space value.
        return self._map[toLoc[1]][toLoc[0]]

    def __testBoard(self):
        #Check that every point on the map always has a space.
        #Check null and bad map string matrices.
        #Check null and bad piece string matrices.
    #Check distance calculations on validation maps/pieces.
        pass
