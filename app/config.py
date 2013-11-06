# ----------- Config ----------
# Shared configuration across all modules
# -----------------------------

from sys import platform

settings = {
	'title': 'TCP',
	'fps': 60,
	'platform': 'unknown',
	'screen_w': 800,
	'screen_h': 600
}

if 'linux' == platform or 'linux2' == platform:
	settings['platform'] = 'linux'
elif 'darwin' == platform:
	settings['platform'] = 'mac'
elif 'win32' == platform or 'cygwin' == platform:
	settings['platform'] = 'windows'

folders = {
	'assets': 'assets/'
}

spriteLayers = {
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