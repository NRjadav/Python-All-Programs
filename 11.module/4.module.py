


import instaloader

mydata = instaloader.Instaloader()

name=input("Enter profilename: ")

pic=mydata.download_profile(name,profile_pic_only=True)