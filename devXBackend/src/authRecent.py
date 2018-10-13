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

def getPersonalizedRecent():
    results = ss.current_user_playlists()
    for item in results['items']:
       # print item
        image_list =  item['id']
        playlist_tracks = #
        print image_list
        for image in image_list:
            if (len(image_list) != 0):
                image = image_list[-1]['url']
                print image_list
                list.append(image)
    return list

                
print getPersonalizedRecent()