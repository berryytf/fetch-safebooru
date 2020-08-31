import safebooru_app

def main():
    user_tags = str(input("Enter tags separated by comma (e.g. cat ears, blue eyes): "))

    while True:
        try:
            user_limit = int(input("Enter number of desired images: "))
            if type(user_limit) == int:
                break
        except:
            print("Invalid input.")

    user_tags = clean_tags(user_tags) # Fix up the tags so the safebooru API can read it

    post_object = safebooru_app.pysbooru(user_tags, user_limit)
    image_data = post_object.get_posts() #Get posts from object.
    if image_data == False:
        print("Didn't work :(") # Crash the ship!
    else:
        posts = generate_post_link(image_data)
        images = generate_image_link(image_data)
        temp = 1
        for i in range(user_limit):
            print(f'Post {temp}: {posts[i]}, Image URL: {images[i]}')
            temp += 1

#Create link for actual post
def generate_post_link(data):
    base_url = 'https://safebooru.org/index.php?page=post&s=view'
    ids = []
    #iterate through list of dictionaries
    for i in range(len(data)):
        ids.append(base_url + f'&id={str(data[i]["id"])}')
    
    return ids

#Create link to direct image file.
def generate_image_link(data):
    base_url = 'https://safebooru.org/images'
    ids = []
    #iterate through list of dictionaries
    for i in range(len(data)):
        ids.append(base_url + f'/{str(data[i]["directory"])}/{str(data[i]["image"])}')  

    return ids

def clean_tags(tags):
    fixed_user_tags = tags.replace(', ', '%20').replace(' ', '_').lower() # API readable tags

    return fixed_user_tags

if __name__ == '__main__':
    main()

