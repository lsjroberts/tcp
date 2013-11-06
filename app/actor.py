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


# ----------- Conversational Actor -----------
# An actor who can hold a conversation.
class ConversationalActor( Actor ):
	pass


# ----------- Emotional Actor -----------
# An actor who has emotions and reactions.
class EmotionalActor( Actor ):
	
	def addEmotion( emotion ):
		if self.emotions is None:
			self.emotions = {}

		self.emotions[emotion.name] = emotion

	def addTargetedEmotion( emotion, target ):
		if self.targetedEmotions is None:
			self.targetedEmotions = {}

		if self.targetedEmotions[target.name] is None:
			self.targetedEmotions[target.name] = {}

		self.targetedEmotions[target.name][emotion.name] = emotion