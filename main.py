from instragram import Instragram
from dotenv import load_dotenv
from os import environ
load_dotenv()

names = [

]

if(len(names) != 0):
    instaBot = Instragram(environ.get("USER"), environ.get("PASSWORD"))
    instaBot.login()

    for name in names:
        instaBot.search(name)
        instaBot.follow()
        print(name + " is followed")
else:
    print("empty names list!!!")
