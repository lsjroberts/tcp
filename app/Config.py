# ----------- Config ----------
# Shared configuration across all modules
# -----------------------------

from sys import platform

app = {
	'title': 'TCP',
	'fps': 60,
	'platform': 'unknown'
}

if 'linux' == platform or 'linux2' == platform:
	app['platform'] = 'linux'
elif 'darwin' == platform:
	app['platform'] = 'mac'
elif 'win32' == platform or 'cygwin' == platform:
	app['platform'] = 'windows'

sprite_layers = {
	'conversation': 1,
	'pc': 2,
	'npc': 3,
	'background_near': 97,
	'background_mid': 98,
	'background_far': 99
}

world = {
	
}

colours = {
	
}

app = None
screen = None