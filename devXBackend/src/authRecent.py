import sys
import spotipy
import spotipy.util as util
    
scope = 'playlist-read-private'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope)

ss = spotipy.Spotify(auth=token)

list = []

def getPersonalizedPlaylists():
    results = ss.current_user_playlists()
    for item in results['items']:
       image_list =  item['id']
       
       playlist_tracks = ss.user_playlist_tracks(user = username, playlist_id = image_list, limit =50 )
        #print(playlist_tracks['items']) 
    for names in playlist_tracks['items']:
            image_list = names['track']['album']['images']
            if (len(image_list) != 0):
                # take the smallest image out of the list of album art
                image_url = image_list[-1]['url']
                list.append(image_url)
    return list



getPersonalizedPlaylists()

