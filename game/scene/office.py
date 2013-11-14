# ---------- Office -----------
# Founder's office
# -----------------------------

# -------- Imports --------

import app.config as config
from app.scene import Scene, SceneLayer


# ----------- Office Scene -----------
# Founder's primary office
class OfficeScene( Scene ):

	def __init__( self ):
		Scene.__init__( self )

		self.addLayer( SceneLayer(
			'office/background.png',
			config.spriteLayers['sceneFar']
		) )