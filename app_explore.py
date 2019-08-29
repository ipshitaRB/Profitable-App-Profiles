from csv import reader

open_apple_file = open('AppleStore.csv', encoding='utf8')
apple_content = reader(open_apple_file)
ios_app_data = list(apple_content)

# open and load google app contents in to a list
open_google_file = open('googleplaystore.csv', encoding='utf8')
android_content = reader(open_google_file)
android_app_data = list(android_content)

