<<<<<<< HEAD
import sys
import spotipy
import spotipy.util as util

username = 'Stoolof'
scope = 'user-library-read'
client_id = '6b13d026884b48d3994070d7dad3cc49'
client_secret = '94cf8d05c5924ada9120cf61a9c7ca4f'
redirected_url = 'http://localhost:8888/callback/'

#util.prompt_for_user_token(username,scope,client_id=client_id,
#                           client_secret=client_secret,
#                           redirect_uri=redirected_url)


#export SPOTIPY_CLIENT_ID='6b13d026884b48d3994070d7dad3cc49'
#export SPOTIPY_CLIENT_SECRET='94cf8d05c5924ada9120cf61a9c7ca4f'
#export SPOTIPY_REDIRECT_URI='your-app-redirect-url'


scope = 'user-library-read'
=======

import spotipy
import spotipy.util as util
import sys
import os
import numpy as np
import urllib.request
import cv2
from PIL import Image
import requests
#from resizeimage import resizeimage

#username = 'greedosan' #placeholder value here
client_id = '64c8c6d551c74a7c90e8db5c2cb42ace' #placeholder value here
client_secret = 'c0e6aa2b7fde4ad9b1f58523ef80d95c' #placeholder value here
redirect_uri = 'http://localhost:8888/callback/'
scope = 'user-read-recently-played'

>>>>>>> master

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: %s username" % (sys.argv[0],))
    sys.exit()

<<<<<<< HEAD
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print (track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print  ("Can't get token for", username)
=======

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

sp = spotipy.Spotify(auth=token)


# Download image from url and resize
def download_image_from_url(image_url, full_file_name, dictionary):
    # Request image from url
    urllib.request.urlretrieve(image_url,full_file_name)
    # Open and resize image
    image = Image.open(full_file_name)
    image = image.resize((32,32))


    # Find average color of image
    color_pic = image.resize((1, 1))

    #color = color_pic.getpixel((0, 0))
    
    # Split each color value into batch (of 32) 8x8x8 possible colors
    color = np.round(np.array(color_pic)/32)
    color = tuple(color[0][0])

    # Add the file_name to the dictionary for the color combination
    if color in dictionary.keys():
        dictionary[color].append(full_file_name)
    else:
        
        dictionary[color] = [full_file_name]
    # Saves in dictionary and folder

    image.save(full_file_name)


# Download album
def download_album_from_playlists(results, dictionary, n_tracks = 100, folder_name = 'pics', starting_index = 0):
    index = starting_index
    
   # Create target Directory if it doesnt exist
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    # Loops through the playlists 
    for playlist in results['playlists']['items']:
        # For each playlist get the id
        playlist_id = playlist['id']
        
        # Call on the ID to get the tracks
        playlist_tracks = sp.user_playlist_tracks(user = username, playlist_id = playlist_id, limit =n_tracks )
        
        # Loop through the tracks 
        for tracks in playlist_tracks['items']:
            
            # Get the album cover for the track
            image_list = tracks['track']['album']['images']

            # Check that there exists album art
            if (len(image_list) != 0):

                # Take the smallest image out of the list of album art
                image_url = image_list[-1]['url']

                # Create path to save image
                full_file_name = folder_name + '/'+str(index) + '.jpg'
                index += 1

                # Download image from url
                download_image_from_url(image_url, full_file_name, dictionary)
        print(len(dictionary))

# General album covers from featured playlists
def download_album_featured_playlists(dictionary, n_playlists = 50, n_tracks = 100, folder_name = 'featured', starting_index = 0):
    results = sp.featured_playlists(limit=n_playlists)    
    download_album_from_playlists(results, n_tracks = n_tracks, folder_name = folder_name, starting_index = starting_index, dictionary = dictionary)

# General album covers from categorical playlists
def download_album_categorical_playlists(dictionary,category = 'chill',n_playlists= 50, n_tracks = 100, folder_name = 'chill', starting_index = 0):
    results = sp.category_playlists(category_id = category, limit = n_playlists)
    download_album_from_playlists(results, n_tracks = n_tracks, folder_name = folder_name, starting_index = starting_index, dictionary = dictionary)


def update_all_general_images_and_dicts():
    featured_dict = {}
    download_album_featured_playlists(dictionary = featured_dict, folder_name = 'featured')
    np.save('featured_dict.npy', featured_dict)     

    #chill_dict = {}
    #download_album_categorical_playlists(dictionary = chill_dict, category = 'chill', folder_name = 'chill')
    #np.save('chill_dict.npy', chill_dict)  
    
    #hiphop_dict = {}
    #download_album_categorical_playlists(dictionary = hiphop_dict, category = 'hiphop', folder_name = 'hiphop')
    #np.save('hiphop_dict .npy', hiphop_dict )  
    
    #rock_dict = {}    
    #download_album_categorical_playlists(dictionary = rock_dict, category = 'rock', folder_name = 'rock')
    #np.save('rock_dict.npy', rock_dict )  
    
    #jazz_dict = {}   
    #download_album_categorical_playlists(dictionary = jazz_dict, category = 'jazz', folder_name = 'jazz')
    #np.save('jazz_dict.npy', jazz_dict )  
    
    #reggae_dict = {}    
    #download_album_categorical_playlists(dictionary = reggae_dict, category = 'reggae', folder_name = 'reggae')
    #np.save('reggae_dict.npy', reggae_dict )  

    #edm_dance_dict = {}    
    #download_album_categorical_playlists(dictionary = edm_dance_dict, category = 'edm_dance', folder_name = 'edm_dance')
    #np.save('edm_dance_dict.npy', edm_dance_dict )  

    #rnb_dict = {}
    #download_album_categorical_playlists(dictionary = rnb_dict, category = 'rnb', folder_name = 'rnb')
    #np.save('rnb_dict.npy', rnb_dict )  

    #classical_dict={}    
    #download_album_categorical_playlists(dictionary = classical_dict, category = 'classical', folder_name = 'classical')
    #np.save('classical_dict.npy', classical_dict )  

    #metal_dict={}    
    #download_album_categorical_playlists(dictionary = metal_dict, category = 'metal', folder_name = 'metal')
    #np.save('metal_dict.npy', metal_dict )  

    #country_dict={}    
    #download_album_categorical_playlists(dictionary = country_dict, category = 'country', folder_name = 'country')
    #np.save('country_dict.npy', country_dict )  

    
    #chill_dict = np.load('chill_dict.npy').item()
    #country_dict = np.load('country_dict.npy').item()
    

update_all_general_images_and_dicts()
#download_image_from_url('https://i.scdn.co/image/46a1dcfa844e7fb2aeee759f70d333b9b95f0742', 'asd.jpg')
  




>>>>>>> master
