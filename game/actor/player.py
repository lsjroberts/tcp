# ----------- Player ----------
# Player controllable actors
# -----------------------------


# -------- Imports --------

from app.player import Player
from app.sprite import AnimatedSprite


# ----------- Hacker -----------
#
class Hacker( Player ):

	def __init__( self, vector=(0,0) ):
		sprite = AnimatedSprite( 'player/hacker.png', vector )

		sprite.addAnimationState( 'idle',         0,  3,  2 )
		sprite.addAnimationState( 'idle-fidget',  4,  7,  4 )
		sprite.addAnimationState( 'walk-left',    8, 11,  4 )
		sprite.addAnimationState( 'walk-right',  12, 15,  4 )
		sprite.addAnimationState( 'idle-chat',   16, 19,  4 )

		sprite.setAnimationState( 'idle' )

		self.setSprite( sprite )


# ----------- Founder -----------
#
class Founder( Player ):

	def __init__( self, vector=(0,0) ):
		sprite = AnimatedSprite( 'player/founder.png', vector )

		sprite.addAnimationState( 'idle',         0,  3,  2 )
		# sprite.addAnimationState( 'idle-fidget',  4,  7,  4 )
		# sprite.addAnimationState( 'walk-left',    8, 11,  4 )
		# sprite.addAnimationState( 'walk-right',  12, 15,  4 )
		# sprite.addAnimationState( 'idle-chat',   16, 19,  4 )

		sprite.setAnimationState( 'idle' )

		self.setSprite( sprite )


# ----------- Android -----------
#
class Android( Player ):

	def __init__( self, vector=(0,0) ):
		sprite = AnimatedSprite( 'player/android.png', vector )

		sprite.addAnimationState( 'idle',         0,  3,  2 )
		sprite.addAnimationState( 'idle-fidget',  4,  7,  4 )
		sprite.addAnimationState( 'walk-left',    8, 11,  4 )
		sprite.addAnimationState( 'walk-right',  12, 15,  4 )
		sprite.addAnimationState( 'idle-chat',   16, 19,  4 )

		sprite.setAnimationState( 'idle' )

		self.setSprite( sprite )