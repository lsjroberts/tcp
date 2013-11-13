# ---------- Level 1 ----------
# 
# -----------------------------


# -------- Imports --------

from app.world import World
from game.scene.office import OfficeScene
from game.actor.player import Founder


# ----------- Level 1 -----------
# 
class Level1( World ):

	def __init__( self ):
		World.__init__( self )
		self.setScene( OfficeScene() )
		self.scene.addActor( Founder() )