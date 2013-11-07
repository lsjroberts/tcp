# ------- Hacking Scene -------
# Where shit gets hacked yo.
# -----------------------------


# -------- Imports --------

import config
from app.world import Scene, SceneLayer
from app.popup import Popup
from game.code import Parser, Compiler, Executer


# ----------- Hacking Scene -----------
# 01110101011
class HackingScene( Scene ):

	def __init__( self ):
		Scene.__init__( self )

		self.addLayer( SceneLayer(
			"hacking/wall-floor.jpg",
			config.spriteLayers['sceneFar']
		) )

		self.addLayer( SceneLayer(
			'hacking/desk.jpg',
			config.spriteLayers['sceneFar'] - 1
		) )

		self.addLayer( SceneLayer(
			'hacking/chair.jpg',
			config.spriteLayers['sceneNear']
		) )





class CodePopup( Popup ):

	def execute( self ):
		parsed   = Parser( self.code )
		compiled = Compiler( parsed )
		result   = Executer( compiled )