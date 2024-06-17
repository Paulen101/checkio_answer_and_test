import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Setup Spotipy client
scope = 'user-modify-playback-state,user-read-playback-state'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def control_spotify(command):
    if command.strip() == 'toggle_play_pause':
        # Toggle play/pause
        playback_state = sp.current_playback()
        if playback_state and playback_state['is_playing']:
            sp.pause_playback()
        else:
            sp.start_playback()
    elif command.strip() == 'next_track':
        # Next track
        sp.next_track()

print("Enter 'toggle_play_pause' to play/pause, 'next_track' to skip to the next track.")
while True:
    command = input("Enter command: ")
    control_spotify(command)
