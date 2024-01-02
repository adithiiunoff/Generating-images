import webbrowser
from unsplash.api import Api
from unsplash.auth import Auth
import requests

client_id = "a1J2JYkkh0iXV6s6Melcg5cUufP-yEM989lOrpvBMVk"
client_secret = "pEtx5rKCDXIInpqozKLlX8oyPFDmHByzUPv94pIgOxw"
redirect_uri = 0

auth = Auth(client_id, client_secret, redirect_uri)
api = Api(auth)

def get_photo_url(photo_id):
    try:
        photo = api.photo.get(photo_id)
        return photo.urls.regular
    except Exception as e:
        print(f"Error fetching photo details: {e}")
        return None

def open_image_in_browser(photo_id):
    photo_url = get_photo_url(photo_id)

    if photo_url:
        webbrowser.open(photo_url)
    else:
        print("Failed to retrieve photo details.")

if __name__ == "__main__":
    try:
        prompt = input("Enter Description: ")

        if (prompt == "surprise me"):
            random_photo = api.photo.random()
            first_photo = random_photo[0].id
        else:
            photos = api.search.photos(prompt)
            photo = photos['results']
            first_photo = photo[0].id
        # random_photo = api.photo.random()
        # print(first_photo)
        open_image_in_browser(first_photo)
    except Exception as e:
        print(f"Error retrieving random photo: {e}")

    