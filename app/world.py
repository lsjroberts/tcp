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
		if self.scene is not None:
			self.unloadScene( )
		self.scene = scene

	def unloadScene( self ):
		if self.scene is None:
			raise Exception( 'Can not unload scene, none set' )
		self.scene = None


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