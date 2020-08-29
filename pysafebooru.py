import json
import random
import urllib.request as urllib2

"""
Uses the safebooru API. There is no API key needed.
"""

class pysbooru:
    def __init__(self, tags='', post_limit=100, page_range=20): #post limit default 100 images
        self.tags = 'tags=' + tags
        self.post_limit = 'limit=' + str(post_limit)
        self.post_id = ''
        self.image = ''
        self.page_range = page_range

    def get_posts(self):
        images = []
        post_ids = []

        #does stuff.
        try:
            post_array = self.__create_response(str(self.post_limit), self.tags) #generate json response
        except:
            return "Oops... Didn't work D:"
        else:
            return post_array

    # Private function to deal with link concatenation
    def __create_response(self, *args):
        page_number = random.randint(1, self.page_range)
        booru_url = 'https://safebooru.org/index.php?page=dapi&s=post&q=index&json=1' # Default url for all responses
        
        if len(args) == 0:
            return False
        else:
            for i in args:
                booru_url = booru_url + f'&{i}'.format()
        booru_url = booru_url + '&pid=' + str(page_number)

        json_obj = urllib2.urlopen(booru_url) # json into an object
        image_dict = json.load(json_obj) # Stores list of image dictionaries into a variable


        return image_dict

