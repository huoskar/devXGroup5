
import spotipy
import spotipy.util as util
import sys
import os
import numpy as np
import urllib.request

from PIL import Image
from resizeimage import resizeimage

#username = 'greedosan' #placeholder value here
client_id = '64c8c6d551c74a7c90e8db5c2cb42ace' #placeholder value here
client_secret = 'c0e6aa2b7fde4ad9b1f58523ef80d95c' #placeholder value here
redirect_uri = 'http://localhost:8888/callback/'
scope = 'user-read-recently-played'


token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

sp = spotipy.Spotify(auth=token)


# Download album
def download_album_from_playlists(results, n_tracks = 100, folder_name = 'pics', starting_index = 0):
    index = starting_index
    
   # Create target Directory if it doesnt exist
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)


    for playlist in results['playlists']['items']:
        playlist_id = playlist['id']
        playlist_tracks = sp.user_playlist_tracks(user = username, playlist_id = playlist_id, limit =n_tracks )
        #print(playlist_tracks['items']) 
        for names in playlist_tracks['items']:
            image_list = names['track']['album']['images']
            
            # Check that there exists album art
            if (len(image_list) != 0):
                # take the smallest image out of the list of album art
                image_url = image_list[-1]['url']

                # Create path to save image
                full_file_name = folder_name + '/'+str(index) + '.jpg'
                index += 1

                # Download image from url
                urllib.request.urlretrieve(image_url,full_file_name)


# General album covers from featured playlists
def download_album_featured_playlists(n_playlists = 50, n_tracks = 100, folder_name = 'featured', starting_index = 0):
    results = sp.featured_playlists(limit=n_playlists)    
    download_album_from_playlists(results, n_tracks = n_tracks, folder_name = folder_name, starting_index = starting_index)


def download_album_categorical_playlists(category = 'chill',n_playlists= 50, n_tracks = 100, folder_name = 'chill', starting_index = 0):
    results = sp.category_playlists(category_id = category, limit = n_playlists)
    download_album_from_playlists(results, n_tracks = n_tracks, folder_name = folder_name, starting_index = starting_index)



download_album_featured_playlists()

