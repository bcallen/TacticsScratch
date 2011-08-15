    from collections import deque
    import heapq
    import random

    def loadtestmap(length, width):
        global _map
        _map = []
        for i in range(length):
            row=[random.randint(1,100) for j in range(width)]
            _map.append(row)
        return _map
    def HeapMoveCosts(fromLoc):
        """ """
        moveCost = 0
        toLoc = fromLoc    
        ActivePiece = None
        Paths = {fromLoc : (moveCost, toLoc)}
        Potentials = [(__CalcMoveCost(fromLoc,toLoc,ActivePiece),
            fromLoc, toLoc) for toLoc in GetAdjacents(fromLoc)]
        heapq.heapify(Potentials)
        while Potentials != []:
            while True:
                currentMin = heapq.heappop(Potentials)
                if Potentials == [] or currentMin[2] not in Paths:
                    moveCost, fromLoc, toLoc = (currentMin[0], currentMin[1], currentMin[2])
                    break
            if not toLoc in Paths:
                Paths.setdefault(toLoc , (moveCost, fromLoc))
            for newLoc in GetAdjacents(toLoc):
                if not newLoc in Paths:
                    heapq.heappush(Potentials, 
                        (moveCost + __CalcMoveCost(toLoc, newLoc, ActivePiece),
                        toLoc, newLoc))
        return Paths

    #Old overly complicated way wo heapq
    def CalcPieceMoveCosts(fromLoc):
        """ """
        Paths = [(fromLoc, 0, None)]
        ActiveSpace = Paths[0][0]
        ActiveCost = 0
        ActivePiece = None
        ActiveIndex = None
        PathIndex = None
        Potentials = []
        NewPotentials = [(loc, ActiveCost + __CalcMoveCost(ActiveSpace,loc,ActivePiece), len(Paths)-1) for loc in GetAdjacents(ActiveSpace)]
        NewPotentials.sort(key = lambda np : np[1])
        Potentials.append(deque(NewPotentials))
        while not __IsEmpty(Potentials):
            NextStep = None  
            while True:
                PathIndex, ActiveIndex = [(record[0][2], idx)
                    for idx, record in enumerate(Potentials)
                    if record[0][1] ==  min([cost[1] for cost in list(zip(*Potentials))[0]])
                    ][0]
                NextStep = Potentials[ActiveIndex].popleft()
                if len(Potentials[ActiveIndex]) == 0:
                    del Potentials[ActiveIndex]
                if not(NextStep[0] in [MappedAlready[0] for MappedAlready in Paths]) or __IsEmpty(Potentials):
                    break
            if __IsEmpty(Potentials):
                break
            #Set up next path tuple
            Paths.append(tuple([NextStep[0], NextStep[1], PathIndex]))
            #Add new potentials.
            NewPotentials = []
            for loc in GetAdjacents(NextStep[0]):
                if not loc in [solvedLoc[0] for solvedLoc in Paths]:
                    NewPotentials.append(tuple([loc, NextStep[1]+__CalcMoveCost(NextStep[0], loc, ActivePiece),len(Paths)-1]))
            if len(NewPotentials)>0:
                NewPotentials.sort(key = lambda np:np[1])
                Potentials.append((deque(NewPotentials)))
        return Paths

    ## REQ: Integer x and y coordinates.
    ## RET: Boolean indicating whether the coordinates fall
    ##  on the map.
    def IsOnBoard(xPosition, yPosition):
        ValidY = (yPosition >= 0) and (yPosition < len(_map))
        if ValidY:
            ValidX = (xPosition >= 0) and (xPosition < len(_map[yPosition]))
        else:
            ValidX = False
        return (ValidY and ValidX)
    ## REQ: Integer coordinates.
    ## RET: List of adjacent map coordinates.
    def GetAdjacents(Position):
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
    #Check that each location is on the board, if so then add to Adjacents
        if IsOnBoard(xPosition, yPosition + 1):
            Adjacents.add((xPosition, yPosition + 1))
        if IsOnBoard(xPosition, yPosition + 1):
            Adjacents.add((xPosition, yPosition + 1))
        if IsOnBoard(xPosition + 1, yPosition):
            Adjacents.add((xPosition +1, yPosition))
        if IsOnBoard(xPosition + 1, yPosition + YModifier):
            Adjacents.add((xPosition + 1, yPosition + YModifier))
        if IsOnBoard(xPosition - 1, yPosition):
            Adjacents.add((xPosition -1, yPosition))
        if IsOnBoard(xPosition - 1, yPosition + YModifier):
            Adjacents.add((xPosition - 1, yPosition + YModifier))
        return Adjacents


    ##################---Private methods---##################
    ## REQ: Adjacent from and two coordinates.  A Piece object.
    ## RET: Integer movement cost for the piece
    def __IsEmpty(seq):
        try:
             return all(map(__IsEmpty, seq))
        except TypeError:
             return False


    def __CalcMoveCost(ActiveSpace,NewSpace,ActivePiece):
        return _map[NewSpace[1]][NewSpace[0]]
