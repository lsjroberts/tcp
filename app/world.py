# ----------- World -----------
# Handles world logic
# -----------------------------


# -------- Imports --------

import pygame, config


# ----------- World -----------
# 
class World( ):
	
	def __init__( self ):
		pass

	def setScene( self, scene ):
		self.scene = scene


# ----------- Scene -----------
# A scene comprised of a set of layers.
class Scene( ):

	def __init__( self ):
		pass

	def addLayer( layer ):
		self.layers.append( layer )


# ----------- Scene Layer -----------
# A layer image with depth position in the scene.
class SceneLayer( ):

	def __init__( self, src, depth ):
		self.image = pygame.image.load( config.folders['scenes'] + src ).convert_alpha( )
		self.depth = depth