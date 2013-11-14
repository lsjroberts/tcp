# ----------- Scene -----------
# Handles scene logic
# -----------------------------


# -------- Imports --------

import pygame, config
from sprite import StaticSprite


# ----------- Scene -----------
# A scene comprised of a set of layers.
class Scene( ):

	def __init__( self ):
		self.layers = []
		self.actors = []

	def addLayer( self, layer ):
		self.layers.append( layer )

	def addActor( self, actor ):
		self.actors.append( actor )


# ----------- Scene Layer -----------
# A layer image with depth position in the scene.
class SceneLayer( StaticSprite ):

	def __init__( self, src, depth ):
		# self.image = pygame.image.load( config.folders['scenes'] + src ).convert_alpha( )
		StaticSprite.__init__( self, config.folders['scenes'] + src )
		self.depth = depth