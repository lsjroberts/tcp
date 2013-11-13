# ------------ TCP ------------
# @author Laurence Roberts
# -----------------------------


# -------- Init --------

# Import config
import app.config as config

# Initialise pygame
import pygame

# if 'windows' == config.settings['platform']:
# 	import pygame._view

pygame.init( )

# Create the app
from app.app import App
from app.event import PygameEvent
app = config.app = App( )

# Setup the screen
config.screen = pygame.display.set_mode( [
	config.settings['screen_w'],
	config.settings['screen_h']
] )
pygame.display.set_caption( config.settings['title'] )
# pygame.display.set_icon(pygame.image.load('sprites/player/player-life.png').convert_alpha())
config.screen.convert( )

# Create the clock
clock = pygame.time.Clock( )



# -------- TEMPORARY --------
config.sprites = pygame.sprite.LayeredUpdates( )
config.spriteGroups['all'] = pygame.sprite.Group( )

from game.world.level1 import Level1
app.setMode( 'game' )
app.setWorld( Level1() )
# ------ ENDTEMPORARY -------



# -------- Game Loop --------
while app.running:

	# Capture events
	for e in pygame.event.get( ):
		event = PygameEvent( e )
		app.events.post( event )

	# Process tick
	clock.tick( config.settings['fps'] )
	app.tick( clock.get_time(), pygame.time.get_ticks() )


# -------- Exit --------
pygame.quit( )