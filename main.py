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
        posts = post_object.generate_post_link(image_data)
        images = post_object.generate_image_link(image_data)
        temp = 1
        for i in range(user_limit):
            print(f'Post {temp}: {posts[i]}, Image URL: {images[i]}')
            temp += 1

def clean_tags(tags):
    fixed_user_tags = tags.replace(', ', '%20').replace(' ', '_').lower() # API readable tags

    return fixed_user_tags

if __name__ == '__main__':
    main()

