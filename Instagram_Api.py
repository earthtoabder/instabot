import requests
import random
import time
from instabot import Bot
import os 
import glob

if os.path.exists("config/*the.art.bot_uuid_and_cookie.json"):
    os.remove("config/*the.art.bot_uuid_and_cookie.json")
else:
    print("The json file does not exist")   

# keys
username = "the.art.bot"
password = "ArtBot00"
# getting into insta servers
api = Bot()
time.sleep(5)
api.login(username=username,password=password)

# opening the files
pictures_names = open("insta_pictures_files.txt").read().splitlines()
posted = open("insta_posted_pictures.txt").read().splitlines()
quotes = open("Quotes.txt").read().splitlines()

# the upload function
def upload_media():
    api.upload_photo(f"/Users/Abder/Desktop/Twitter_Api_Stuff/Pictures/{random_pic}",caption=f"{random_quote}.")
    print("image posted!")

# posting file function
def posted_pictures_file():
    with open('insta_posted_pictures.txt',"a+") as posted_pictures_file:
    	if random_pic not in posted:
            posted_pictures_file.write(random_pic+"\n")	
    with open("posted_quotes_insta.txt","a+") as posted_quotes:
        if random_quote not in posted_quotes:
            posted_quotes.write(random_quote+"\n")   

# to see if everything works`

# the loop for uploading
for pic in pictures_names:
    while pic not in posted:
        random_pictures = random.choices(pictures_names)   
        random_pic = random_pictures[-1]
        random_quote = random.choices(quotes)
        random_quote = random_quote[-1]
        posted = open("insta_posted_pictures.txt").read().splitlines()
        posted_quotes = open("posted_quotes_insta.txt").read().splitlines()
        if random_pic in posted:
    	    continue
        if len(random_quote) > 120:
            continue
        posted_pictures_file()	
        print(f'Posting: {random_pic}')
        try:
            upload_media()
        except:
            print("Media ignored!")
            continue
        time.sleep(6*60**2)
print("We are done boss!")