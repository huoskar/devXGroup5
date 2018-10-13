import sys
import spotipy
import spotipy.util as util

#util.prompt_for_user_token(username,scope,client_id='bf050439613e46a698879a7317ae2d9b',client_secret='2d346cde651842f6b9bafa6c1ea8663a',your-app-redirect-url',redirect_uri='https://developer.spotify.com/dashboard/applications/bf050439613e46a698879a7317ae2d9b')
scope = 'user-top-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope)

list = []

if token:
    sp = spotipy.Spotify(auth=token)
    
    def getPersonalizedImageUrl():
        results = sp.current_user_top_tracks(limit=20, offset=0, time_range='medium_term')
        for item in results['items']:
            image_list =  item['album']['images']
            for image in image_list:
                if (len(image_list) != 0):
                    image = image_list[-1]['url']
                    list.append(image)
        return list

                
    print getPersonalizedImageUrl()

  

    
else:
    print "Can't get token for", username

    
    print ("Usage: %s username" % (sys.argv[0],))
    sys.exit()