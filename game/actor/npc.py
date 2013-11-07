# ------------ NPC ------------
# Non-playable characters
# -----------------------------


# -------- Imports --------

from app.npc import ConversationalNPC, EmotionalNPC
from app.sprite import AnimatedSprite


# ----------- Shop Assistant -----------
#
class ShopAssistant( ConversationalNPC ):

	def __init__( self ):
		sprite = AnimatedSprite( 'npc/shop-assistant.png' )

		sprite.addAnimationState( 'idle',         0,  3,  2 )
		sprite.addAnimationState( 'idle-fidget',  4,  7,  4 )
		sprite.addAnimationState( 'idle-chat',    8, 11,  4 )

		sprite.setAnimationState( 'idle' )

		self.setSprite( sprite )


# ----------- Founder Assistant -----------
#
class FounderAssistant( ConversationalNPC, EmotionalNPC ):

	def __init__( self ):
		sprite = AnimatedSprite( 'npc/founder-assistant.png' )

		sprite.addAnimationState( 'idle',         0,  3,  2 )
		sprite.addAnimationState( 'idle-fidget',  4,  7,  4 )
		sprite.addAnimationState( 'walk-left',    8, 11,  4 )
		sprite.addAnimationState( 'walk-right',  12, 15,  4 )
		sprite.addAnimationState( 'idle-chat',   16, 19,  4 )

		sprite.setAnimationState( 'idle' )

		self.setSprite( sprite )