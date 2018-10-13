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

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print (track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print  ("Can't get token for", username)
