
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


# Download image from url and resize
def download_image_from_url(image_url, full_file_name, dictionary):
    # Request image from url
    urllib.request.urlretrieve(image_url,full_file_name)
    # Open and resize image
    #image = Image.open(full_file_name)
    #image = image.resize((16,16))
    image = cv2.imread(full_file_name)
    image = cv2.resize(image, (16,16))

    # Find average color of image
    color_pic = cv2.resize(image, (1, 1))

    #color = color_pic.getpixel((0, 0))
    
    # Split each color value into batch (of 1) 256x256x256 possible colors
    color = np.round(np.array(color_pic))
    color = tuple(color[0][0])
    
    # Add the file_name to the dictionary for the color combination
    if color in dictionary.keys():
        dictionary[color].append(full_file_name)
    else:
        
        dictionary[color] = [full_file_name]
    # Saves in dictionary and folder

    cv2.imwrite(full_file_name, image)


# Download album
def download_album_from_playlists(results, dictionary, n_tracks = 100, folder_name = 'pics', starting_index = 0):
    index = starting_index
    
   # Create target Directory if it doesnt exist
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    n = 0 

    # Loops through the playlists 
    for playlist in results['playlists']['items']:
        # For each playlist get the id
        playlist_id = playlist['id']
        
        # Call on the ID to get the tracks
        playlist_tracks = sp.user_playlist_tracks(user = username, playlist_id = playlist_id, limit =n_tracks )
        
        playlist_tracks = playlist_tracks['items']
        n += len(playlist_tracks)
        # Loop through the tracks 
        for tracks in playlist_tracks:
            
            # Get the album cover for the track
            
            image_list = tracks['track']['album']['images']
            
            #Maybe add the album name to an additional dictionary to be able to list the used ones
            #album_name = tracks['track']['album']['name'])


            # Check that there exists album art
            if (len(image_list) != 0):

                # Take the smallest image out of the list of album art
                image_url = image_list[-1]['url']

                # Create path to save image
                full_file_name = folder_name + '/'+str(index) + '.jpg'
                index += 1

                # Download image from url
                download_image_from_url(image_url, full_file_name, dictionary)
                
        print("Length of current dictionary: " + str(len(dictionary))+ ", with "+ str(n) + " songs.")

# General album covers from featured playlists
def download_album_featured_playlists(dictionary, n_playlists = 50, n_tracks = 100, folder_name = 'featured', starting_index = 0):
    results = sp.featured_playlists(limit=n_playlists)    
    download_album_from_playlists(results, n_tracks = n_tracks, folder_name = folder_name, starting_index = starting_index, dictionary = dictionary)

# General album covers from categorical playlists
def download_album_categorical_playlists(dictionary,category = 'chill',n_playlists= 50, n_tracks = 100, folder_name = 'chill', starting_index = 0):
    results = sp.category_playlists(category_id = category, limit = n_playlists)
    download_album_from_playlists(results, n_tracks = n_tracks, folder_name = folder_name, starting_index = starting_index, dictionary = dictionary)


def update_all_general_images_and_dicts():
    #print("Downloading featured album covers")    
    #featured_dict = {}
    #download_album_featured_playlists(dictionary = featured_dict, folder_name = 'featured')
    #np.save('featured_dict.npy', featured_dict)     
    #print("Done with featured album covers")       
    
    
    #print("Downloading hiphop album covers") 
    #hiphop_dict = {}
    #download_album_categorical_playlists(dictionary = hiphop_dict, category = 'hiphop', folder_name = 'hiphop')
    #np.save('hiphop_dict.npy', hiphop_dict )  
    #print("Done with hiphop album covers")     
    
    #print("Downloading rock album covers") 
    #rock_dict = {}    
    #download_album_categorical_playlists(dictionary = rock_dict, category = 'rock', folder_name = 'rock')
    #np.save('rock_dict.npy', rock_dict )  
    #print("Downloading rock album covers")     
    
    #print("Downloading jazz album covers") 
    #jazz_dict = {}   
    #download_album_categorical_playlists(dictionary = jazz_dict, category = 'jazz', folder_name = 'jazz')
    #np.save('jazz_dict.npy', jazz_dict )  
    #print("Done with jazz album covers")

    #print("Downloading reggae album covers") 
    #reggae_dict = {}    
    #download_album_categorical_playlists(dictionary = reggae_dict, category = 'reggae', folder_name = 'reggae')
    #np.save('reggae_dict.npy', reggae_dict )  
    #print("Done with reggae album covers")

    #print("Downloading chill album covers") 
    #chill_dict = {}
    #download_album_categorical_playlists(dictionary = chill_dict, category = 'chill', folder_name = 'chill')
    #np.save('chill_dict.npy', chill_dict )  
    #print("Done with chill album covers")
   
    print("Downloading metal album covers") 
    metal_dict = {}
    download_album_categorical_playlists(dictionary = metal_dict, category = 'metal', folder_name = 'metal')
    np.save('metal_dict.npy', metal_dict )  
    print("Done with metal album covers")
    
    print("Downloading edm_dance album covers") 
    edm_dance_dict = {}
    download_album_categorical_playlists(dictionary = edm_dance_dict, category = 'edm_dance', folder_name = 'edm_dance')
    np.save('edm_dance_dict.npy', edm_dance_dict )  
    print("Done with edm_dance album covers")
  

    #print("Downloading country album covers")
    #country_dict={}    
    #download_album_categorical_playlists(dictionary = country_dict, category = 'country', folder_name = 'country')
    #np.save('country_dict.npy', country_dict )  
    #print("Done with country album covers")


    #print("Downloading pop album covers")
    #pop_dict={}    
    #download_album_categorical_playlists(dictionary = pop_dict, category = 'pop', folder_name = 'pop')
    #np.save('pop_dict.npy', pop_dict )  
    #print("Done with pop album covers")

    

    #country_dict = np.load('country_dict.npy').item()

def update_all_folder_images_and_dicts():    
    #all_dict={} 
    all_dict = np.load('all_dict.npy').item()   
    print("Downloading ALL album covers:")
    
    print("Downloading metal album covers") 
    download_album_categorical_playlists(dictionary = all_dict, category = 'metal', folder_name = 'metal_all')
    np.save('all_dict.npy', all_dict )  
    print("Done with metal album covers")

    print("Downloading edm_dance album covers") 
    download_album_categorical_playlists(dictionary = all_dict, category = 'edm_dance', folder_name = 'edm_dance_all')
    np.save('all_dict.npy', all_dict )  
    print("Done with edm_dance album covers")
    

    #print("Downloading hiphop album covers") 
    #download_album_categorical_playlists(dictionary = all_dict, category = 'hiphop', folder_name = 'hiphop_all')
    #np.save('all_dict.npy', all_dict )  
    #print("Done with hiphop album covers")     
    
    #print("Downloading rock album covers")    
    #download_album_categorical_playlists(dictionary = all_dict, category = 'rock', folder_name = 'rock_all')
    #np.save('all_dict.npy', all_dict )  
    #print("Downloading rock album covers")     
    
    #print("Downloading jazz album covers") 
    #download_album_categorical_playlists(dictionary = all_dict, category = 'jazz', folder_name = 'jazz_all')
    #np.save('all_dict.npy', all_dict )  
    #print("Done with jazz album covers")

    #print("Downloading reggae album covers")     
    #download_album_categorical_playlists(dictionary = all_dict, category = 'reggae', folder_name = 'reggae_all')
    #np.save('all_dict.npy', all_dict )  
    #print("Done with reggae album covers")
 

    #print("Downloading country album covers") 
    #download_album_categorical_playlists(dictionary = all_dict, category = 'country', folder_name = 'country_all')
    #np.save('all_dict.npy', all_dict )  
    #print("Done with country album covers")


    


update_all_folder_images_and_dicts()
#update_all_general_images_and_dicts()




