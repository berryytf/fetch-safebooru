import json
import random
import urllib.request as urllib2

"""
Uses the safebooru API. There is no API key needed.
"""

class pysbooru:
    def __init__(self, tags='', post_limit=100): #post limit default 100 images
        self.tags = 'tags=' + tags
        self.post_limit = 'limit=' + str(post_limit)
        self.post_id = ''
        self.image = ''

    def get_posts(self):
        images = []
        post_ids = []

        #does stuff.
        try:
            post_array = self.__create_response(str(self.post_limit), self.tags) #generate json response
        except:
            return False
        else:
            return post_array

    # Private function to deal with link concatenation
    def __create_response(self, *args):
        booru_url = 'https://safebooru.org/index.php?page=dapi&s=post&q=index&json=1' # Default url for all responses
        image_dict = []

        
        while image_dict == []:
            page_number = random.randint(1, 50)
            if len(args) == 0:
                return False
            else:
                for i in args:
                    booru_url = booru_url + f'&{i}'
            booru_url = booru_url + '&pid=' + str(page_number)

            json_obj = urllib2.urlopen(booru_url) # json into an object
            image_dict = json.load(json_obj) # Stores list of image dictionaries into a variable

        return image_dict
    
    #Create link for actual post
    def generate_post_link(self, data):
        base_url = 'https://safebooru.org/index.php?page=post&s=view'
        ids = []
        #iterate through list of dictionaries
        for i in range(len(data)):
            ids.append(base_url + f'&id={str(data[i]["id"])}')
        
        return ids

    #Create link to direct image file.
    def generate_image_link(self, data):
        base_url = 'https://safebooru.org/images'
        ids = []
        #iterate through list of dictionaries
        for i in range(len(data)):
            ids.append(base_url + f'/{str(data[i]["directory"])}/{str(data[i]["image"])}')  

        return ids


