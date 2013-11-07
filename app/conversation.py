# -------- Conversation -------
# Handles conversations between the player and characters.
# -----------------------------


# -------- Imports --------



# ----------- Conversation -----------
#
class Conversation( ):

	def __init__( self ):
		self.actors = []

	def addActor( self, actor ):
		self.actors.append( actor )


# ----------- Message -----------
# A statement or question within a conversation
class Message( ):

	def __init__( self, content ):
		self.content = content

	def say( self ):
		pass


# ----------- Node -----------
# A branching conversational point
class Node( Message ):

	def __init__( self, content, choices ):
		Message.__init__( self, content )
		self.choices = choices