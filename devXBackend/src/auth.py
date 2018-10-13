import spotipy
import spotipy.util as util
import sys


import numpy as np


import urllib.request


#username = 'greedosan' #placeholder value here
client_id = '64c8c6d551c74a7c90e8db5c2cb42ace' #placeholder value here
client_secret = 'c0e6aa2b7fde4ad9b1f58523ef80d95c' #placeholder value here
redirect_uri = 'http://localhost:8888/callback/'
scope = 'user-read-recently-played'



if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

sp = spotipy.Spotify(auth=token)

#if token:  
#    results = sp.current_user_saved_tracks()
#    for item in results['items']:
#        track = item['track']
#        print (track['name'] + ' - ' + track['artists'][0]['name'])
#else:
#    print ("Can't get token for", username)

#name = "Post Malone"
#results = sp.search(q='artist:' + name, type='artist')

# General album covers from featured playlists
def download_album_featured_playlists(n_playlists = 50, n_tracks = 100, folder_name = 'pics'):
    results = sp.featured_playlists(limit=n_playlists)

    #print(results['playlists']['items'])
    index = 0
    for playlists in results['playlists']['items']:
        playlist_id = playlists['id']
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
            
        #print(playlist_tracks['images'])    
        #for tracks in playlist_tracks:
        #    print(tracks)   
        #print(sp.search(q='playlist:' + playlist_id, type = 'playlist'))

#def download_personalized_playlist()

#download_album_featured_playlists()
#    print(item)
    
#print (results['artists'])



