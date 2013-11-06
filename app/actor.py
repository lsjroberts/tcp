# ----------- Actor ------------
# Actors represent interactable characters within the game world.
# ----------------------------


# -------- Imports --------

import config


# -------- Actor --------
# Base abstract actor
class Actor( ):

    # -------- Init --------
    # Constructor
    #
    # @return Actor
    def __init__( self ):
    	self.sprite = None

    def setSprite( self, sprite ):
    	self.sprite = sprite

   	def update( self, frameTime, lifeTime ):
   		pass


# ----------- Moveable Actor -----------
# An actor that can be repositioned after instantiation.
class MoveableActor( Actor ):

	def move( self, frameTime ):
		pass

	def update( self, frameTime, lifeTime ):
		self.move( frameTime )
		Actor.update( self, frameTime, lifeTime )


# ----------- Controllable Actor -----------
# An actor that can be positioned by the player.
class ControllableActor( MoveableActor ):
	pass