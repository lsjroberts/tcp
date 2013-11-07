# ----------- Popup -----------
# Handles displaying popups on the screen
# -----------------------------


# -------- Imports --------



# ----------- Popup -----------
# Abstract popup
class Popup( ):

	def __init__( self ):
		self.pos = None

	def update( self, frameTime, lifeTime ):
		pass