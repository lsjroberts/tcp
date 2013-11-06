# ----------- Sprite ------------
# Handles different types of sprites.
# ----------------------------


# -------- Imports --------

import pygame, config


# -------- Sprite --------
# Base abstract sprite
class Sprite( pygame.sprite.Sprite ):

    # -------- Init --------
    # Constructor
    #
    # @return Sprite
    def __init__( self ):
        self.groups = self.groups or []
        pygame.sprite.Sprite.__init__( self, self.groups )


# -------- Static Sprite --------
# A sprite that has a single frame.
class StaticSprite( Sprite ):

    # -------- Init --------
    # Constructor
    #
    # @return StaticSprite
    def __init__( self, src, vector ):
        Sprite.__init__( self )

        self.vector = vector
        self.image = pygame.image.load( config.folders['assets'] + src ).convert_alpha( )
        self.rect = self.image.get_rect( )
        self.rect.x = self.vector.x
        self.rect.y = self.vector.y

    # -------- Update --------
    # Update the sprite's position
    #
    # @return StaticSprite
    def update( self, frameTime, lifeTime ):
        self.rect.x = self.vector.x
        self.rect.y = self.vector.y


# -------- Animated Sprite --------
# A sprite that can have multiple frames.
class AnimatedSprite( Sprite ):

    # -------- Init --------
    # Constructor
    #
    # @return AnimatedSprite
    def __init__( self, src, vector ):
        Sprite.__init__( self )

        self.frames = [ ]
        self.numFrames = 0
        self.states = { }
        self.vector = vector

        self.srcImage = pygame.image.load( config.folders['assets'] + src ).convert_alpha( )
        self.srcWidth, self.srcHeight = self.srcImage.get_size( )

        self.lastUpdate = 0
        self.frame = 0
        self.state = ''