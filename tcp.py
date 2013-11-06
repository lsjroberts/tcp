# ------------ TCP ------------
# @author Laurence Roberts
# -----------------------------


# -------- Init --------

# Import config
import app.Config as config


# Initialise pygame
import pygame

if 'windows' == config.app['platform']:
	import pygame._view

pygame.init( )


# Create the app
from app.App import App
from app.Event import PygameEvent

app = config.app = App( )


# Setup the screen
config.screen = pygame.display.set_mode( [
	config.screen_w,
	config.screen_h
] )
pygame.display.set_caption( config.app_title )
# pygame.display.set_icon(pygame.image.load('sprites/player/player-life.png').convert_alpha())
config.screen.convert( )


# Create the clock
clock = pygame.time.Clock( )


# -------- Game Loop --------
while app.running:

	# Capture events
	for e in pygame.event.get( ):
		event = PygameEvent( e )
		app.events.fire( event )

	# Process tick
	clock.tick( config.fps )
	app.tick( clock.get_time() )


# -------- Exit --------
pygame.quit( )