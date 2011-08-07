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

    def __init__(self): 
        _map = []
        _pieces = []
        
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
              
    def CalcPieceMoveCost(self, fromLoc):
        """ """
    RouteMap = []
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
    ## REQ: Integer x and y coordinates.
    ## RET: Boolean indicating whether the coordinates fall
    ##  on the map.
    def __IsOnBoard(self, xPosition, yPosition):
        ValidY = (yPosition >= 0) and (yPosition < len(self._map))
        if ValidY:
            ValidX = (xPosition >= 0) and (xPosition < len(self._map[yPosition]))
        else:
            ValidX = False
        return (ValidY and ValidX)
    
    ## REQ: Integer coordinates.
    ## RET: List of adjacent map coordinates.
    def __GetAdjacents(self, xPosition, yPosition):
        ## 1 -- Takes valid coordinates corresponding to a space on the board
        ## 2 -- Returns the set of adjacent spaces
    
        xPosition = testSpace[0]
        yPosition = testSpace[1]

        Adjacents = []

        #Set YPosition modifier for hexagonal adjacency
        if xPosition % 2 == 0:
            YModifier = -1
        else:
            YModifier = 1
        
        #Check that each location is on the board, if so then add to Adjacents
        if self.__IsOnBoard(xPosition, yPosition + 1):
            Adjacents.append(xPosition, yPosition + 1)
    
        if self.__IsOnBoard(xPosition, yPosition + 1):
            Adjacents.append(xPosition, yPosition + 1)

        if self.__IsOnBoard(xPosition + 1, yPosition):
            Adjacents.append(xPosition +1, yPosition)
    
        if self.__IsOnBoard(xPosition + 1, yPosition + YModifier):
            Adjacents.append(xPosition + 1, yPosition + YModifier)

        if self.__IsOnBoard(xPosition - 1, yPosition):
            Adjacents.append(xPosition -1, yPosition)
    
        if self.__IsOnBoard(xPosition - 1, yPosition + YModifier):
            Adjacents.append(xPosition - 1, yPosition + YModifier)

        return Adjacents

    ## REQ: Adjacent from and two coordinates.  A Piece object.
    ## RET: Integer movement cost for the piece
    def __CalcMoveCost(self, fromLoc, toLoc, checkPiece)
        """Calculate the cost of movement from fromLoc to the adjacent toLoc for the check piece"""
        if toLoc in self.__getAdjacents(fromLoc[0], fromLoc[1]):
            Movecost = 1
        else:
            pass ##TODO add exception - fromLoc and toLoc should be adjacent

    def __testBoard(self):
        #Check that every point on the map always has a space.
        #Check null and bad map string matrices.
        #Check null and bad piece string matrices.
    #Check distance calculations on validation maps/pieces.
        pass
