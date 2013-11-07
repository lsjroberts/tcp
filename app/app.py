# ----------- App ------------
# Handles all general application logic
# ----------------------------


# -------- Imports --------

import pygame, config
from event import EventManager, EventListener


# -------- App --------
# Global app class.
class App( ):

    # -------- Init --------
    # Constructor, creates the app and sets it to running.
    #
    # @return App
    def __init__( self ):
        # Set the app to running
        self.running = True

        # Create the event manager
        self.events = EventManager( )
        self.events.registerListener( AppListener() )

        # Set the app mode
        self.mode = 'game'

        self.updateableObjects = {
            'game': [],
            'menu': []
        }

    # -------- Tick --------
    # Process a single tick of the game loop.
    #
    # @param  int  frameTime Number of milliseconds passed since the previous tick.
    # @param  int  lifeTime  Number of milliseconds since pygame initialised.
    # @return None
    def tick( self, frameTime, lifeTime ):
        if 'game' == self.mode:
            self.tickGame( frameTime, lifeTime )
        else:
            self.tickMenu( frameTime, lifeTime )

    # -------- Tick Game --------
    # Process a single tick within the game mode.

    # @param  int  frameTime Number of milliseconds passed since the previous tick.
    # @param  int  lifeTime  Number of milliseconds since pygame initialised.
    # @return None
    def tickGame( self, frametime, lifeTime ):
        for obj in self.updateableObjects['game']:
            pass

    # -------- Tick Menu --------
    # Process a single tick within the menu mode.

    # @param  int  frameTime Number of milliseconds passed since the previous tick.
    # @param  int  lifeTime  Number of milliseconds since pygame initialised.
    # @return None
    def tickMenu( self, frametime, lifeTime ):
        for obj in self.updateableObjects['menu']:
            pass


    def addUpdateableObject( self, mode, obj ):
        self.updateableObjects[mode].append( obj )


# -------- App Listener --------
# Listen for and handle app events.
class AppListener( EventListener ):

    def notify( self, event ):

        if isinstance( event, PygameEvent ):
            if pygame.QUIT == event.data.type:
                config.app.running = False
                print 'Exiting app...'


# ----------- Updateable Game Object -----------
# An object that is updated each tick when the app is in game mode
class UpdateableGameObject( ):

    def __init__( self ):
        config.app.addUpdateableObject( 'game', self )

    # ----------- Update -----------
    # 
    # @param  int  frameTime Number of milliseconds passed since the previous tick.
    # @param  int  lifeTime  Number of milliseconds since pygame initialised.
    # @return None
    def update( self, frameTime, lifeTime ):
        raise NotImplementedError( 'You must define an update() method on descendants of UpdateableGameObject' )


# ----------- Updateable Menu Object -----------
# An object that is updated each tick when the app is in menu mode
class UpdateableMenuObject( ):

    def __init__( self ):
        config.app.addUpdateableObject( 'menu', self )

    # ----------- Update -----------
    # 
    # @param  int  frameTime Number of milliseconds passed since the previous tick.
    # @param  int  lifeTime  Number of milliseconds since pygame initialised.
    # @return None
    def update( self, frameTime, lifeTime ):
        raise NotImplementedError( 'You must define an update() method on descendants of UpdateableMenuObject' )