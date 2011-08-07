'''
Created on Jul 21, 2011

@author: Bonual
'''

class Piece:
    '''
    Pieces are objects that exist on the board.
    '''
    	

    def __init__(self):

	#Active indicates whether a piece is in the turn queue.
	_bActive = True
	_iExperience = 0

	###Actions:  contains a list of ability objects. Could also be a list or dictionary....
	_oActions = [] #TODO probably the base piece starts out with a simple attack

	###Movement cost detail
	_dictTerrainMoveCosts = []
	#Should altitude movement costs be derived entirely from agility?  Probably.
	_dictAltitudeMoveCosts = []

	#Matrix of terrain map costs spanning the entire map.
	#Function of the piece specific Move costs.
	#Used in conjunction with altitude and piece location
	#for movement calculations.
	_iTMapCosts = self.RefreshMoveCostMap()

	#Initialize base statistics (will be adtl in the future)
	_iStrength = 1
	_iStamina = 1
	_iWisdom = 1
	_iSpeed = 1

	#Dependent statistics - initialized here and recalced immediately.
	#Default move stats  TODO Could use nonlocal flags to set these?
	_iMovePoints = 1

	_iMaxHP = 1
	_iMaxMP = 1

	self.RecalcDependentStats()

	#Do we want engine characteristics to be built into the code
	#or should general parms (like these tens) live in a database.
	#Seems like they should be in a config file for easy/cons manipulation.
	_iCurrentHP = _iMaxHP
	_iCurrentMP = _iMaxMP
    
    ###############----Accessors----###############
    #Would it make sense to combine any of these? Or should each one have its own method?
    def setExperience(self, newExperience)
	if newExperience > 0 then:
	    self._iExperience = newExperience
	else:
	    print("I'm an invalid experience input!",newLevel)


     def setHP(self, newHP)
	if newHP > 0 and newHP <= self._iMaxHP then:
	    self._iCurrentHP = newHP
	else:
	    print("I'm an invalid HP!",newHP) #TODO replace this with an exception

    def setMP(self, newMP)
	if newMP > 0 and newMP <= self.iMaxMP then:
	    self._iCurrentMP=newMP
	else:
	    print("I'm an invalid MP!",newMP) #TODO replace this with an exception

    def setMoveCost(self, moveCostDict)
	#TODO add check
	self._dictMoveCost = moveCostDict

    def setStrength(self, newStr)
    	#TODO Check the value of newStr.  Make sure that it is in bounds.
	#Get the range of valid values from the database.
	self._iStrength = newStr
    
    def setStamina(self, newSta)
	#TODO Add checking	
	self._iStamina = newSta

    def setWisdom(self, newWis)
	#TODO Add checking
	self._iWisdom = newWis
    
    def getExperience(self)
	return self._iExperience

    def getLevel(self)
	return (self._iExperience / 100)

    def getMaxHP(self)
	return self._iMaxHP

    def getMaxMP(self)
	return self._iMaxMP

    def getCurrentHP(self)
	return self._iCurrentHP

    def getCurrentMP(self)
	return self._iCurrentMP

    def getStrength(self)
	return self._iStrength

    def getStamina(self)
	return self._iStamina

    def getWisdom(self)
	return self._iWisdom
    ###############
    def RecalcDependentStats(self)
	self._iMovePoints = self._iSpeed * 10
	self._iMaxHP = self._iStamina * 10
	self._iMaxMP = self._iWisdom * 10  

    #Convenience method: change current HP, checking that the final HP is not
    #higher than the defined maximum and is not less than zero.
    def ChangeHP(self, HPChange)
	if self._iCurrentHP + HPChange > maxHP:
	    setCurrentHP(self._iMaxHP)
	elif self._iCurrentHP + HPChange < 0:
	    self.setCurrentHP(0)
	else:
	    self.setCurrentHP(self._iCurrentHP + HPChange)
	return self.getCurrentHP()


    def ChangeMP(self, MPChange)
	setCurrentMP(self._iCurrentMP + MPChange)
	return getCurrentMP()


    def	ChangeExperience(self, ExpChange)
	#Does this need a check for valid ExpChange?
	newExp = ExpChange + (self._iExperience % 100)
	#Should this 100 be stored in the database?  Or is ok to hardcode?
	while newExp >= 100:
	    newExp = newExp - 100
	    self.LevelUp()
	self.SetExperience(self.GetExperience() + ExpChange)


    def LevelUp(self)
	#This should probably include end of level stat changes
	#with the intent that it be overridden by subclasses often.

	#TODO these are very simple, hardcoded placeholders.  
	#We'll definitely revise once we start to calibrate the game.

	self.setStrength(self.getStrength() + 1)
	self.setStamina(self.getStamina() + 1)
	self.setWisdom(self.getWisdom() + 1)
	self.RefreshDependantStats()
    
    #This method loads/refreshes the base cost map for the
    #piece. This is referenced by the board for use in the
    #particular piece's movement calculations.
    def RefreshMoveCostMap(self, board)
	##TODO Ensure that the board is a matrix.  Should be filled with spaces.
	for column in board:
	    for space in column:
		self._dictTerrainMoveCost(space.getTerrain)


##############-----Private Methods-----#####################
    
    
