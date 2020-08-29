import safebooru_app

def main():
    user_tags = str(input("Enter tags separated by comma (e.g. cat ears, blue eyes): "))
    user_limit = int(input("Enter number of desired images: "))

    user_tags = clean_tags(user_tags)

    post_object = pysafebooru.pysbooru(user_tags, user_limit)
    image_data = post_object.get_posts()
    if image_data == False:
        print("Didn't work :(")
    else:
        images = generate_post_link(image_data)

        temp = 1
        for i in images:
            print(f"Image {temp}: ".format() + i)
            temp += 1

def generate_post_link(data):
    base_url = 'https://safebooru.org/index.php?page=post&s=view'
    ids = []
    for i in range(len(data)):
        ids.append(base_url + '&id=' + str(data[i]['id']))
    
    return ids

def clean_tags(tags):
    fixed_user_tags = tags.replace(', ', '%20').replace(' ', '_').lower()

    return fixed_user_tags

if __name__ == '__main__':
    main()